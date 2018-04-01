import pygame
from pygame.locals import *

pygame.init()
opcion=pygame.mixer.Sound("sonidos/selectChar.wav")
click=pygame.mixer.Sound("sonidos/clickChar.wav")
voces=[pygame.mixer.Sound("sonidos/enzoVoz.wav"),pygame.mixer.Sound("sonidos/pabloVoz.wav"),pygame.mixer.Sound("sonidos/fonteVoz.wav"),pygame.mixer.Sound("sonidos/lichaVoz.wav")]

class Select(pygame.sprite.Sprite):
    def __init__(self, imagen,player):
        self.imagen = imagen
        self.rect = self.imagen.get_rect()
        self.posicionPermitidoDerecha = True
        self.posicionPermitidoIzquierda = True
        self.direccion=2

        if(player==1):
            self.player=1
            self.rect.top, self.rect.left = (75, 270)
            self.posicion=1
        elif(player==2):
            self.player = 2
            self.rect.top, self.rect.left = (75, 380)
            self.posicion = 2


    def update(self, superficie,posicion,apretada,direccion):
        # if self.player==2:
        #     print "PLAYER 2 PERSONAJE: %d"%posicion
        # if self.player==1:
        #     print "PLAYER 1 PERSONAJE: %d"%posicion
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

    # musica
    pygame.mixer.music.load("sonidos/selectCharacterMusic.mp3")

    select1 = Select(imagen1,1)
    select2 = Select(imagen2,2)
    posicion1=select1.posicion
    posicion2=select2.posicion
    direccion1=select1.direccion
    direccion2 = select2.direccion
    leftsigueapretada, rightsigueapretada, upsigueapretada, downsigueapretada = False, False, False, False
    mantiene_pulsado = False
    seleccionar1=True
    seleccionarOpcion1=7
    seleccionar2=True
    seleccionarOpcion2 = 7
    pygame.mixer.music.play(2)
    while salir != True:  # LOOP PRINCIPAL
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True

            k = pygame.key.get_pressed()
            apretada1=False
            apretada2=False
            if not mantiene_pulsado:
                if seleccionar1==True:
                    if k[K_c]:
                        opcion.play()
                        print "c"
                        posicion1 -= 1
                        direccion1=0
                        apretada1=True
                    if k[K_v]:
                        opcion.play()
                        print "v"
                        posicion1 += 1
                        direccion1 = 1
                        apretada1 = True
                    elif k[K_SPACE]:
                        click.play()
                        print "barra"
                        seleccionar1=False
                        seleccionarOpcion1=posicion1
                        sonarVoz(seleccionarOpcion1)
                if seleccionar2==True:
                    if k[K_LEFT]:
                        opcion.play()
                        posicion2 -= 1
                        direccion2=0
                        apretada2 = True
                    if k[K_RIGHT]:
                        opcion.play()
                        posicion2 += 1
                        direccion2=1
                        apretada2 = True
                    elif k[K_RETURN]:
                        click.play()
                        print "enter"
                        seleccionar2=False
                        seleccionarOpcion2=posicion2
                        sonarVoz(seleccionarOpcion2)

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

            if(seleccionar1==False and seleccionar2==False):
                print "return"
                return (seleccionarOpcion1,seleccionarOpcion2)

        reloj1.tick(8)
        pantalla.blit(selectScreen, (0, 0))

        select1.update(pantalla,posicion1,apretada1,direccion1)
        select2.update(pantalla, posicion2, apretada2, direccion2)
        pygame.display.update()

    pygame.quit()

def sonarVoz(numeroJugador):
    voces[numeroJugador].play()
