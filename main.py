import pyxel
import math

CELL_SIZE = 16
GRID_ROWS = 16
GRID_COLS = 16
FPS = 30

class GameController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        pyxel.init(GRID_COLS*CELL_SIZE, GRID_ROWS*CELL_SIZE, fps=FPS)
        pyxel.mouse(True)
        pyxel.run(self.update, self.view.draw)

    def update(self):
        if not self.model.game_started and not self.model.game_over:
            if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                if (GRID_COLS * CELL_SIZE // 2 - 20 < pyxel.mouse_x < GRID_COLS * CELL_SIZE // 2 + 20 and
                        GRID_ROWS * CELL_SIZE // 2 - 10 < pyxel.mouse_y < GRID_ROWS * CELL_SIZE // 2 + 10):
                    self.model.game_started = True
        elif self.model.game_over:
            if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                if (GRID_COLS * CELL_SIZE // 2 - 20 < pyxel.mouse_x < GRID_COLS * CELL_SIZE // 2 + 20 and
                        GRID_ROWS * CELL_SIZE // 2 < pyxel.mouse_y < GRID_ROWS * CELL_SIZE // 2 + 20):
                    self.model.reset_game()
        else:
            if pyxel.frame_count % 60 == 0:
                self.model.spawn_enemy()
            self.model.update_enemies()
            self.model.update_projectiles()
            self.model.update_cooldown()
            if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT):
                self.model.tower_shoot(pyxel.mouse_x, pyxel.mouse_y)

model = GameModel()
view = GameView(model)
GameController(model, view)
