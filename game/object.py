class GameObject:
    def __init__(self, pos: tuple[int, int], size: tuple[int, int],
                 color: tuple[int,int,int]):
        self._x = pos[0]
        self._y = pos[1]
        self._width = size[0]
        self._height = size[1]
        self._colors = color


    @property
    def pos(self):
        """The position of the object in data will be it's top left point"""
        return self._x, self._y


    @property
    def size(self):
        return self._width, self._height


    @property
    def colors(self):
        return self._colors


    @property
    def image(self):
        return False


    def move(self):
        pass


class Ground(GameObject):
    def __init__(self, level: float,
                 colors: tuple[int, int, int]):
        self._x = 0
        self._y = level
        self._width = 1
        self._height = 1
        self._colors = colors
        # self._background = True



class Building(GameObject):
    def __init__(self, loc: int, width: int,
                 colors: tuple[int, int, int]):
        self._x = loc
        self._y = 0 # buildings are skyscrapers, so they always take up the whole screen
        self._width = width
        self._height = 1 # same here
        self._colors = colors
        # self._background = True


class MovingObject(GameObject):
    def __init__(self, pos: tuple[int, int], size: tuple[int, int],
                 color: tuple[int,int,int], speed: tuple[int, int]):
        super().__init__(pos, size, color)
        self._speed = speed


    def move(self):
        self._x += self._speed[0]
        self._y += self._speed[1]


class Car(MovingObject):
    def __init__(self, pos: tuple[int, int], speed: tuple[int, int]):
        super().__init__(pos, (.2,.1), (0,0,0), speed)


    def move(self):
        super().move()
        if self._x > 1.5:
            self._x = -0.5
        if self._x < -0.5:
            self._x = 1.5


class ImageObject(GameObject):
    def __init__(self, pos: tuple[int, int], name: str):
        super().__init__(pos, (0,0), (0,0,0))
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def image(self):
        return True


class Clone(ImageObject):
    def __init__(self, pos:int, reversed: bool):
        if reversed:
            super().__init__((pos,0.584), "char_rev_image")
        else:
            super().__init__((pos,0.584), "char_image")


class Npc(ImageObject):
    def __init__(self, pos: int):
        super().__init__((pos, 0.59), "npc")




__all__ = [GameObject.__name__,
           Ground.__name__,
           Building.__name__,
           MovingObject.__name__,
           Car.__name__,
           ImageObject.__name__,
           Npc.__name__,
           Clone.__name__,
           ]
