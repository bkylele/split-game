import pygame
from game import *


_LEFT, _RIGHT, _JUMP = 1,2,3

_IMAGE = {"char_image" : pygame.image.load('./resources/character/char2.png'),
          "char_rev_image" : pygame.transform.flip(pygame.image.load('./resources/character/char2.png'), True, False),
          "npc" : pygame.image.load('./resources/objects/npc.png'),
          "officer" : pygame.image.load('./resources/objects/officer.png'),
          "tree" : pygame.transform.scale(pygame.image.load('./resources/objects/tree.png'), (300,400)),
          "char_hippie" : pygame.image.load('./resources/character/char_hippie.png'),
          "guitar" : pygame.transform.scale(pygame.image.load('./resources/objects/guitar.png'), (100,100)),
          }

class Game:
    def __init__(self):
        self._running = True
        self.state = GameState()


    def run(self) -> None:
        pygame.init()

        self._resize_surface((600,600))

        clock = pygame.time.Clock()

        while self._running:
            clock.tick(60)
            self._handle_events()

        pygame.quit()


    def _handle_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._end_game()
            if event.type == pygame.VIDEORESIZE:
                self._resize_surface(event.size)
            if event.type == pygame.KEYDOWN:
                self._handle_key_pressed(event.key)

        self._handle_keys()
        self._draw_frame()
        self.state.gravity()


    def _handle_key_pressed(self, key):
        if key == pygame.K_UP:
            self.state.player_move(_JUMP)
        if key == pygame.K_SPACE:
            self.state.scroll_text()
        if key == pygame.K_q: # debug convenience
            self._end_game()


    def _handle_keys(self) -> None:
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.state.player_move(_LEFT)
        if keys[pygame.K_RIGHT]:
            self.state.player_move(_RIGHT)


    def _draw_frame(self) -> None:
        surface = pygame.display.get_surface()
        surface.fill(pygame.Color(173,203,234))
        self._draw_ground(surface)
        self._draw_player(surface)
        pygame.display.flip()

    
    def _draw_player(self, surface) -> None:
        width = surface.get_width()
        height = surface.get_height()

        player_x, player_y = self.state.player_position

        actual_x = player_x * width
        actual_y = player_y * height

        left = actual_x - 34
        top = actual_y - 100

        if (not self.state.player_direction):
            surface.blit(_IMAGE["char_rev_image"], (left, top))
             # surface.blit(self.char_rev_image, (left, top))
        else:
            surface.blit(_IMAGE["char_image"], (left, top))
            # surface.blit(self.char_image, (left, top))


    def _draw_ground(self, surface) -> None:
        width = surface.get_width()
        height = surface.get_height()

        for obj in self.state.objects:
            if obj.image:
                surface.blit(_IMAGE[obj.name],
                             (obj.pos[0]*width, obj.pos[1]*height))
            else:
                pygame.draw.rect(
                        surface, obj.colors,
                        pygame.Rect(
                            obj.pos[0]*width, obj.pos[1]*height,
                            obj.size[0]*width, obj.size[1]*height))

        floor_level = self.state.ground.pos[1]
        pygame.draw.rect(
                surface, self.state.ground.colors,
                pygame.Rect(
                    0, floor_level*height,
                    width, height))

        self._draw_dialogue(surface)


    def _draw_dialogue(self, surface) -> None:
        width = surface.get_width()
        height = surface.get_height()

        font = pygame.font.Font(None, 24)
        text = font.render(self.state.get_dialogue(), True, pygame.Color(255,255,255))
        surface.blit(text, (width*.15, height*.83))



    def _end_game(self) -> None:
        self._running = False


    def _resize_surface(self, size: tuple[int,int]) -> None:
        pygame.display.set_mode(size, pygame.RESIZABLE)




if __name__ == '__main__':
    Game().run()
