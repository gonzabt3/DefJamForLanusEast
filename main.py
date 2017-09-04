import pygame
from threading import Timer

class Fondo(pygame.sprite.Sprite):
    def __init__(self):
        self.imagen=pygame.image.load("imagenes/fondo/enzoHause.gif").convert_alpha()
        self.rect=self.imagen.get_rect()

    def update(self,pantalla):
        pantalla.blit(self.imagen,self.rect)

class LifeBar(pygame.sprite.Sprite):
    def __init__(self):
        self.marco=pygame.image.load("imagenes/lifebar/life_bar_marco.png").convert_alpha()
        self.relleno=pygame.image.load("imagenes/lifebar/life_bar_relleno.png").convert_alpha()
        self.pixelesBarra=228
        self.rect = self.marco.get_rect()
        self.rect.top, self.rect.left = (10, 10)
        self.rectRelleno=self.relleno.get_rect()
        self.rectRelleno.top,self.rectRelleno.left=(54,76)

    def update(self,pantalla):
        pantalla.blit(self.marco, self.rect)
        pantalla.blit(self.relleno, self.rectRelleno)

    def actualizarBar(self,damage):
        damagePixeles = (damage * self.pixelesBarra) / 100
        self.pixelesBarra = self.pixelesBarra - damagePixeles
        self.relleno = pygame.transform.smoothscale(self.relleno, (self.pixelesBarra, 5))

class Peleador(pygame.sprite.Sprite):
    def __init__(self,imagenesQuieto,imagenesMovimiento,imagenesPunio1,imagenesPatada1,imagenesDefensa1,lifeBar):

        #atributos
        self.imagenesMovimiento=imagenesMovimiento
        self.imagenesQuieto=imagenesQuieto
        self.imagenesPunio1=imagenesPunio1
        self.imagenesPatada1=imagenesPatada1
        self.imagenesDefensa1=imagenesDefensa1
        self.imagenActual=0
        self.imagen=self.imagenesQuieto[self.imagenActual]
        self.rect=self.imagen.get_rect()
        self.rect.top,self.rect.left=(250,100)
        self.move=False
        self.estado=0 # 0=inactivo,1=ataque,2=defensa,3=herido
        self.life=100
        self.lifeBar=lifeBar

    def mover(self, vx, vy): #metodo que mueve al chabon
        self.rect.move_ip(vx, vy)

    def update(self, superficie,vx,vy,fightMove,q_apretada,w_apretada,defenseMove,e_apretada,lifeBar1):
        if(fightMove==True): #PREGUNTO SI hay un movimiento de pelea
            if (q_apretada == True): #punio1
                self.punio1(superficie)
                self.lifeBar.actualizarBar(3)
            if (w_apretada == True): #patada1
                self.patada2(superficie)
        elif (defenseMove == True):
            if (e_apretada==True):
                self.defensa1(superficie)
        elif(vx==0 and vy==0): #si la velocida esta en 0 no se mueve
            self.move=False #me fijo si se esta moviendo
            self.estarQuieto(superficie)
        else: #si la velocidad no esta en 0 se mueve
                self.move = True
                self.mover(vx, vy)
                if(vx>0):
                    self.moverse(superficie)
                if(vx<0):
                    self.moverseAtras(superficie)

    def estarQuieto(self,superficie): #funcion que anima al personaj cuando esta quieto
            self.estado=0;
            self.nextImage(self.imagenesQuieto)
            superficie.blit(self.imagenesQuieto[self.imagenActual], self.rect)

    def moverse(self,superficie):
            self.nextImage(self.imagenesMovimiento)
            superficie.blit(self.imagenesMovimiento[self.imagenActual],self.rect)

    def moverseAtras(self,superficie):
            self.previusImage(self.imagenesMovimiento)
            superficie.blit(self.imagenesMovimiento[self.imagenActual],self.rect)


    # def punio1(self,superficie):
    #         self.nextImage(self.imagenesPunio1)
    #         superficie.blit(self.imagenesPunio1[self.imagenActual],self.rect)

    def punio1(self,superficie):

        self.estado=1
        for i in range(0, 3):
            # print i
            if self.imagenActual>len(self.imagenesPunio1):
                self.imagenActual=0
            self.nextImageLimitado(self.imagenesPunio1)
            print self.imagenActual
            if self.imagenActual>len(self.imagenesPunio1):
                self.imagenActual-1
            if self.imagenActual < len(self.imagenesPunio1):
                superficie.blit(self.imagenesPunio1[self.imagenActual],self.rect)

    def patada2(self,superficie):
        self.estado=1
        for i in range(0, 3):
            # print i
            if self.imagenActual>len(self.imagenesPatada1):
                self.imagenActual=0
            self.nextImageLimitado(self.imagenesPatada1)
            print self.imagenActual
            if self.imagenActual>len(self.imagenesPatada1):
                self.imagenActual-1
            if self.imagenActual < len(self.imagenesPatada1):
                superficie.blit(self.imagenesPatada1[self.imagenActual],self.rect)
        
    def defensa1(self,superficie):
        self.estado=2
        self.nextImageLimitado(self.imagenesDefensa1);
        if(self.imagenActual<=len(self.imagenesDefensa1)-1):
            superficie.blit(self.imagenesDefensa1[self.imagenActual],self.rect)
        else:
            self.imagenActual=0

    def nextImageLimitado(self,imagenesSec):

        if(self.imagenActual<len(imagenesSec)-1):
            self.imagenActual+=1

    def nextImage(self,imagenesSec):#cambio de imagen:
        self.imagenActual += 1
        if self.imagenActual > (len(imagenesSec) - 1):  # si se fue de rango que lo ponga en 0
            self.imagenActual = 0

    def previusImage(self,imagenesSec):
        # self.imagenActual=len(imagenesSec)
        self.imagenActual-=1
        if self.imagenActual==0:  # si se fue de rango que lo ponga en 0
            self.imagenActual = len(imagenesSec)-1

def main():

    pygame.init()
    pantalla = pygame.display.set_mode((600, 500))
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

    #imagenes chabon patada1
    imagenPatada1 = pygame.image.load("imagenes/zub_zero/patada/patada1.png").convert_alpha()
    imagenPatada2 = pygame.image.load("imagenes/zub_zero/patada/patada2.png").convert_alpha()
    imagenPatada3 = pygame.image.load("imagenes/zub_zero/patada/patada3.png").convert_alpha()
    imagenPatada4 = pygame.image.load("imagenes/zub_zero/patada/patada4.png").convert_alpha()
    imagenPatadaArray = [imagenPatada1, imagenPatada2, imagenPatada3, imagenPatada4]

    #imagenes chabon defensa1
    imagenDefensa1 = pygame.image.load("imagenes/zub_zero/defensa/defensa1.png").convert_alpha()
    imagenDefensa2 = pygame.image.load("imagenes/zub_zero/defensa/defensa2.png").convert_alpha()
    imagenDefensa1Array =[imagenDefensa1,imagenDefensa2]

    lifeBar1 = LifeBar()
    player1 = Peleador(imagenParadoArray,imagenMovimientoArray,imagenPunioArray,imagenPatadaArray,imagenDefensa1Array,lifeBar1)
    fondo1=Fondo()
    vx, vy = 0, 0
    velocidad = 7
    t = 0
    leftsigueapretada, rightsigueapretada, upsigueapretada, downsigueapretada,q_apretada,w_apretada,e_apretada = False, False, False, False,False,False,False
    fightMove=False
    defenseMove=False
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
                # if event.key == pygame.K_UP:
                #     upsigueapretada = True
                #     vy = -velocidad
                # if event.key == pygame.K_DOWN:
                #     downsigueapretada = True
                #     vy = velocidad
                if event.key == pygame.K_q:
                    q_apretada = True
                    fightMove=True
                if event.key == pygame.K_w:
                    w_apretada = True
                    fightMove=True
                if event.key == pygame.K_e:
                    e_apretada = True
                    defenseMove=True

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
                # if event.key == pygame.K_UP:
                #     upsigueapretada = False
                #     if downsigueapretada:
                #         vy = velocidad
                #     else:
                #         vy = -0
                # if event.key == pygame.K_DOWN:
                #     downsigueapretada = False
                #     if upsigueapretada:
                #         vy = -velocidad
                #     else:
                #         vy = 0
                if event.key == pygame.K_q:
                    q_apretada=False
                    fightMove = False
                if event.key == pygame.K_w:
                    w_apretada=False
                    fightMove=False
                if event.key == pygame.K_e:
                    e_apretada=False
                    defenseMove=False

        reloj1.tick(16)
        #auxiliar de la animacion
        #t += 1
        #if t > 1:
        #t = 0

        pantalla.fill((200, 200, 200))
        fondo1.update(pantalla)
        lifeBar1.update(pantalla)
        player1.update(pantalla, vx, vy,fightMove,q_apretada,w_apretada,defenseMove,e_apretada,lifeBar1)
        pygame.display.update()

    pygame.quit()

main()


