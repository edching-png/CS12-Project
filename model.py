import math

from tower import *
from projectile import *
from enemy import *

class GameModel:
    def __init__(self):
        self.enemies = []
        self.projectiles = []
        self.spawned = 0
        self.enemy_limit = 5
        self.game_over = False
        self.game_started = False
        self.health = 2
        self.silver = 0

        path_cells = []
        for r in range(2, GRID_ROWS - 3):
            path_cells.append((2, r))
        for c in range(2, GRID_COLS - 3):
            path_cells.append((c, GRID_ROWS - 3))
        for r in range(GRID_ROWS - 3, 2, -1):
            path_cells.append((GRID_COLS - 3, r))

        self.path_pixels = [(c*CELL_SIZE, r*CELL_SIZE) for (c, r) in path_cells]
        self.tower = Tower(GRID_COLS//2, GRID_ROWS//2)

    def reset_game(self):
        self.enemies.clear()
        self.projectiles.clear()
        self.spawned = 0
        self.silver = 0
        self.health = 2
        self.game_over = False
        self.tower.cooldown = 0

    def spawn_enemy(self):
        if self.spawned < self.enemy_limit:
            self.enemies.append(Enemy(self.path_pixels))
            self.spawned += 1

    def update_enemies(self):
        occupied = set()
        for e in self.enemies[:]:
            e.frames_waited += 1
            if e.frames_waited >= e.speed_frames:
                if e.index < len(self.path_pixels) - 1:
                    next_tile = self.path_pixels[e.index + 1]
                    if next_tile not in occupied:
                        e.index += 1
                        e.x, e.y = self.path_pixels[e.index]
                        e.frames_waited = 0
                else:
                    self.health -= 1
                    self.enemies.remove(e)
                    if self.health <= 0:
                        self.game_over = True
                    continue
            occupied.add((e.x, e.y))

        if self.spawned >= self.enemy_limit and not self.enemies:
            self.game_over = True

    def update_projectiles(self):
        for proj in self.projectiles[:]:
            proj.update()
            for e in self.enemies[:]:
                if (abs(proj.x - e.x) < e.size and abs(proj.y - e.y) < e.size):
                    self.enemies.remove(e)
                    self.projectiles.remove(proj)
                    self.silver += 1
                    break
            if proj.x < 0 or proj.x > GRID_COLS*CELL_SIZE or proj.y < 0 or proj.y > GRID_ROWS*CELL_SIZE:
                if proj in self.projectiles:
                    self.projectiles.remove(proj)

    def tower_shoot(self, target_x, target_y):
        if self.tower.cooldown == 0:
            dx = target_x - self.tower.x
            dy = target_y - self.tower.y
            angle = math.atan2(dy, dx)
            self.projectiles.append(Projectile(self.tower.x, self.tower.y, angle))
            self.tower.cooldown = self.tower.cooldown_max

    def update_cooldown(self):
        if self.tower.cooldown > 0:
            self.tower.cooldown -= 1
