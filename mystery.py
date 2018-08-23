import pygame
import game_obj
from random import randint
from flavor import flavors, flavorOfTheFortnite

def main():
    pygame.init()
 
    screen = pygame.display.set_mode([900, 900])
    pygame.display.set_caption('Mystery Flavor')
 
    #pygame.mouse.set_visible(False)

    done = False
    clock = pygame.time.Clock()

    game = game_obj.Game()

    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        clock.tick(60)
 
    pygame.quit()
 

if __name__ == "__main__":
    main()