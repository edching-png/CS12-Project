class Tower:
    def __init__(self, col, row):
        self.x = col * CELL_SIZE + CELL_SIZE // 2
        self.y = row * CELL_SIZE + CELL_SIZE // 2
        self.cooldown = 0
        self.cooldown_max = 33  
