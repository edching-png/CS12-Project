import math

class Projectile:
    def __init__(self, x, y, angle, speed=2.4):
        self.x = x
        self.y = y
        self.vx = math.cos(angle) * speed
        self.vy = math.sin(angle) * speed
        self.radius = 5

    def update(self):
        self.x += self.vx
        self.y += self.vy
