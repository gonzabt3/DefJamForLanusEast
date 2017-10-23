import pygame

pantalla = pygame.display.set_mode((750, 500))
nombre="enzo"
#imagenes chabon parado
imagenParado1 = pygame.image.load("imagenes/enzo/parado/mov1.png").convert_alpha()
imagenParado2 = pygame.image.load("imagenes/enzo/parado/mov2.png").convert_alpha()
imagenParado3 = pygame.image.load("imagenes/enzo/parado/mov3.png").convert_alpha()
imagenParado4 = pygame.image.load("imagenes/enzo/parado/mov4.png").convert_alpha()
imagenParado5 = pygame.image.load("imagenes/enzo/parado/mov5.png").convert_alpha()
imagenParado6 = pygame.image.load("imagenes/enzo/parado/mov6.png").convert_alpha()

imagenParadoArray = [imagenParado1, imagenParado2, imagenParado3, imagenParado4, imagenParado5, imagenParado6]

# imagenes chabon movimietno
imagenMovimiento1 = pygame.image.load("imagenes/enzo/movimiento/mov1.png").convert_alpha()
imagenMovimiento2 = pygame.image.load("imagenes/enzo/movimiento/mov2.png").convert_alpha()
imagenMovimiento3 = pygame.image.load("imagenes/enzo/movimiento/mov3.png").convert_alpha()
imagenMovimiento4 = pygame.image.load("imagenes/enzo/movimiento/mov4.png").convert_alpha()
imagenMovimiento5 = pygame.image.load("imagenes/enzo/movimiento/mov5.png").convert_alpha()
imagenMovimiento6 = pygame.image.load("imagenes/enzo/movimiento/mov6.png").convert_alpha()
imagenMovimiento7 = pygame.image.load("imagenes/enzo/movimiento/mov7.png").convert_alpha()
imagenMovimiento8 = pygame.image.load("imagenes/enzo/movimiento/mov8.png").convert_alpha()
imagenMovimiento9 = pygame.image.load("imagenes/enzo/movimiento/mov9.png").convert_alpha()
imagenMovimientoArray = [imagenMovimiento1, imagenMovimiento2, imagenMovimiento3, imagenMovimiento4, imagenMovimiento5,imagenMovimiento6, imagenMovimiento7, imagenMovimiento8, imagenMovimiento9]

# imagenes chabon punio1
imagenPunio1 = pygame.image.load("imagenes/enzo/punio1/punio1s.png").convert_alpha()
imagenPunio2 = pygame.image.load("imagenes/enzo/punio1/punio2s.png").convert_alpha()
imagenPunio3 = pygame.image.load("imagenes/enzo/punio1/punio3s.png").convert_alpha()
imagenPunioArray = [imagenPunio1, imagenPunio2, imagenPunio3]

# imagenes chabon patada1
imagenPatada1 = pygame.image.load("imagenes/enzo/patada/patada1s.png").convert_alpha()
imagenPatada2 = pygame.image.load("imagenes/enzo/patada/patada2s.png").convert_alpha()
imagenPatada3 = pygame.image.load("imagenes/enzo/patada/patada3s.png").convert_alpha()
imagenPatada4 = pygame.image.load("imagenes/enzo/patada/patada4s.png").convert_alpha()
imagenPatadaArray = [imagenPatada1, imagenPatada2, imagenPatada3, imagenPatada4]

# imagenes chabon defensa1
imagenDefensa1 = pygame.image.load("imagenes/enzo/defensa/def1s.png").convert_alpha()
imagenDefensa2 = pygame.image.load("imagenes/enzo/defensa/def2s.png").convert_alpha()
imagenDefensa1Array = [imagenDefensa1, imagenDefensa2]

#imagene chabon herido
herido1=pygame.image.load("imagenes/enzo/herido/herido1.png").convert_alpha()
herido2=pygame.image.load("imagenes/enzo/herido/herido2.png").convert_alpha()
imagenHeridoArray=[herido1,herido2]

#imagenes chabon muerto
muerto1=pygame.image.load("imagenes/enzo/muerto/muerto1.png").convert_alpha()
muerto2=pygame.image.load("imagenes/enzo/muerto/muerto2.png").convert_alpha()
muerto3=pygame.image.load("imagenes/enzo/muerto/muerto3.png").convert_alpha()
muerto4=pygame.image.load("imagenes/enzo/muerto/muerto4.png").convert_alpha()
muerto5=pygame.image.load("imagenes/enzo/muerto/muerto5.png").convert_alpha()

imagenMuertoArray=[muerto1,muerto2,muerto3,muerto4,muerto5]

#imagenes chabon muerto sin cabeza
muertoScabe1=pygame.image.load("imagenes/enzo/muertoSinCabeza/sinCabeza1.png").convert_alpha()
muertoScabe2=pygame.image.load("imagenes/enzo/muertoSinCabeza/sinCabeza2.png").convert_alpha()
muertoScabe3=pygame.image.load("imagenes/enzo/muertoSinCabeza/sinCabeza3.png").convert_alpha()
muertoScabe4=pygame.image.load("imagenes/enzo/muertoSinCabeza/sinCabeza4.png").convert_alpha()
muertoScabe5=pygame.image.load("imagenes/enzo/muertoSinCabeza/sinCabeza5.png").convert_alpha()

imagenMuertoSinCabezaArray=[muertoScabe1,muertoScabe2,muertoScabe3,muertoScabe4,muertoScabe5]


# texto
texto = pygame.image.load("imagenes/enzo/texto.png").convert_alpha()

# cabeza
cabeza = pygame.image.load("imagenes/enzo/cabeza.png").convert_alpha()