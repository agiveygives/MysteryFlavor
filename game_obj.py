import pygame
from flavor import commitFlavor, flavors, flavorOfTheFortnite

class Game(object):
    def __init__(self):
        # variables
        self.game_over = False
        self.flavor_font = pygame.font.Font('Courier Prime Code.ttf', 50)
        self.flavor_text = self.flavor_font.render(flavorOfTheFortnite, True, (0,0,0))

        #sprite lists
        self.all_sprites_list = pygame.sprite.Group()

        #player object
        #self.player = player_obj.Player('./assets/player-green.png', 2)
        #self.all_sprites_list.add(self.player)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            commitFlavor()
            return True
        if keys[pygame.K_ESCAPE]:
            return True
       
        return False

    def run_logic(self):
        if not self.game_over:
            self.all_sprites_list.update()

    def display_frame(self, screen):
        screen.fill([255,255,255])
        screen.blit(self.flavor_text, (10, 200))
        #screen.blit(background_image.image, background_image.rect)

        if not self.game_over:
            self.all_sprites_list.draw(screen)
 
        pygame.display.flip()