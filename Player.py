SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20

    def set_position(self, x, y):
        half_w = self.width / 2
        self.x = max(half_w, min(SCREEN_WIDTH - half_w, x))
        self.y = y


    def set_position(self, x, y):
        self.x = max(0, min(SCREEN_WIDTH - self.width, x))
        self.y = y

