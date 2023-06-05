class Player:
    def __init__(self):
        self._x = 0.15
        self._y = 0.75
        self._vert_acc = 0.005
        self._falling = True
        self._direction = True # True is right, False is left

        self.level = False 


    @property
    def pos(self):
        return self._x, self._y


    @property
    def direction(self):
        return self._direction


    @property
    def falling(self):
        return self._falling

    
    def go_left(self):
        self._x -= 0.005
        if self._x < 0:
            self._x = 0.9
            self.level = True
        if self._direction: # set direction to left
            self._direction = not self._direction


    def go_right(self):
        self._x += 0.005
        if self._x > 1:
            self._x = 0.1
            self.level = True
        if not self._direction: # set direction to right
            self._direction = not self._direction


    def jump(self):
        """If the player is not faling, and choose to jump,
        then set their state to falling and let their vertical
        acceleration increase again from -0.015"""
        if not self._falling:
            self._vert_acc = -0.015
            self._falling = True


    def fall(self):
        """Change the player's y value based on their vertical
        acceleration, and change their acceleration every time
        they fall one tick"""
        if self._falling:
            self._y += self._vert_acc
            self._vert_acc += 0.001
        if self._y >= 0.75:
            self._falling = False
            self._y = 0.75




__all__ = [Player.__name__]
