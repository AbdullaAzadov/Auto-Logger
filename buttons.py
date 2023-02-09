import pygame

class Button():
    def __init__(self, screen):
        self.screen = screen

    def blit(self, low, med, high):
        self.low = low
        self.med = med
        self.high = high

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.low == False:
            # LOW
            if 52 < mouse[0] < 221 and 90 < mouse[1] < 150:
                self.screen.blit(pygame.image.load('images/low.png'), (52, 90))
                if click[0] == 1:
                    self.screen.blit(pygame.image.load('images/low_p.png'), (52, 91))
                    self.screen.blit(pygame.image.load('images/med_n.png'), (236, 90))
                    self.screen.blit(pygame.image.load('images/high_n.png'), (425, 90))
                    return 10
            else:
                self.screen.blit(pygame.image.load('images/low_n.png'),(52, 90))

        else:
            self.screen.blit(pygame.image.load('images/low_p.png'), (52, 91))


        if self.med == False:
            # MEDIUM
            if 236 < mouse[0] < 405 and 90 < mouse[1] < 150:
                self.screen.blit(pygame.image.load('images/med.png'), (236, 90))
                if click[0] == 1:
                    self.screen.blit(pygame.image.load('images/med_p.png'), (236, 91))
                    self.screen.blit(pygame.image.load('images/high_n.png'), (425, 90))
                    return 20
            else:
                self.screen.blit(pygame.image.load('images/med_n.png'), (236, 90))
        else:
            self.screen.blit(pygame.image.load('images/med_p.png'), (236, 91))

        if self.high == False:
            # HIGH
            if 425 < mouse[0] < 594 and 90 < mouse[1] < 150:
                self.screen.blit(pygame.image.load('images/high.png'), (425, 90))
                if click[0] == 1:
                    self.screen.blit(pygame.image.load('images/high_p.png'), (425, 91))
                    return 30
            else:
                self.screen.blit(pygame.image.load('images/high_n.png'), (425, 90))
        else:
            self.screen.blit(pygame.image.load('images/high_p.png'), (425, 91))
