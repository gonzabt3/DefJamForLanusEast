import pygame

pantalla = pygame.display.set_mode((750, 500))

#imagenes chabon parado
imagenParado1 = pygame.image.load("imagenes/fonte/parado/mov1s.png").convert_alpha()
imagenParado2 = pygame.image.load("imagenes/fonte/parado/mov2s.png").convert_alpha()
imagenParado3 = pygame.image.load("imagenes/fonte/parado/mov3s.png").convert_alpha()
imagenParado4 = pygame.image.load("imagenes/fonte/parado/mov4s.png").convert_alpha()
imagenParado5 = pygame.image.load("imagenes/fonte/parado/mov5s.png").convert_alpha()
imagenParado6 = pygame.image.load("imagenes/fonte/parado/mov6s.png").convert_alpha()
imagenParado7 = pygame.image.load("imagenes/fonte/parado/mov7s.png").convert_alpha()
imagenParado8 = pygame.image.load("imagenes/fonte/parado/mov8s.png").convert_alpha()
imagenParado9 = pygame.image.load("imagenes/fonte/parado/mov9s.png").convert_alpha()
imagenParado10 = pygame.image.load("imagenes/fonte/parado/mov10s.png").convert_alpha()
imagenParadoArray = [imagenParado1, imagenParado2, imagenParado3, imagenParado4, imagenParado5, imagenParado6,imagenParado7, imagenParado8, imagenParado9, imagenParado10]

# imagenes chabon movimietno
imagenMovimiento1 = pygame.image.load("imagenes/zub_zero/movimiento/movimiento1.png").convert_alpha()
imagenMovimiento2 = pygame.image.load("imagenes/zub_zero/movimiento/movimiento2.png").convert_alpha()
imagenMovimiento3 = pygame.image.load("imagenes/zub_zero/movimiento/movimiento3.png").convert_alpha()
imagenMovimiento4 = pygame.image.load("imagenes/zub_zero/movimiento/movimiento4.png").convert_alpha()
imagenMovimiento5 = pygame.image.load("imagenes/zub_zero/movimiento/movimiento5.png").convert_alpha()
imagenMovimiento6 = pygame.image.load("imagenes/zub_zero/movimiento/movimiento6.png").convert_alpha()
imagenMovimiento7 = pygame.image.load("imagenes/zub_zero/movimiento/movimiento7.png").convert_alpha()
imagenMovimiento8 = pygame.image.load("imagenes/zub_zero/movimiento/movimiento8.png").convert_alpha()
imagenMovimiento9 = pygame.image.load("imagenes/zub_zero/movimiento/movimiento9.png").convert_alpha()
imagenMovimientoArray = [imagenMovimiento1, imagenMovimiento2, imagenMovimiento3, imagenMovimiento4, imagenMovimiento5,imagenMovimiento6, imagenMovimiento7, imagenMovimiento8, imagenMovimiento9]

# imagenes chabon punio1
imagenPunio1 = pygame.image.load("imagenes/fonte/punio1/punio1s.png").convert_alpha()
imagenPunio2 = pygame.image.load("imagenes/fonte/punio1/punio2s.png").convert_alpha()
imagenPunio3 = pygame.image.load("imagenes/fonte/punio1/punio3s.png").convert_alpha()
imagenPunioArray = [imagenPunio1, imagenPunio2, imagenPunio3]

# imagenes chabon patada1
imagenPatada1 = pygame.image.load("imagenes/fonte/patada/patada1s.png").convert_alpha()
imagenPatada2 = pygame.image.load("imagenes/fonte/patada/patada2s.png").convert_alpha()
imagenPatada3 = pygame.image.load("imagenes/fonte/patada/patada3s.png").convert_alpha()
imagenPatada4 = pygame.image.load("imagenes/fonte/patada/patada4s.png").convert_alpha()
imagenPatadaArray = [imagenPatada1, imagenPatada2, imagenPatada3, imagenPatada4]

# imagenes chabon defensa1
imagenDefensa1 = pygame.image.load("imagenes/fonte/defensa/def1s.png").convert_alpha()
imagenDefensa2 = pygame.image.load("imagenes/fonte/defensa/def2s.png").convert_alpha()
imagenDefensa1Array = [imagenDefensa1, imagenDefensa2]

# texto
texto = pygame.image.load("imagenes/fonte/texto.png").convert_alpha()

# cabeza
cabeza = pygame.image.load("imagenes/fonte/cabeza.png").convert_alpha()