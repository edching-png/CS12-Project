class Enemy:
    def __init__(self, path, speed_frames=60):
        self.path = path
        self.index = 0
        self.x, self.y = path[0]
        self.frames_waited = 0
        self.speed_frames = speed_frames
        self.size = CELL_SIZE
        self.hp = 1

    def update(self, occupied_cells, front_enemy_pos=None):
        if self.index < len(self.path) - 1:
            self.frames_waited += 1
            if self.frames_waited >= self.speed_frames:
                next_cell = self.path[self.index + 1]
                if next_cell not in occupied_cells and (front_enemy_pos is None or next_cell != front_enemy_pos):
                    self.index += 1
                    self.x, self.y = self.path[self.index]
                    self.frames_waited = 0
        else:
            return True 
        return False
