import pygame
from threading import Timer
class Peleador(pygame.sprite.Sprite):
    def __init__(self,imagenesQuieto,imagenesMovimiento,imagenesPunio1):

        self.imagenesMovimiento=imagenesMovimiento
        self.imagenesQuieto=imagenesQuieto
        self.imagenesPunio1=imagenesPunio1
        self.imagenActual=0
        self.imagen=self.imagenesQuieto[self.imagenActual]
        self.rect=self.imagen   .get_rect()
        self.rect.top,self.rect.left=(100,200)
        self.move=False

    def mover(self, vx, vy): #metodo que mueve al chabon
        self.rect.move_ip(vx, vy)

    def update(self, superficie,vx,vy,fightMove,spacesigueapretada):
        if(fightMove==True): #PREGUNTO SI hay un movimiento de pelea
            if (spacesigueapretada == True): #punio1
                self.punio1(superficie)
        elif(vx==0 and vy==0): #si la velocida esta en 0 no se mueve
            self.move=False #me fijo si se esta moviendo
            self.estarQuieto(superficie)
        else: #si la velocidad no esta en 0 se mueve
                self.move = True
                self.mover(vx, vy)
                self.moverse(superficie)

    def estarQuieto(self,superficie): #funcion que anima al personaj cuando esta quieto
            self.nextImage(self.imagenesQuieto)
            superficie.blit(self.imagenesQuieto[self.imagenActual], self.rect)

    def moverse(self,superficie):
            self.nextImage(self.imagenesMovimiento)
            superficie.blit(self.imagenesMovimiento[self.imagenActual],self.rect)
    
    def punio1(self,superficie):
            self.nextImage(self.imagenesPunio1)
            superficie.blit(self.imagenesPunio1[self.imagenActual],self.rect)

    def nextImage(self,imagenesSec):#cambio de imagen:
        self.imagenActual += 1

        if self.imagenActual > (len(imagenesSec) - 1):  # si se fue de rango que lo ponga en 0
            self.imagenActual = 0

    def previusImage(self,imagenesSec):
        self.imagenActual=len(imagenesSec)
        self.imagenActual-=1
        if self.imagenActual>0 :  # si se fue de rango que lo ponga en 0
            self.imagenActual = 0

def main():


    pygame.init()
    pantalla = pygame.display.set_mode((600, 600))
    salir = False
    reloj1 = pygame.time.Clock()

    #imagenes chabon parado
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

    #imagenes chabon movimietno
    imagenMovimiento1 = pygame.image.load("imagenes/zub_zero/movimiento/movimiento1.png").convert_alpha()
    imagenMovimiento2 = pygame.image.load("imagenes/zub_zero/movimiento/movimiento2.png").convert_alpha()
    imagenMovimiento3 = pygame.image.load("imagenes/zub_zero/movimiento/movimiento3.png").convert_alpha()
    imagenMovimiento4 = pygame.image.load("imagenes/zub_zero/movimiento/movimiento4.png").convert_alpha()
    imagenMovimiento5 = pygame.image.load("imagenes/zub_zero/movimiento/movimiento5.png").convert_alpha()
    imagenMovimiento6 = pygame.image.load("imagenes/zub_zero/movimiento/movimiento6.png").convert_alpha()
    imagenMovimiento7 = pygame.image.load("imagenes/zub_zero/movimiento/movimiento7.png").convert_alpha()
    imagenMovimiento8 = pygame.image.load("imagenes/zub_zero/movimiento/movimiento8.png").convert_alpha()
    imagenMovimiento9 = pygame.image.load("imagenes/zub_zero/movimiento/movimiento9.png").convert_alpha()
    imagenMovimientoArray =[imagenMovimiento1,imagenMovimiento2,imagenMovimiento3,imagenMovimiento4,imagenMovimiento5,imagenMovimiento6,imagenMovimiento7,imagenMovimiento8,imagenMovimiento9]

    #imagenes chabon punio1
    imagenPunio1 = pygame.image.load("imagenes/zub_zero/punio1/punio1.png").convert_alpha()
    imagenPunio2= pygame.image.load("imagenes/zub_zero/punio1/punio2.png").convert_alpha()
    imagenPunio3 = pygame.image.load("imagenes/zub_zero/punio1/punio3.png").convert_alpha()
    imagenPunioArray=[imagenPunio1,imagenPunio2,imagenPunio3]

    player1 = Peleador(imagenParadoArray,imagenMovimientoArray,imagenPunioArray)
    vx, vy = 0, 0
    velocidad = 7
    t = 0
    leftsigueapretada, rightsigueapretada, upsigueapretada, downsigueapretada,spacesigueapretada = False, False, False, False,False
    fightMove=False
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
                    fightMove=True

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
                    fightMove = False

        reloj1.tick(18)
        # auxiliar de la animacion
      #  t += 1
       # if t > 1:
        #    t = 0



        pantalla.fill((200, 200, 200))
        player1.update(pantalla, vx, vy,fightMove,spacesigueapretada)
        pygame.display.update()

    pygame.quit()


main()


