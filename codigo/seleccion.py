import pygame


class Select(pygame.sprite.Sprite):
    def __init__(self, imagen):
        self.imagen = imagen
        self.rect = self.imagen.get_rect()
        self.rect.top, self.rect.left = (100, 200)



    def update(self, superficie,vx,vy):
        self.rect.move_ip(vx,vy)
        superficie.blit(self.imagen, self.rect)


def main():
    import pygame

    pygame.init()
    pantalla = pygame.display.set_mode((750,500))
    salir = False
    reloj1 = pygame.time.Clock()
    imagen1 = pygame.image.load("selectScreen/select1.png").convert_alpha()
    selectScreen = pygame.image.load("selectScreen/selectScreen.jpg").convert_alpha()

    select1 = Select(imagen1)
    vx, vy = 0, 0
    posicion1=1
    posicion2=3
    velocidad = 10
    leftsigueapretada, rightsigueapretada, upsigueapretada, downsigueapretada = False, False, False, False

    while salir != True:  # LOOP PRINCIPAL
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                salir = True
            k = pygame.key.get_pressed()

            if not mantiene_pulsado:
                if k[K_c]:
                    print "c"
                    self.posicion1 -= 1
                    self.rect1.move_ip(10, 10)
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

        reloj1.tick(20)
        pantalla.blit(selectScreen, (0, 0))

        select1.update(pantalla,vx, vy)
        pygame.display.update()

    pygame.quit()


main()