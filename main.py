import pygame

class Peleador(pygame.sprite.Sprite):
    def __init__(self,imagen1,imagen2,imagen3):
        #self.nombre=nombre
        #self.vida=vida
        #self.golpe=golpe
        self.imagen1=imagen1
        self.imagen2=imagen2
        self.imagen3=imagen3
        self.imagenes = [self.imagen1, self.imagen2,self.imagen3]
        self.imagenActual=0
        self.imagen=self.imagenes[self.imagenActual]
        self.rect=self.imagen.get_rect()
        self.rect.top,self.rect.left=(100,200)
        self.move=False

    def mover(self, vx, vy): #metodo que mueve al chabon
        self.rect.move_ip(vx, vy)

    def update(self, superficie,vx,vy,t):
        if(vx==0 and vy==0):
            self.move=False #me fijo si se esta moviendo
        else:
            self.move=True

        if(t>=0 and self.move==True):
            self.nextimage()


        self.mover(vx, vy)
        self.imagen=self.imagenes[self.imagenActual]
        superficie.blit(self.imagen, self.rect)


    def nextimage(self):#cambio de imagen:
        self.imagenActual += 1

        if self.imagenActual > (len(self.imagenes) - 1):  # si se fue de rango que lo ponga en 0
            self.imagenActual = 0



def main():


    pygame.init()
    pantalla = pygame.display.set_mode((600, 600))
    salir = False
    reloj1 = pygame.time.Clock()

    imagen1 = pygame.image.load("imagenes/cody/cody_pelea1.png").convert_alpha()
    imagen2  = pygame.image.load("imagenes/cody/cody_pelea2.png").convert_alpha()
    imagen3 = pygame.image.load("imagenes/cody/cody_pelea3.png").convert_alpha()

    player1 = Peleador(imagen1,imagen2,imagen3)
    vx, vy = 0, 0
    velocidad = 7
    t = 0
    leftsigueapretada, rightsigueapretada, upsigueapretada, downsigueapretada = False, False, False, False

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

        reloj1.tick(25)
        # auxiliar de la animacion
        t += 1
        if t > 1:
            t = 0



        pantalla.fill((200, 200, 200))
        player1.update(pantalla, vx, vy, t)
        pygame.display.update()

    pygame.quit()


main()


