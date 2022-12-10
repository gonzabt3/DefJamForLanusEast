import pygame

pygame.init()
#sonidos
punio1Sonido=pygame.mixer.Sound("sonidos/punio.wav")
punioBloqueoSonido=pygame.mixer.Sound("sonidos/puniob.wav")
patadaSonido=pygame.mixer.Sound("sonidos/patada.wav")
patadaBloqueoSonido=pygame.mixer.Sound("sonidos/patadab.wav")

fuente=pygame.font.Font("fuentesMK/mk2.ttf",50)


class Peleador(pygame.sprite.Sprite):
    def __init__(self,nombre,imagenesQuieto, imagenesMovimiento, imagenesPunio1, imagenesPatada1, imagenesDefensa1,imagenesHerido,imagenesMuerto,imagenesSinCabeza,lifeBar,player,imagenesFestejo):

        # atributos

        self.nombre=nombre
        self.banderaPelea=True #bandera que marca si la pelea esta on o si ya hay un ganador
        self.imagenesMovimiento = imagenesMovimiento
        self.imagenesQuieto = imagenesQuieto
        self.imagenesPunio1 = imagenesPunio1
        self.imagenesPatada1 = imagenesPatada1
        self.imagenesDefensa1 = imagenesDefensa1
        self.imagenesHerido = imagenesHerido
        self.imagenesMuerto = imagenesMuerto
        self.imagenesSinCabeza = imagenesSinCabeza
        self.imagenesFestejo = imagenesFestejo
        self.imagenActual = 0
        self.imagen = self.imagenesQuieto[self.imagenActual]
        self.rect = self.imagen.get_rect()
        self.rect.inflate_ip(-20,-20)
        self.contadorMuerto=0 #esta variable la pongo para contar el tiempo para mostrar la fatality antes que terminar la pelea,VILLERIADA

        self.player=player
        if(player==1):
            self.x=100
            self.y=250
            self.rect.top,self.rect.left = (self.y,self.x) #posicion en la pantalla

            # seteo rects golpes
            self.rectPunio = pygame.Rect((210, 279), (10, 10))
            self.rectPatada =pygame.Rect((230,318),(10,10))

        #doy vuelta imagenes si es el player2
        if(player==2):
            self.x = 550
            self.y = 250
            self.rect.top, self.rect.left = ( self.y,self.x)  # posicion en la pantalla
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

            for index,imagenesHeridos in enumerate(imagenesHerido):
                self.imagenesHerido[index]=pygame.transform.flip(imagenesHeridos,True,False)

            #seteo rects golpes
            self.rectPunio = pygame.Rect((552, 276), (10, 10))
            self.rectPatada = pygame.Rect((552, 285), (10, 10))

        self.move = False
        self.estado = 0  # 0=inactivo,1=ataque,2=defensa,3=herido,4=muerto,5=ganador,6=fatality,7=pelea terminada
        self.life = 100
        self.lifeBar = lifeBar

        #imagenes sangre universal para todos los fighters
        blood1 = pygame.image.load("imagenes/sangradoCabeza/bloodCabeza1.png").convert_alpha()
        blood2 = pygame.image.load("imagenes/sangradoCabeza/bloodCabeza2.png").convert_alpha()
        blood3 = pygame.image.load("imagenes/sangradoCabeza/bloodCabeza3.png").convert_alpha()
        blood4 = pygame.image.load("imagenes/sangradoCabeza/bloodCabeza4.png").convert_alpha()
        blood5 = pygame.image.load("imagenes/sangradoCabeza/bloodCabeza5.png").convert_alpha()
        blood6 = pygame.image.load("imagenes/sangradoCabeza/bloodCabeza6.png").convert_alpha()

        bloodCabezaArray = [blood1,blood2,blood3,blood4,blood5,blood6]
        self.sangreCabeza=bloodCabezaArray
        self.sangreCabezaImagenActual=0

    def mover(self, vx, vy):  # metodo que mueve al chabon
        if(self.x+vx>=2 and self.x+vx<=634): #el if es para que no se valla del rango
            # muevo los recs de lugar
            self.rect.move_ip(vx,vy)
            self.rectPunio.move_ip(vx,vy)
            self.rectPatada.move_ip(vx,vy)

            #actulizo localizacion
            self.x = self.rect.x
            self.y = self.rect.y

    def action(self):


    def update(self, superficie, vx, vy, fightMove, golpe, patada, defenseMove, defensa, lifeBar,oponente):
        #imprime los estados de los pj
        # print self.nombre, self.estado

        if(self.estado!=5):#CREO QUE ESTA AL PEDO ,CREO
            if(self.estado!=4):
                if(self.estado!=6):
                    # print self.nombre,"verifiado"
                    self.verificarVida(superficie,oponente)

            if( self.estado !=6):
                if(self.estado !=4  ):
                    if (fightMove == True):  # PREGUNTO SI hay un movimiento de pelea
                        if (golpe == True):  # punio1
                            self.estado = 1
                            self.punio1(superficie)

                            if(self.rectPunio.colliderect(oponente.rect) and oponente.estado!=2 and oponente.estado!=4):
                                oponente.lifeBar.actualizarBar(3)
                                punio1Sonido.play()
                                self.cambiarEstado(oponente,3)
                                oponente.life=oponente.life-3

                            if (self.rectPunio.colliderect(oponente.rect) and oponente.estado == 2):
                                oponente.lifeBar.actualizarBar(1)
                                punioBloqueoSonido.play()
                                oponente.life = oponente.life - 1
                            if (self.rectPunio.colliderect(oponente.rect) and oponente.estado ==4):
                                # print "entro"
                                self.cambiarEstado(oponente,6)
                                oponente.banderaPelea=False
                                self.banderaPelea=False

                        if (patada == True):  # patada1
                            self.patada2(superficie)
                            if (self.rectPatada.colliderect(oponente.rect) and oponente.estado != 2 and oponente.estado!=4):
                                oponente.lifeBar.actualizarBar(5)
                                patadaSonido.play()
                                self.cambiarEstado(oponente,3)
                                oponente.life = oponente.life - 5
                            if (self.rectPatada.colliderect(oponente.rect) and oponente.estado == 2):
                                oponente.lifeBar.actualizarBar(2)
                                patadaBloqueoSonido.play()
                                oponente.life = oponente.life - 2
                            if (self.rectPatada.colliderect(oponente.rect) and oponente.estado == 4):
                                self.cambiarEstado(oponente,6)
                    elif (defenseMove == True):
                        if (defensa == True):
                            self.defensa1(superficie)
                    elif(self.estado==3 and self.estado!=6):
                        self.herido(superficie)
                        self.estado=0

                    elif (vx == 0 and vy == 0 ):  # si la velocida esta en 0 no se mueve
                        self.move = False  # me fijo si se esta moviendo
                        self.estarQuieto(superficie)
                        # pygame.draw.rect(superficie,(255,0,0),self.rect) # line para pintar recs
                    else:  # si la velocidad no esta en 0 se mueve
                        self.move = True
                        self.mover(vx, vy)
                        #direccion al caminar
                        if(self.player==1):
                            if (vx > 0):
                                self.moverse(superficie)
                            if (vx < 0):
                                self.moverseAtras(superficie)
                        if (self.player ==2):
                            if (vx < 0):
                                self.moverse(superficie)
                            if (vx > 0):
                                self.moverseAtras(superficie)
                elif(self.estado==4):
                    self.muerto(superficie)
            if(self.estado==6):
                self.muertoSinCabeza(superficie)
                self.fatality(superficie)
        if(self.estado==5):
            oponente.estado=6
            self.festejo(superficie)
            self.cartelGanaro(superficie)
        # print self.nombre,"estado: ",self.estado


    def estarQuieto(self, superficie):  # funcion que anima al personaj cuando esta quieto
        self.estado = 0;
        self.nextImage(self.imagenesQuieto)
        superficie.blit(self.imagenesQuieto[self.imagenActual], self.rect)

    def herido(self,superficie):
        superficie.blit(self.imagenesHerido[1], self.rect)

    def muerto(self,superficie):
        self.nextImage(self.imagenesMuerto)
        superficie.blit(self.imagenesMuerto[self.imagenActual], self.rect)

    def muertoSinCabeza(self,superfice):
        self.nextImage(self.imagenesSinCabeza)
        superfice.blit(self.imagenesSinCabeza[self.imagenActual],self.rect)

    def fatality(self,superficie):
        # print "fatality"
        self.sangreCabezaImagenActual+=1
        if self.sangreCabezaImagenActual > (len(self.sangreCabeza) - 1):  # si se fue de rango que lo ponga en 0
            self.sangreCabezaImagenActual = 0
        superficie.blit(self.sangreCabeza[self.sangreCabezaImagenActual],(self.x,self.y-30))

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


        for i in range(0, 3):
            # print i
            if self.imagenActual > len(self.imagenesPunio1):
                self.imagenActual = 0
            self.nextImageLimitado(self.imagenesPunio1)
            # print self.imagenActual
            if self.imagenActual > len(self.imagenesPunio1):
                self.imagenActual - 1
            if self.imagenActual < len(self.imagenesPunio1):
                superficie.blit(self.imagenesPunio1[self.imagenActual], self.rect)
                # pygame.draw.rect(superficie,(255,0,0),self.rectPunio) # line para pintar recs

    def patada2(self, superficie):
        self.estado = 1
        for i in range(0, 3):
            # print i
            if self.imagenActual > len(self.imagenesPatada1):
                self.imagenActual = 0
            self.nextImageLimitado(self.imagenesPatada1)
            #print self.imagenActual
            if self.imagenActual > len(self.imagenesPatada1):
                self.imagenActual - 1
            if self.imagenActual < len(self.imagenesPatada1):
                superficie.blit(self.imagenesPatada1[self.imagenActual], self.rect)
                # pygame.draw.rect(superficie, (255, 0, 0), self.rectPatada)  # line para pintar recs

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

    def verificarVida(self,superficie,oponente):
        if(self.life<=-100):
            self.estado=4
            oponente.estado=5


    def cambiarEstado(self,oponente,estado):
        if(oponente.estado!=4 or oponente.estado!=6):
            oponente.estado=estado
        if(oponente.estado==4 and estado==6):
            oponente.estado=6



    def festejo(self,superfice):
        self.nextImage(self.imagenesFestejo)
        superfice.blit(self.imagenesFestejo[self.imagenActual],self.rect)


    def cartelGanaro(self,superficie):
        if(self.player==1):
            label = fuente.render("GANADOR PLAYER 1", 1, (255, 0, 0))
            superficie.blit(label, (100, 100))
        elif(self.player==2):
            label = fuente.render("GANADOR PLAYER 2", 1, (255, 0, 0))
            superficie.blit(label, (100, 100))