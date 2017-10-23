import pygame
pygame.init()
fightSound=pygame.mixer.Sound("sonidos/otros/fight.wav")


class Fight(pygame.sprite.Sprite):
    def __init__(self):
        self.imagenFight = pygame.image.load("imagenes/fight.png").convert_alpha()
        self.rectFight = self.imagenFight.get_rect()
        self.contador=0

class Fondo(pygame.sprite.Sprite):
    def __init__(self):
        self.imagen=pygame.image.load("imagenes/fondo/enzoHause.gif").convert_alpha()
        self.rect=self.imagen.get_rect()
        self.fight=Fight()

    def update(self,pantalla):
        pantalla.blit(self.imagen,self.rect)


    def pintarFight(self,pantalla):

        if self.fight.contador<=25:
            if self.fight.contador==0:
                fightSound.play()
            pantalla.blit(self.fight.imagenFight,(250,175))
            self.fight.contador+=1
