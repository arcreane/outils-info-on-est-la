SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

class Ennemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 40
        self.height = 20


    def set_position(self, x, y):
        self.x = max(self.width, min(SCREEN_WIDTH - self.width, x))
        self.y = y