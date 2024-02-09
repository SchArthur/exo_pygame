# Example file showing a basic pygame "game loop"
import pygame
import random
import pbm_loader
import convert

img_to_load = 'gigachad'
img_format = 'mnsl'

running = True

class newGame:
    def __init__(self, width = 800, height = 600, running = True) -> None:
        try :
            self.image = pbm_loader.newImage(img_to_load+'.'+img_format)
            print('opening file')
        except FileNotFoundError:
            print('creating file')
            convert.pngToMNSL(img_to_load)
            self.image = pbm_loader.newImage(img_to_load+'.'+img_format)
        width = self.image.img_x
        height = self.image.img_y
        # pygame setup
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((width, height))

        self.pixels = self.createRandomPixels()
        self.run(running)


    def createRandomPixels(self,min_count = 1, max_count = 100) -> list:
        pixels = []
        max_width = self.screen.get_width()
        max_height = self.screen.get_height()
        pixel_count = random.randrange(min_count,max_count)
        for _ in range(0, pixel_count):
            x = random.randrange(0, max_width)
            y = random.randrange(0, max_height)
            pixels.append((x,y))
        return pixels


    def run(self, running = True):
        self.running = running 
        self.screen.fill("white")
        self.image.drawImg(self.screen)
        while self.running:
            # poll for events
            # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.pixels = self.createRandomPixels()
                if event.type == pygame.QUIT:
                    self.running = False

            # fill the screen with a color to wipe away anything from last frame
            # for pixel in self.pixels:
            #     self.screen.set_at(pixel, "black")
            # RENDER YOUR GAME HERE
            # flip() the display to put your work on screen
            pygame.display.flip()

            self.clock.tick(60)  # limits FPS to 60

        pygame.quit()

jeu = newGame()  