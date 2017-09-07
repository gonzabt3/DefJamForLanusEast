import pygame


class Peleador(pygame.sprite.Sprite):
    def __init__(self, imagenesQuieto, imagenesMovimiento, imagenesPunio1, imagenesPatada1, imagenesDefensa1, lifeBar,player):

        # atributos
        self.imagenesMovimiento = imagenesMovimiento
        self.imagenesQuieto = imagenesQuieto
        self.imagenesPunio1 = imagenesPunio1
        self.imagenesPatada1 = imagenesPatada1
        self.imagenesDefensa1 = imagenesDefensa1
        self.imagenActual = 0
        self.imagen = self.imagenesQuieto[self.imagenActual]
        self.rect = self.imagen.get_rect()
        if(player==1):
            self.rect.top, self.rect.left = (250, 100)
        if(player==2):
            self.rect.top, self.rect.left = (250, 550)
            for index,imagenesMovimientos in enumerate(imagenesMovimiento):
                self.imagenesMovimiento[index]=pygame.transform.flip(imagenesMovimientos,True,False)

            for index,imagenesQuietos in enumerate(imagenesQuieto):
                self.imagenesQuieto[index]=pygame.transform.flip(imagenesQuietos,True,False)

            for index,imagenesPunio1s in enumerate(imagenesPunio1):
                self.imagenesPunio1[index]=pygame.transform.flip(imagenesPunio1s,True,False)

            for index,imagenesPatada1s in enumerate(imagenesPatada1):
                self.imagenesPatada1[index]=pygame.transform.flip(imagenesPatada1s,True,False)

            for index,imagenesDefensa1s in enumerate(imagenesDefensa1):
                self.imagenesDefensa1[index]=pygame.transform.flip(imagenesDefensa1s,True,False)

        self.move = False
        self.estado = 0  # 0=inactivo,1=ataque,2=defensa,3=herido
        self.life = 100
        self.lifeBar = lifeBar




    def mover(self, vx, vy):  # metodo que mueve al chabon
        self.rect.move_ip(vx, vy)

    def update(self, superficie, vx, vy, fightMove, golpe, patada, defenseMove, defensa, lifeBar):
        if (fightMove == True):  # PREGUNTO SI hay un movimiento de pelea
            if (golpe == True):  # punio1
                self.punio1(superficie)
                self.lifeBar.actualizarBar(3)
            if (patada == True):  # patada1
                self.patada2(superficie)
        elif (defenseMove == True):
            if (defensa == True):
                self.defensa1(superficie)
        elif (vx == 0 and vy == 0):  # si la velocida esta en 0 no se mueve
            self.move = False  # me fijo si se esta moviendo
            self.estarQuieto(superficie)
        else:  # si la velocidad no esta en 0 se mueve
            self.move = True
            self.mover(vx, vy)
            if (vx > 0):
                self.moverse(superficie)
            if (vx < 0):
                self.moverseAtras(superficie)

    def estarQuieto(self, superficie):  # funcion que anima al personaj cuando esta quieto
        self.estado = 0;
        self.nextImage(self.imagenesQuieto)
        superficie.blit(self.imagenesQuieto[self.imagenActual], self.rect)

    def moverse(self, superficie):
        self.nextImage(self.imagenesMovimiento)
        superficie.blit(self.imagenesMovimiento[self.imagenActual], self.rect)

    def moverseAtras(self, superficie):
        self.previusImage(self.imagenesMovimiento)
        superficie.blit(self.imagenesMovimiento[self.imagenActual], self.rect)

    # def punio1(self,superficie):
    #         self.nextImage(self.imagenesPunio1)
    #         superficie.blit(self.imagenesPunio1[self.imagenActual],self.rect)

    def punio1(self, superficie):

        self.estado = 1
        for i in range(0, 3):
            # print i
            if self.imagenActual > len(self.imagenesPunio1):
                self.imagenActual = 0
            self.nextImageLimitado(self.imagenesPunio1)
            print self.imagenActual
            if self.imagenActual > len(self.imagenesPunio1):
                self.imagenActual - 1
            if self.imagenActual < len(self.imagenesPunio1):
                superficie.blit(self.imagenesPunio1[self.imagenActual], self.rect)

    def patada2(self, superficie):
        self.estado = 1
        for i in range(0, 3):
            # print i
            if self.imagenActual > len(self.imagenesPatada1):
                self.imagenActual = 0
            self.nextImageLimitado(self.imagenesPatada1)
            print self.imagenActual
            if self.imagenActual > len(self.imagenesPatada1):
                self.imagenActual - 1
            if self.imagenActual < len(self.imagenesPatada1):
                superficie.blit(self.imagenesPatada1[self.imagenActual], self.rect)

    def defensa1(self, superficie):
        self.estado = 2
        self.nextImageLimitado(self.imagenesDefensa1);
        if (self.imagenActual <= len(self.imagenesDefensa1) - 1):
            superficie.blit(self.imagenesDefensa1[self.imagenActual], self.rect)
        else:
            self.imagenActual = 0

    def nextImageLimitado(self, imagenesSec):

        if (self.imagenActual < len(imagenesSec) - 1):
            self.imagenActual += 1

    def nextImage(self, imagenesSec):  # cambio de imagen:
        self.imagenActual += 1
        if self.imagenActual > (len(imagenesSec) - 1):  # si se fue de rango que lo ponga en 0
            self.imagenActual = 0

    def previusImage(self, imagenesSec):
        # self.imagenActual=len(imagenesSec)
        self.imagenActual -= 1
        if self.imagenActual == 0:  # si se fue de rango que lo ponga en 0
            self.imagenActual = len(imagenesSec) - 1
