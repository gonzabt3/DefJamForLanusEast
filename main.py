import pygame
from threading import Timer
class Peleador(pygame.sprite.Sprite):
    def __init__(self,imagenesQuieto):

        self.imagenQuieto=imagenesQuieto
        # self.imagen1=imagen1
        # self.imagen2=imagen2
        # self.imagen3=imagen3
        # self.imagenGolpe=imagenGolpe
        # self.imagenGolpe2 = imagenGolpe2
        # self.imagenesPuno=[self.imagenGolpe,self.imagenGolpe2]
        # self.imagenes = [self.imagen1, self.imagen2,self.imagen3]
        self.imagenActual=0
        self.imagen=self.imagenQuieto[self.imagenActual]
        self.rect=self.imagen.get_rect()
        self.rect.top,self.rect.left=(100,200)
        self.move=False

    def mover(self, vx, vy): #metodo que mueve al chabon
        self.rect.move_ip(vx, vy)

    def update(self, superficie,vx,vy):
        if(vx==0 and vy==0):
            self.move=False #me fijo si se esta moviendo
            self.estarQuieto(superficie)
        else:
            self.move=True





    # def pegarGolpe(self,spacesigueapretada,superficie):#pegar golpe
    #
    #     if(spacesigueapretada==True):
    #         for i in range(2):
    #             self.imagen = self.imagenesPuno[i]
    #             superficie.blit(self.imagen,self.rect)
    #             print i
    #
    def estarQuieto(self,superficie):
            print self.imagenActual
            self.nextImage(self.imagenActual,self.imagenQuieto)
            superficie.blit(self.imagenQuieto[self.imagenActual], self.rect)

    def nextImage(self,imagenActual,imagenesSec):#cambio de imagen:
        self.imagenActual += 1

        if self.imagenActual > (len(imagenesSec) - 1):  # si se fue de rango que lo ponga en 0
            self.imagenActual = 0

def main():


    pygame.init()
    pantalla = pygame.display.set_mode((600, 600))
    salir = False
    reloj1 = pygame.time.Clock()

    imagenParado1 = pygame.image.load("imagenes/zub_zero/parado/parado1.png").convert_alpha()
    imagenParado2 = pygame.image.load("imagenes/zub_zero/parado/parado2.png").convert_alpha()
    imagenParado3 = pygame.image.load("imagenes/zub_zero/parado/parado3.png").convert_alpha()
    imagenParado4 = pygame.image.load("imagenes/zub_zero/parado/parado4.png").convert_alpha()
    imagenParado5 = pygame.image.load("imagenes/zub_zero/parado/parado5.png").convert_alpha()
    imagenParado6 = pygame.image.load("imagenes/zub_zero/parado/parado6.png").convert_alpha()
    imagenParado7 = pygame.image.load("imagenes/zub_zero/parado/parado7.png").convert_alpha()
    imagenParado8 = pygame.image.load("imagenes/zub_zero/parado/parado8.png").convert_alpha()
    imagenParado9 = pygame.image.load("imagenes/zub_zero/parado/parado9.png").convert_alpha()
    imagenParado10 = pygame.image.load("imagenes/zub_zero/parado/parado10.png").convert_alpha()
    imagenParadoArray =[imagenParado1,imagenParado2,imagenParado3,imagenParado4,imagenParado5,imagenParado6,imagenParado7,imagenParado8,imagenParado9,imagenParado10]

    player1 = Peleador(imagenParadoArray)
    vx, vy = 0, 0
    velocidad = 7
    t = 0
    leftsigueapretada, rightsigueapretada, upsigueapretada, downsigueapretada,spacesigueapretada = False, False, False, False,False

    while salir != True:  # LOOP PRINCIPAL
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    leftsigueapretada = True
                    vx = -velocidad
                if event.key == pygame.K_RIGHT:
                    rightsigueapretada = True
                    vx = velocidad
                if event.key == pygame.K_UP:
                    upsigueapretada = True
                    vy = -velocidad
                if event.key == pygame.K_DOWN:
                    downsigueapretada = True
                    vy = velocidad
                if event.key == pygame.K_SPACE:
                    spacesigueapretada = True

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    leftsigueapretada = False
                    if rightsigueapretada:
                        vx = velocidad
                    else:
                        vx = 0
                if event.key == pygame.K_RIGHT:
                    rightsigueapretada = False
                    if leftsigueapretada:
                        vx = -velocidad
                    else:
                        vx = 0
                if event.key == pygame.K_UP:
                    upsigueapretada = False
                    if downsigueapretada:
                        vy = velocidad
                    else:
                        vy = -0
                if event.key == pygame.K_DOWN:
                    downsigueapretada = False
                    if upsigueapretada:
                        vy = -velocidad
                    else:
                        vy = 0
                if event.key == pygame.K_SPACE:
                    spacesigueapretada=False


        reloj1.tick(18)
        # auxiliar de la animacion
        t += 1
        if t > 1:
            t = 0



        pantalla.fill((200, 200, 200))
        player1.update(pantalla, vx, vy)
        pygame.display.update()

    pygame.quit()


main()


