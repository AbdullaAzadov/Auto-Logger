import pygame


class Start_B():
    def __init__(self, screen):
        self.screen = screen

    def blit(self, low, med, high):
        self.low = low
        self.med = med
        self.high = high

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.low == True or self.med == True or self.high == True:
            # START
            if 227 < mouse[0] < 419 and 194 < mouse[1] < 284:
                self.screen.blit(pygame.image.load('images/start.png'),(227, 194))
                if click[0] == 1:
                    self.screen.blit(pygame.image.load('images/start_p.png'), (227, 195))
                    return 100
            else:
                self.screen.blit(pygame.image.load('images/start_n.png'), (227, 194))

