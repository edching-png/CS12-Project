import pyxel
import math

from constants import *

class GameView:
    def __init__(self, model):
        self.model = model

    def draw(self):
        pyxel.cls(0)
        for r in range(GRID_ROWS):
            for c in range(GRID_COLS):
                pyxel.rectb(c * CELL_SIZE, r * CELL_SIZE, CELL_SIZE, CELL_SIZE, 1)
        for (x, y) in self.model.path_pixels:
            pyxel.rect(x, y, CELL_SIZE, CELL_SIZE, 3)

        pyxel.text(5, 5, f"Silver: {self.model.silver}", 7)
        pyxel.text(5, 15, f"Health: {self.model.health}", 8)

        if not self.model.game_started and not self.model.game_over:
            pyxel.rect(GRID_COLS * CELL_SIZE // 2 - 20, GRID_ROWS * CELL_SIZE // 2 - 10, 40, 20, 10)
            pyxel.text(GRID_COLS * CELL_SIZE // 2 - 15, GRID_ROWS * CELL_SIZE // 2 - 3, "START", 7)
        elif self.model.game_over:
            pyxel.text(GRID_COLS * CELL_SIZE // 2 - 30, GRID_ROWS * CELL_SIZE // 2 - 20, "GAME OVER", 8)
            pyxel.rect(GRID_COLS * CELL_SIZE // 2 - 20, GRID_ROWS * CELL_SIZE // 2, 40, 20, 10)
            pyxel.text(GRID_COLS * CELL_SIZE // 2 - 15, GRID_ROWS * CELL_SIZE // 2 + 7, "RESTART", 7)
        else:
            pyxel.circ(self.model.tower.x, self.model.tower.y, 8, 9)
            for e in self.model.enemies:
                pyxel.rect(e.x, e.y, e.size, e.size, 8)
            for p in self.model.projectiles:
                pyxel.circ(p.x, p.y, p.radius, 7)

            dx = pyxel.mouse_x - self.model.tower.x
            dy = pyxel.mouse_y - self.model.tower.y
            angle = math.atan2(dy, dx)
            gun_x = self.model.tower.x + math.cos(angle) * 16
            gun_y = self.model.tower.y + math.sin(angle) * 16
            pyxel.line(self.model.tower.x, self.model.tower.y, gun_x, gun_y, 7)
