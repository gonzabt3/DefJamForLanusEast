import pygame
from pygame.locals import *


class Select(pygame.sprite.Sprite):
    def __init__(self):

        self.player1=-1
        self.player2=-1
        self.posicion1=0
        self.posicion2=3
        self.select1=pygame.image.load("selectScreen/select1.png").convert_alpha()
        self.select2 = pygame.image.load("selectScreen/select2.png").convert_alpha()
        self.rect1=self.select1.get_rect()
        self.rect2=self.select2.get_rect()
        self.selectScreen = pygame.image.load("selectScreen/selectScreen.jpg").convert_alpha()
        self.mantiene_pulsado = False
        self.x1=160
        self.y1=70
        self.x2=500
        self.y2=70
        self.rect1.top,self.rect1.left=(self.y1,self.x1)
        self.rect2.top, self.rect2.left = (self.y2, self.x2)

    def pantalla(self):
        salir = False
        reloj1 = pygame.time.Clock()

        pygame.font.init()
        screen = pygame.display.set_mode((750, 500))
        fondo = self.selectScreen


        while not salir:

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    salir = True
                k = pygame.key.get_pressed()

                if not self.mantiene_pulsado:
                    if k[K_c]:
                        print "c"
                        self.posicion1 -= 1

                    if k[K_v]:
                        print "v"
                        self.posicion1 += 1

                    elif k[K_SPACE] and self.player1 == -1:
                        self.player1 = self.posicion1
                    if k[K_LEFT]:
                        print "LEFT"
                        self.posicion2 -= 1
                    if k[K_RIGHT]:
                        self.posicion2 += 1
                    elif k[K_RETURN] and self.player2 == -1:
                        self.player2 = self.posicion2

                if self.posicion1 < 0:
                    self.posicion1 = 0
                elif self.posicion1 > 3:
                    self.posicion1 = 3

                if self.posicion2 < 0:
                    self.posicion2 = 0
                elif self.posicion2 > 3:
                    self.posicion2 = 3

                # indica si el usuario mantiene pulsada alguna tecla.
                self.mantiene_pulsado = k[K_c] or k[K_v] or k[K_LEFT] or k[K_RIGHT] or k[K_RETURN] or k[K_SPACE]


            screen.blit(fondo, (0, 0))

            self.update()

            # reloj1.tick()  # relog
            pygame.display.flip()
            # pygame.display.update()
            pygame.time.delay(100)

    def update(self):


        self.selectScreen.blit(self.select1, self.rect1)
        self.moverSelect()




    def moverSelect(self):
        if self.posicion1==0:
           self.x1=160
        if self.posicion2==0:
           self.x2=160
        if self.posicion1==1:
            self.x1=275
        if self.posicion2==1:
            self.x2 =275
        if self.posicion1==2:
            self.x1=385
        if self.posicion2==2:
            self.x2 =385
        if self.posicion1==3:
            self.x1=500
        if self.posicion2==3:
            self.x2 =500

        # self.rect1.x=self.x1
        # print self.rect1
        self.rect1.move_ip(self.x1,70)
        # self.rect2.move_ip(self.x2, 70)

    # def mover(self,x,numeroSelect):  # metodo que mueve al chabon
    #     #muevo los recs de lugar
    #     if numeroSelect==1:
    #         self.rect1.move_ip(x,70)
    #
    #     if numeroSelect==2:
    #         self.rect2.move_ip(x,70)


