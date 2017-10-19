import pygame

class Fight(pygame.sprite.Sprite):
    def __init__(self):
        self.imagenFight = pygame.image.load("imagenes/fight.png").convert_alpha()
        self.rectFight = self.imagenFight.get_rect()


class Fondo(pygame.sprite.Sprite):
    def __init__(self):
        self.imagen=pygame.image.load("imagenes/fondo/enzoHause.gif").convert_alpha()
        self.rect=self.imagen.get_rect()
        self.fight=Fight()

    def update(self,pantalla):
        pantalla.blit(self.imagen,self.rect)


    def pintarFight(self,pantalla):
        pantalla.blit(self.fight.imagenFight,self.fight.rectFight)