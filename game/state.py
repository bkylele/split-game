from game.player import *
from game.levels import *
from game.object import Ground


_LEVEL = {1:  Level1,
          2:  Level2,
          3:  Level3,
          4:  Level4,
          5:  Level5,
          6:  Level6,
          7:  Level7,
          8:  Level8,
          9:  Level9,
          10: Level10,
          11: Level11,
          12: Level12,
          13: Level13,
          14: Level14,
          15: Level15,
          16: Level16,
          17: Level17,
          18: Level18,
          19: Level19,
          20: Level20,
          21: Level21,
          22: Level22,
          23: Level23,
          24: Level24,
          25: Level25,
          26: Level26,
          27: Level27,
          28: Level28,
          29: Level29,
          30: Level30,
          31: Level31,
          }

_PATHS = {1:  ( 2 ,None ),
          2:  ( 3 ,1  ),
          3:  ( 4 ,2  ),
          4:  ( 5 ,3  ),
          5:  ( 6 ,4  ),
          6:  ( 7 ,5  ),
          7:  ( 8 ,6  ),
          8:  ( 9 ,7  ),
          9:  ( 10,8  ),
          10: ( 11,9  ),
          11: ( 12,10 ),
          12: ( 13,22 ),  # crossroads
          13: ( 14,12 ),
          14: ( 15,13 ),
          15: ( 16,14 ),
          16: ( 17,15 ),
          17: ( 18,16 ),
          18: ( 19,17 ),
          19: ( 20,18 ),
          20: ( 21,19 ),
          22: ( 12,23 ),
          23: ( 22,24 ),
          24: ( 23,25 ),
          25: ( 24,26 ),
          26: ( 25,27 ),
          27: ( 26,28 ),
          28: ( 27,29 ),
          29: ( 31,30 ),
        }



class GameState:
    def __init__(self):
        self._player = Player()
        self._ground = Ground(0.75, (0,0,0))
        self._level = 1
        self._map = _LEVEL[self._level]()

        self._current_text = 0
        self._current_speech = 0


    @property
    def objects(self) -> set["GameObject"]:
        """Returns all objects on this level"""
        for obj in self._map.objects:
            obj.move()
        return self._map.objects


    @property
    def ground(self) -> int:
        """Returns the y level at which the ground begins"""
        return self._ground
        # return self._ground.pos[1]

    
    @property
    def player_position(self) -> tuple[int,int]:
        """Returns the current fractional position of the player"""
        return self._player.pos


    @property
    def player_direction(self) -> bool:
        """Returns the direction that the player is facing"""
        return self._player.direction


    def get_dialogue(self) -> str:
        msg = self._map.dialogue[self._current_text]
        return msg


    def scroll_text(self):
        self._current_text += 1
        self._current_text = self._current_text % len(self._map.dialogue)


    def check_speech(self):
        for obj in self._object():
            if dialgoue.__name__ in obj.__dict__:
                self._current_speech += 1
                self._current_speech = self._current_speech % len(obj.dialogue)


    def player_move(self, action: int) -> None:
        """Given the key that was pressed, move the player.
        If the player goes to the next level, then update loaded attribte
        to request for a screen redraw, as well as resetting read dialogue"""
        match action:
            case 1:
                self._player.go_left()
                if self._player.level:
                    if self._level == 1:
                        self._player.level = False
                    else:
                        self._current_text = 0

                        # self._level -= 1
                        self._level = _PATHS[self._level][1]


                        self._map = _LEVEL[self._level]()
                        self._loaded = False
                        self._player.level = False
            case 2:
                self._player.go_right()
                if self._player.level:
                    self._current_text = 0

                    # self._level += 1
                    self._level = _PATHS[self._level][0]

                    self._map = _LEVEL[self._level]()
                    self._loaded = False
                    self._player.level = False
            case 3:
                self._player.jump()
            case _:
                pass


    def gravity(self) -> None:
        """Makes the player fall to the ground, If they fall below the
        ground, place them back on it, and set their falling state to
        false.""" 
        self._player.fall()



__all__ = [GameState.__name__,
           Player.__name__]


