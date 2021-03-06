import pygame

pantalla = pygame.display.set_mode((750, 500))
nombre="pablo"
#imagenes chabon parado
imagenParado1 = pygame.image.load("imagenes/pablo/parado/mov1s.png").convert_alpha()
imagenParado2 = pygame.image.load("imagenes/pablo/parado/mov2s.png").convert_alpha()
imagenParado3 = pygame.image.load("imagenes/pablo/parado/mov3s.png").convert_alpha()
imagenParado4 = pygame.image.load("imagenes/pablo/parado/mov4s.png").convert_alpha()
imagenParado5 = pygame.image.load("imagenes/pablo/parado/mov5s.png").convert_alpha()
imagenParado6 = pygame.image.load("imagenes/pablo/parado/mov6s.png").convert_alpha()
imagenParado7 = pygame.image.load("imagenes/pablo/parado/mov7s.png").convert_alpha()
imagenParado8 = pygame.image.load("imagenes/pablo/parado/mov8s.png").convert_alpha()
imagenParado9 = pygame.image.load("imagenes/pablo/parado/mov9s.png").convert_alpha()
imagenParado10 = pygame.image.load("imagenes/pablo/parado/mov10s.png").convert_alpha()
imagenParadoArray = [imagenParado1, imagenParado2, imagenParado3, imagenParado4, imagenParado5, imagenParado6,imagenParado7, imagenParado8, imagenParado9, imagenParado10]

# imagenes chabon movimietno
imagenMovimiento1 = pygame.image.load("imagenes/pablo/movimiento/mov1.png").convert_alpha()
imagenMovimiento2 = pygame.image.load("imagenes/pablo/movimiento/mov2.png").convert_alpha()
imagenMovimiento3 = pygame.image.load("imagenes/pablo/movimiento/mov3.png").convert_alpha()
imagenMovimiento4 = pygame.image.load("imagenes/pablo/movimiento/mov4.png").convert_alpha()
imagenMovimiento5 = pygame.image.load("imagenes/pablo/movimiento/mov5.png").convert_alpha()
imagenMovimiento6 = pygame.image.load("imagenes/pablo/movimiento/mov6.png").convert_alpha()
imagenMovimiento7 = pygame.image.load("imagenes/pablo/movimiento/mov7.png").convert_alpha()
imagenMovimiento8 = pygame.image.load("imagenes/pablo/movimiento/mov8.png").convert_alpha()
imagenMovimiento9 = pygame.image.load("imagenes/pablo/movimiento/mov9.png").convert_alpha()
imagenMovimientoArray = [imagenMovimiento1, imagenMovimiento2, imagenMovimiento3, imagenMovimiento4, imagenMovimiento5,imagenMovimiento6, imagenMovimiento7, imagenMovimiento8, imagenMovimiento9]

# imagenes chabon punio1
imagenPunio1 = pygame.image.load("imagenes/pablo/punio1/punio1s.png").convert_alpha()
imagenPunio2 = pygame.image.load("imagenes/pablo/punio1/punio2s.png").convert_alpha()
imagenPunio3 = pygame.image.load("imagenes/pablo/punio1/punio3s.png").convert_alpha()
imagenPunioArray = [imagenPunio1, imagenPunio2, imagenPunio3]

# imagenes chabon patada1
imagenPatada1 = pygame.image.load("imagenes/pablo/patada/patada1s.png").convert_alpha()
imagenPatada2 = pygame.image.load("imagenes/pablo/patada/patada2s.png").convert_alpha()
imagenPatada3 = pygame.image.load("imagenes/pablo/patada/patada3s.png").convert_alpha()
imagenPatada4 = pygame.image.load("imagenes/pablo/patada/patada4s.png").convert_alpha()
imagenPatadaArray = [imagenPatada1, imagenPatada2, imagenPatada3, imagenPatada4]

# imagenes chabon defensa1
imagenDefensa1 = pygame.image.load("imagenes/pablo/defensa/def1s.png").convert_alpha()
imagenDefensa2 = pygame.image.load("imagenes/pablo/defensa/def2s.png").convert_alpha()
imagenDefensa1Array = [imagenDefensa1, imagenDefensa2]

#imagene chabon herido
herido1=pygame.image.load("imagenes/pablo/herido/herido1.png").convert_alpha()
herido2=pygame.image.load("imagenes/pablo/herido/herido2.png").convert_alpha()
imagenHeridoArray=[herido1,herido2]

#imagenes chabon muerto
muerto1=pygame.image.load("imagenes/pablo/muerto/muerto1.png").convert_alpha()
muerto2=pygame.image.load("imagenes/pablo/muerto/muerto2.png").convert_alpha()
muerto3=pygame.image.load("imagenes/pablo/muerto/muerto3.png").convert_alpha()
muerto4=pygame.image.load("imagenes/pablo/muerto/muerto4.png").convert_alpha()
imagenMuertoArray=[muerto1,muerto2,muerto3,muerto4]

#imagenes chabon muerto sin cabeza
muertoScabe1=pygame.image.load("imagenes/pablo/muertoSinCabeza/sinCabeza1.png").convert_alpha()
muertoScabe2=pygame.image.load("imagenes/pablo/muertoSinCabeza/sinCabeza2.png").convert_alpha()
muertoScabe3=pygame.image.load("imagenes/pablo/muertoSinCabeza/sinCabeza3.png").convert_alpha()
muertoScabe4=pygame.image.load("imagenes/pablo/muertoSinCabeza/sinCabeza4.png").convert_alpha()


imagenMuertoSinCabezaArray=[muertoScabe1,muertoScabe2,muertoScabe3,muertoScabe4]

#imagenes chabon festejo
festejo1=pygame.image.load('imagenes/pablo/festejo/fes1.png').convert_alpha()
festejo2=pygame.image.load('imagenes/pablo/festejo/fes2.png').convert_alpha()
festejo3=pygame.image.load('imagenes/pablo/festejo/fes3.png').convert_alpha()
festejo4=pygame.image.load('imagenes/pablo/festejo/fes4.png').convert_alpha()
festejo5=pygame.image.load('imagenes/pablo/festejo/fes5.png').convert_alpha()
festejo6=pygame.image.load('imagenes/pablo/festejo/fes6.png').convert_alpha()
festejo7=pygame.image.load('imagenes/pablo/festejo/fes7.png').convert_alpha()
festejo8=pygame.image.load('imagenes/pablo/festejo/fes8.png').convert_alpha()
festejo9=pygame.image.load('imagenes/pablo/festejo/fes9.png').convert_alpha()
festejo10=pygame.image.load('imagenes/pablo/festejo/fes10.png').convert_alpha()

imagenFestejo=[festejo1,festejo2,festejo3,festejo4,festejo5,festejo6,festejo7,festejo8,festejo9,festejo10]

# texto
texto = pygame.image.load("imagenes/pablo/texto.png").convert_alpha()

# cabeza
cabeza = pygame.image.load("imagenes/pablo/cabeza.png").convert_alpha()