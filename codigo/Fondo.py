import pygame
pygame.init()
fightSound=pygame.mixer.Sound("sonidos/otros/fight.wav")
finishHimSound=pygame.mixer.Sound("sonidos/otros/finishhim.mp3")


class Fight(pygame.sprite.Sprite):
    def __init__(self):
        self.imagenFight = pygame.image.load("imagenes/fight.png").convert_alpha()
        self.rectFight = self.imagenFight.get_rect()
        self.contador=0

class FinishHim(pygame.sprite.Sprite):
    def __init__(self):
        self.imagenFinishHim = pygame.image.load("imagenes/finishHim.png").convert_alpha()
        self.rectFinishHim = self.imagenFinishHim.get_rect()


class Fondo(pygame.sprite.Sprite):
    def __init__(self):
        self.imagen=pygame.image.load("imagenes/fondo/mk1.gif").convert_alpha()
        self.rect=self.imagen.get_rect()
        self.fight=Fight()
        self.finishHim=FinishHim()

    def update(self,pantalla):
        pantalla.blit(self.imagen,self.rect)


    def pintarFight(self,pantalla):
        if self.fight.contador<=25:
            if self.fight.contador==0:
                fightSound.play()
            pantalla.blit(self.fight.imagenFight,(250,175))
            self.fight.contador+=1

    def pintarFinishHim(self,pantalla,player1,player2):
        if(player1.estado==4):
            pantalla.blit(self.finishHim.imagenFinishHim,(175,120))
            finishHimSound.play()
        if(player2.estado==4):
            pantalla.blit(self.finishHim.imagenFinishHim, (175, 120))
            finishHimSound.play()