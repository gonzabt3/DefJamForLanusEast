import pygame
from pygame.locals import *


class Select(pygame.sprite.Sprite):
    def __init__(self, imagen,player):
        self.imagen = imagen
        self.rect = self.imagen.get_rect()
        self.posicionPermitidoDerecha = True
        self.posicionPermitidoIzquierda = True
        self.direccion=2

        if(player==1):
            self.player=1
            self.rect.top, self.rect.left = (75, 160)
            self.posicion=0
        elif(player==2):
            self.player = 2
            self.rect.top, self.rect.left = (75, 480)
            self.posicion = 3


    def update(self, superficie,posicion,apretada,direccion):
        if self.player==2:
            print "PLAYER 2 PERSONAJE: %d"%posicion
        if self.player==1:
            print "PLAYER 1 PERSONAJE: %d"%posicion
        if apretada == True:
            if direccion==1 and  posicion<=3 and self.posicionPermitidoDerecha!=False :
                self.posicionPermitidoIzquierda = True
                cordenadas=(110,0)
                self.rect.move_ip(cordenadas)
            if (posicion == 3):
                self.posicionPermitidoDerecha = False


            if direccion==0 and posicion>=0 and self.posicionPermitidoIzquierda!=False:
                self.posicionPermitidoDerecha = True
                cordenadas = (-110, 0)
                self.rect.move_ip(cordenadas)
                if (posicion == 0):
                    self.posicionPermitidoIzquierda= False
        superficie.blit(self.imagen, self.rect)


def main():
    import pygame

    pygame.init()
    pantalla = pygame.display.set_mode((750,500))
    salir = False
    reloj1 = pygame.time.Clock()
    imagen1 = pygame.image.load("selectScreen/select1.png").convert_alpha()
    imagen2 = pygame.image.load("selectScreen/select2.png").convert_alpha()
    selectScreen = pygame.image.load("selectScreen/selectScreen.jpg").convert_alpha()

    select1 = Select(imagen1,1)
    select2 = Select(imagen2,2)
    posicion1=select1.posicion
    posicion2=select2.posicion
    direccion1=select1.direccion
    direccion2 = select2.direccion
    leftsigueapretada, rightsigueapretada, upsigueapretada, downsigueapretada = False, False, False, False
    mantiene_pulsado = False

    while salir != True:  # LOOP PRINCIPAL
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
            k = pygame.key.get_pressed()
            apretada1=False
            apretada2=False
            if not mantiene_pulsado:
                if k[K_c]:
                    print "c"
                    posicion1 -= 1
                    direccion1=0
                    apretada1=True
                if k[K_v]:
                    print "v"
                    posicion1 += 1
                    direccion1 = 1
                    apretada1 = True
                elif k[K_SPACE]:
                    pass

                if k[K_LEFT]:
                    posicion2 -= 1
                    direccion2=0
                    apretada2 = True
                if k[K_RIGHT]:
                    posicion2 += 1
                    direccion2=1
                    apretada2 = True
                elif k[K_RETURN]  :
                    pass

            if posicion1 < 0:
                posicion1 = 0
            elif posicion1 > 3:

                posicion1 = 3

            if posicion2 < 0:
                posicion2 = 0
            elif posicion2 > 3:
                posicion2 = 3

            # indica si el usuario mantiene pulsada alguna tecla.
            mantiene_pulsado = k[K_c] or k[K_v] or k[K_LEFT] or k[K_RIGHT] or k[K_RETURN] or k[K_SPACE]

        reloj1.tick(8)
        pantalla.blit(selectScreen, (0, 0))

        select1.update(pantalla,posicion1,apretada1,direccion1)
        select2.update(pantalla, posicion2, apretada2, direccion2)
        pygame.display.update()

    pygame.quit()


main()