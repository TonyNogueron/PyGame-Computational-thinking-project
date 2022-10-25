#Proyecto Final en PyGame - Antonio y Camila 
from pygame import *
import sys, random
import sys, time
from PIL import Image

def cargar_animacion(nombre,extension, n):
    images = []
    for i in range(1,n+1):
        name = nombre+str(i)+extension
        images.append(image.load(name))
    return images

def mostrar_animacion(images, freq, x, y):
    frame = int(time.time()*freq) % len(images)
    screen.blit(images[frame],(x, y))

escena = 0
score = 0

mapa1 = image.load("mapas/mapa1.png")
mapa1 = transform.scale(mapa1, (1280,720))

mapa2 = image.load("mapas/mapa2.png")
mapa2 = transform.scale(mapa2, (1280,720))

mapa3 = image.load("mapas/mapa3.png")
mapa3 = transform.scale(mapa3, (1280,720))

mapa4 = image.load("mapas/mapa4.png")
mapa4 = transform.scale(mapa4, (1280,720))

mapa5 = image.load("mapas/mapa5.png")
mapa5 = transform.scale(mapa5, (1280,720))

instrucciones = image.load("fondos/instrucciones.png")
instrucciones = transform.scale(instrucciones, (1280,720))

playerizq = cargar_animacion("left/left", ".png", 3)
playerder = cargar_animacion("right/right", ".png", 3)
playerup = cargar_animacion("up/up", ".png", 3)
playerdown = cargar_animacion("down/down", ".png", 3)

player = image.load("player.png")
player = transform.scale(player, (28,32))

moviendose = False

xMapa1 = 0

xPlayer = 280
yPlayer = 120

speedPlayer = 2.5 # 0.8

obstaculos1 = image.load("mapas/mapa1_magenta.png")
obstaculos2 = image.load("mapas/mapa2_magenta.png")
obstaculos3 = image.load("mapas/mapa3_magenta.png")
obstaculos4 = image.load("mapas/mapa4_magenta.png")
obstaculos5 = image.load("mapas/mapa5_magenta.png")
magenta = Color(255,0,255,255)

def multilineText(screen, tipo, texto, width, x, y, R,G,B):
    while len(texto)>0:
        linea = ""
        lin = tipo.render(linea, True, (250,250,250))
        i=0
        espacio = -1
        while lin.get_width()<width and i<len(texto):
            linea = linea + texto[i]
            if texto[i]==" ": espacio = i
            i+=1
            lin = tipo.render(linea, True, (250,250,250))
        if i==len(texto): espacio = i
        lin = tipo.render(linea[:espacio+1], True, (R,G,B))
        texto = texto[espacio+1:]
        screen.blit(lin, (x, y))
        y = y + 50 # espacio entre líneas
        
def pintar_boton(boton,fontB,textoBoton,R,G,B):
    if boton.collidepoint(mouse.get_pos()):
        draw.rect(screen, (255, 123,0), boton, 0)
    else:
        draw.rect(screen, (19, 191,62), boton, 0)
    texto = fontB.render(textoBoton, True, (R,G,B))    
    screen.blit(texto, (boton.x+(boton.width-texto.get_width())/2,
                        boton.y+(boton.height-texto.get_height())/2))


def escenaJuego(screen):
		global score
		pared = image.load("minijuego/pared.jpg")
		pared = transform.scale(pared, (1280,720))

		flecha = image.load("minijuego/flecha.png")
		flecha = transform.scale(flecha, (196 // 2, 60 // 2))

		playerJ = image.load("minijuego/personaje.png")
		playerJ = transform.scale(playerJ, (102, 174))

		bat = image.load("minijuego/bat.png")
		bat = transform.scale(bat, (1104//8,749//8))

		batsX = []
		batsY = []

		for i in range(6):
				batsX.append(random.randint(1280, 2500))
				batsY.append(random.randint(20,600))   

		scorenivel = 0

		xpared = 0
		xpared1 = 1280

		xplayerJ = 50
		yplayerJ = 250

		xflecha = 1000
		yflecha = 1000

		xbat = random.randint(801, 1600)
		ybat = random.randint(20,500)
		
		pregunta = False
		puntitos = 0
		speedplayer = 1.4
		while True:
			if scorenivel >= 50:
				score += 50
				return 4
			if pregunta == False:
				screen.fill((255,255,255))
				for e in event.get():
						if e.type == QUIT: sys.exit()
						if e.type == KEYDOWN and e.key == K_p and xflecha > 1280:
								xflecha = xplayerJ + 75
								yflecha = yplayerJ + 86
				
				screen.blit(pared,(xpared,0))
				screen.blit(pared,(xpared1,0))

		#Movimiento
				if yplayerJ < 0:
						yplayerJ = 0
				if yplayerJ + 129 > 720:
						yplayerJ = 720 -129
				if key.get_pressed()[K_w]:
						yplayerJ = yplayerJ - speedplayer 
				if key.get_pressed()[K_s]:
						yplayerJ = yplayerJ + speedplayer 
						
				screen.blit(playerJ, (xplayerJ, yplayerJ))    
				screen.blit(flecha, (xflecha, yflecha))
				
				for i in range(6):
						screen.blit(bat, (batsX[i], batsY[i]))
						batsX[i] = batsX[i] - 1.8
						if batsX[i] < -150:
								batsX[i] = (random.randint(801, 2000))
								batsY[i] = (random.randint(20,650))
								
				playerJRect = Rect(xplayerJ, yplayerJ, player.get_width(), playerJ.get_height())
				flechaRect = Rect(xflecha, yflecha, flecha.get_width(), flecha.get_height())
				
				
				for i in range(6):
						batRect = Rect(batsX[i],batsY[i], bat.get_width(), bat.get_height())
						if playerJRect.colliderect(batRect):
								pregunta = True
						if flechaRect.colliderect(batRect):
								scorenivel += 1
								batsX[i] = (random.randint(801, 2000))
								batsY[i] = (random.randint(20,500))
				
				
				puntaje = "Puntos: " + str(scorenivel)
				fontB = font.Font("Gratise.ttf", 50)
				
				texto = fontB.render(puntaje, True, (255,255,255))
				screen.blit(texto, (1050,20))
				
				if xpared < -1280:
						xpared = 1280
				if xpared1 < -1280:
						xpared1 = 1280
						
				xpared = xpared-0.4 
				xpared1 = xpared1-0.4 
				xflecha = xflecha + 2.4 
				
				display.flip()
			elif pregunta == True:
				pregunta, puntitos = escenaPreguntasJuego(screen)
				scorenivel += puntitos
				puntitos = 0
				for i in range(6):
					batsX[i] = (random.randint(801, 2000))
					batsY[i] = (random.randint(20,650))
				

def escenaPreguntasJuego(screen):
	a = random.randint(1,6)
	b = random.randint(1,10)
	c = a * b
	fondo = image.load('minijuego/pared.jpg')
	fondo = transform.scale(fondo, (1280,720))
	myFont = font.Font("Gratise.ttf", 50)
	texto = 'Los murciélagos te atacan, si puedes disparar una flecha cada ' + str(a) + ' segundos, y hay ' + str(b) + ' murciélagos, ¿cuántos segundos tardarás en eliminar a todos si no fallas ninguna flecha?'
	boton = Rect(200,350,180,100) 
	boton2 = Rect(550,350,180,100)
	boton3 = Rect(900,350,180,100)
	boton4 = Rect(550,500,220,100)
	fontB = font.Font("Gratise.ttf", 50)
	textos = [str(c),str(c-random.randint(1,2)), str(c+random.randint(1,2))]
	random.shuffle(textos)
	textoBoton = textos[0]
	textoBoton2 = textos[1]
	textoBoton3 = textos[2]
	contestado = False
	puntitos = 0
	while True:
			for e in event.get():
				if e.type == QUIT: sys.exit()
				if e.type == MOUSEBUTTONDOWN and e.button == 1 and contestado == True:
					if boton4.collidepoint(mouse.get_pos()):
						if puntitos != 0:
							return False, 0
						else: return False, -5
				if e.type == MOUSEBUTTONDOWN and e.button == 1 and not contestado:
					
					if boton.collidepoint(mouse.get_pos()):
						contestado = True
						if c == int(textoBoton):
							texto = "¡Correcto! Da un clic para continuar"
							puntitos += 1
						else:
							texto  = "Esa no era la respuesta correcta, tardarás " + str(c) + " segundos. Da un clic para continuar"
					if boton2.collidepoint(mouse.get_pos()):
						contestado = True
						if c == int(textoBoton2):
							texto = "¡Correcto! Da un clic para continuar"
							puntitos += 1
						else:
							texto  = "Esa no era la respuesta correcta, tardarás " + str(c) + " segundos. Da un clic para continuar"
					if boton3.collidepoint(mouse.get_pos()):
						contestado = True
						if c == int(textoBoton3):
							texto = "¡Correcto! Da un clic para continuar"
							puntitos += 1
						else:
							texto  = "Esa no era la respuesta correcta, tardarás " + str(c) + " segundos. Da un clic para continuar"
			screen.blit(fondo, (0,0))
			multilineText(screen, myFont, texto, 1080, 110,75, 255,255,255)
			if contestado == False:
				pintar_boton(boton,fontB,textoBoton,255,255,255)
				pintar_boton(boton2,fontB,textoBoton2,255,255,255)
				pintar_boton(boton3,fontB,textoBoton3,255,255,255)
			else:
				pintar_boton(boton4,fontB,"Continuar",255,255,255)		
			display.flip()

def escenaMenu(screen):
	fondo = image.load('fondos/Menu.png')
	fondo = transform.scale(fondo, (1280,720))
	myFont = font.Font("Gratise.ttf", 50)
	boton = Rect(550,350,180,100)
	instruccion = False
	while True:
			for e in event.get():
				if e.type == QUIT: sys.exit()
				if e.type == MOUSEBUTTONDOWN and e.button == 1 and instruccion == False:
					if boton.collidepoint(mouse.get_pos()):
						fondo = instrucciones
						instruccion = True
						boton = Rect(550,600,180,80)
				if e.type == MOUSEBUTTONDOWN and e.button == 1 and instruccion == True:
					if boton.collidepoint(mouse.get_pos()):
						return 1
			screen.blit(fondo, (0,0))
			pintar_boton(boton,myFont,"Jugar",255,255,255)		
			display.flip()
		
def escenaObstaculo(screen):
	global score
	fondo = image.load('fondos/obstaculo.jpg')
	fondo = transform.scale(fondo, (1280,720))
	myFont = font.Font("Gratise.ttf", 50)
	boton = Rect(550,550,300,100)
	while True:
			for e in event.get():
				if e.type == QUIT: sys.exit()
				if e.type == MOUSEBUTTONDOWN and e.button == 1:
					if boton.collidepoint(mouse.get_pos()):
						score += 10
						return 3, 300, 300
			screen.blit(fondo, (0,0))
			pintar_boton(boton,myFont,"Quitar árboles",255,255,255)		
			display.flip()

def escenaFinal(screen):
	fondo = image.load('fondos/final.png')
	fondo = transform.scale(fondo, (1280,720))
	while True:
		for e in event.get():
			if e.type == QUIT: sys.exit()
		screen.blit(fondo, (0,0))		
		display.flip()

def instruccionesCastillo(screen):
	instrucciones_castillo = image.load("minijuego/instrucciones_castillo.png")
	instrucciones_castillo = transform.scale(instrucciones_castillo, (1280,720))	
	myFont = font.Font("Gratise.ttf", 50)
	boton = Rect(1050,600,180,80)
	while True:
			for e in event.get():
				if e.type == QUIT: sys.exit()
				if e.type == MOUSEBUTTONDOWN and e.button == 1:
					if boton.collidepoint(mouse.get_pos()):
						return 7
			screen.blit(instrucciones_castillo, (0,0))
			pintar_boton(boton,myFont,"Jugar",255,255,255)		
			display.flip()

def escenaLago(screen):
  global score
  a = random.randint(1,12)
  b = random.randint(1,12)
  c = a*b
  fondo = image.load('fondos/lago4.jpg')
  fondo = transform.scale(fondo, (1280,720))
  myFont = font.Font("Gratise.ttf", 50)
  texto = 'Te has encontrado con un lago, necesitas un barco para pasar. Para construir el barco necesitas '+ str(c) + ' tablones de madera, si un árbol te da ' + str(b) + ' tablones, ¿cuántos árboles necesitas?'
  boton = Rect(200,350,180,100) 
  boton2 = Rect(550,350,180,100)
  boton3 = Rect(900,350,180,100)
  boton4 = Rect(550,500,220,100)
  fontB = font.Font("Gratise.ttf", 50)
  textos = [str(a),str(a-random.randint(1,3)), str(a+random.randint(1,3))]
  random.shuffle(textos)
  textoBoton = textos[0]
  textoBoton2 = textos[1]
  textoBoton3 = textos[2]
  contestado = False
  while True:
      for e in event.get():
        if e.type == QUIT: sys.exit()
        if e.type == MOUSEBUTTONDOWN and e.button == 1 and contestado == True:
          if boton4.collidepoint(mouse.get_pos()):
            if score != 0:
              return 1, 780, 40
            else:
              return 1, 200, 100
        if e.type == MOUSEBUTTONDOWN and e.button == 1 and not contestado:
          if boton.collidepoint(mouse.get_pos()):
            contestado = True
            if a == int(textoBoton):
              right.play()
              texto = "¡Correcto! Da un clic para continuar"
              score += 15
            else:
              wrong.play()
              texto  = "Esa no era la respuesta correcta, necesitas " + str(a) + " tablones para construir el barco. Da un clic para continuar"
          if boton2.collidepoint(mouse.get_pos()):
            contestado = True
            if a == int(textoBoton2):
              right.play()
              texto = "¡Correcto! Da un clic para continuar"
              score += 15
            else:
              wrong.play()
              texto = "Esa no era la respuesta correcta, necesitas " + str(a) + " tablones para construir el barco. Da un clic para continuar"
          if boton3.collidepoint(mouse.get_pos()):
            contestado = True
            if a == int(textoBoton3):
              right.play()
              texto = "¡Correcto! Da un clic para continuar"
              score += 15
            else:
              wrong.play()
              texto = "Esa no era la respuesta correcta, necesitas " + str(a) + " tablones para construir el barco. Da un clic para continuar"
      screen.blit(fondo, (0,0))
      multilineText(screen, fontB, texto, 1080, 110,75, 0,0,0)
      if contestado == False:
        pintar_boton(boton,fontB,textoBoton,255,255,255)
        pintar_boton(boton2,fontB,textoBoton2,255,255,255)
        pintar_boton(boton3,fontB,textoBoton3,255,255,255)
      else:
        pintar_boton(boton4,fontB,"Continuar",255,255,255)		
      display.flip()

def escenaPuente(screen):
  global score
  preguntas = [
    ["¿Sabes de alguna letrita, que si le das vuelta, enseguida se convierte de consonante en vocal?", "La letra n", "La letra v", "La letra u", "La letra n"],
    ["¿Cuántos animales tengo en casa sabiendo que todos son perros menos dos, todos son gatos menos dos, y que todos son loros menos dos?", "Un perro, un gato y un loro", "3 perros", "Un perro, un loro y un conejo", "Un perro, un gato y un loro"],
    ["Si 5 máquinas hacen 5 artículos en 5 minutos, ¿cuánto tiempo dedicarán 100 máquinas en hacer 100 artículos?", "5 minutos", "25 minutos", "10 minutos", "5 minutos"],
  ]
  fondo = image.load('fondos/puente.png')
  fondo = transform.scale(fondo, (1280,720))
  myFont = font.Font("Gratise.ttf", 70)
  indice = random.randint(0,2)
  texto = preguntas[indice][0]
  boton = Rect(150,350,300,100) 
  boton2 = Rect(500,350,300,100)
  boton3 = Rect(820,350,300,100)
  boton4 = Rect(550,500,230,100)
  fontB = font.Font("Gratise.ttf", 25)
  textos = [preguntas[indice][1], preguntas[indice][2], preguntas[indice][3]]
  random.shuffle(textos)
  respuesta = preguntas[indice][4]
  textoBoton = textos[0]
  textoBoton2 = textos[1]
  textoBoton3 = textos[2]
  contestado = False
  while True:
      for e in event.get():
        if e.type == QUIT: sys.exit()
        if e.type == MOUSEBUTTONDOWN and e.button == 1 and contestado == True:
          if boton4.collidepoint(mouse.get_pos()):
            if texto == "¡Correcto! Da un clic para continuar":
              return 3, 420, 360
            else:
              return 3, 750, 360
        if e.type == MOUSEBUTTONDOWN and e.button == 1 and not contestado:
          if boton.collidepoint(mouse.get_pos()):
            contestado = True
            if textoBoton == respuesta:
              right.play()
              texto = "¡Correcto! Da un clic para continuar"
              score += 15
            else:
              wrong.play()
              texto  = "Esa no era la respuesta correcta. Da un clic para continuar"
          if boton2.collidepoint(mouse.get_pos()):
            contestado = True
            if textoBoton2 == respuesta:
              right.play()
              texto = "¡Correcto! Da un clic para continuar"
              score += 15
            else:
              wrong.play()
              texto  = "Esa no era la respuesta correcta. Da un clic para continuar"
          if boton3.collidepoint(mouse.get_pos()):
            contestado = True
            if textoBoton3 == respuesta:
              right.play()
              texto = "¡Correcto! Da un clic para continuar"
              score += 15
            else:
              wrong.play()
              texto  = "Esa no era la respuesta correcta. Da un clic para continuar"
      screen.blit(fondo, (0,0))
      multilineText(screen, myFont, texto, 1080, 110,75, 0,0,0)
      if contestado == False:
        pintar_boton(boton,fontB,textoBoton,255,255,255)
        pintar_boton(boton2,fontB,textoBoton2,255,255,255)
        pintar_boton(boton3,fontB,textoBoton3,255,255,255)
      else:
        pintar_boton(boton4,fontB,"Continuar",255,255,255)		
      display.flip()

def escenaVolcan(screen):
	global score
	a = random.randint(31,35)
	b = random.randint(20,31)
	c = a - b
	if c != 5:
		respuesta = "No"
	else:
		respuesta = "Si"
	
	fondo = image.load('fondos/Lava.png')
	fondo = transform.scale(fondo, (1280,720))
	myFont = font.Font("Gratise.ttf", 50)
	texto = '¡Oh no! El volcán ha hecho erupción. El volcán está a '+ str(a) + ' kilómetros de la aldea, una de las rocas que salió disparada cayó a ' + str(b) + ' kilómetros de la aldea, si el camino que recorres está a 5 kilómetros del volcán, ¿la roca está bloqueando el paso? (Tip: calcula la distancia entre la roca y el volcán)'
	boton = Rect(350,450,180,100) 
	boton2 = Rect(700, 450 ,180,100)
	boton4 = Rect(550,500,220,100)
	fontB = font.Font("Gratise.ttf", 50)
	textos = ["Si", "No"]
	random.shuffle(textos)
	textoBoton = textos[0]
	textoBoton2 = textos[1]
	
	contestado = False
	while True:
			for e in event.get():
				if e.type == QUIT: sys.exit()
				if e.type == MOUSEBUTTONDOWN and e.button == 1 and contestado == True:
					if boton4.collidepoint(mouse.get_pos()):
						return 2, 700,300
				if e.type == MOUSEBUTTONDOWN and e.button == 1 and not contestado:
					if boton.collidepoint(mouse.get_pos()):
						contestado = True
						if respuesta == textoBoton:
							right.play()
							texto = "¡Correcto! Da un clic para continuar"
							score += 15
						else:
							wrong.play()
							texto  = "Esa no era la respuesta correcta, la roca" + respuesta + " obstruye el paso. Da un clic para continuar"
					if boton2.collidepoint(mouse.get_pos()):
						contestado = True
						if respuesta == textoBoton2:
							right.play()
							texto = "¡Correcto! Da un clic para continuar"
							score += 15
						else:
							wrong.play()
							texto  = "Esa no era la respuesta correcta, la roca" + respuesta + " obstruye el paso. Da un clic para continuar"
			screen.fill((110,115,100))
			screen.blit(fondo, (0,0))
			multilineText(screen, fontB, texto, 1080, 110,75, 255,255,255)
			if contestado == False:
				pintar_boton(boton,fontB,textoBoton,255,255,255)
				pintar_boton(boton2,fontB,textoBoton2,255,255,255)
			else:
				pintar_boton(boton4,fontB,"Continuar",255,255,255)		
			display.flip()

def movimiento(obstaculos):
	global xPlayer, yPlayer, speedPlayer
	if key.get_pressed()[K_w]:
		pixelColor = obstaculos.get_at((int(xPlayer),int(yPlayer - speedPlayer)))
		if (pixelColor != magenta):
			yPlayer = yPlayer - speedPlayer
		mostrar_animacion(playerup,10,xPlayer,yPlayer)
	elif key.get_pressed()[K_s]:
		pixelColor = obstaculos.get_at((int(xPlayer),int(yPlayer + 32 + speedPlayer)))
		if (pixelColor != magenta):
			yPlayer = yPlayer + speedPlayer
		mostrar_animacion(playerdown,10,xPlayer,yPlayer)        
	elif key.get_pressed()[K_a]:
		pixelColor = obstaculos.get_at((int(xPlayer - speedPlayer),int(yPlayer)))
		if (pixelColor != magenta):
			xPlayer = xPlayer - speedPlayer
		mostrar_animacion(playerizq,10,xPlayer,yPlayer)      
	elif key.get_pressed()[K_d]:
		pixelColor = obstaculos.get_at((int(xPlayer + 28 + speedPlayer),int(yPlayer)))
		if (pixelColor != magenta):
			xPlayer = xPlayer + speedPlayer
		mostrar_animacion(playerder,10,xPlayer,yPlayer)
	else:
			screen.blit(player, (xPlayer, yPlayer))

def pintar_puntos():
	global score
	puntaje = "Puntos: " + str(score)
	fontB = font.Font("Gratise.ttf", 50)
	texto = fontB.render(puntaje, True, (255,255,255))
	screen.blit(texto, (1050,20))

#=============== while True principal ===================#
init()
screen = display.set_mode((1280,720))
mixer.init()
music = mixer.Sound("sonidos/adventure.wav")
right = mixer.Sound("sonidos/right.wav")
wrong = mixer.Sound("sonidos/wrong.wav")
music.set_volume(0.05)
right.set_volume(0.2)
wrong.set_volume(0.2)
music.play(-1)

while True:
		screen.fill((255,255,255))
		for e in event.get():
			if e.type == QUIT: sys.exit()
		if escena == 5:
			escena, xPlayer, yPlayer = escenaLago(screen)
		elif escena == 7:
			escena = escenaJuego(screen)
		elif escena == 8:
			escena = instruccionesCastillo(screen)
		elif escena == 9:
			escena, xPlayer, yPlayer = escenaPuente(screen)
		elif escena == 10:
			escenaFinal(screen)
		elif escena == 11:
			escena, xPlayer, yPlayer = escenaObstaculo(screen)
		elif escena == 6:
			escena, xPlayer, yPlayer = escenaVolcan(screen)
		elif escena == 0:
			escena = escenaMenu(screen)
		elif escena == 1:                                   #ESCENA 1
			if score >= 100:
				mapa1 = mapa5
				obstaculos1 = obstaculos5
				if xPlayer > 60 and xPlayer < 100 and yPlayer < 100 and yPlayer > 80:
					escena = 10
			screen.blit(mapa1,(0,0))
			movimiento(obstaculos1)					
			if xPlayer + 28 >= mapa1.get_width():	xPlayer = mapa1.get_width() - 28
			if xPlayer <= 5:
					xPlayer = 1250
					escena = 4
			if yPlayer + 32 >= mapa1.get_height()-4: yPlayer = mapa1.get_height() - 36
			if yPlayer <= 0:
					yPlayer = 680
					escena = 2
			if xPlayer > 700 and xPlayer < 732 and yPlayer < 275:
				escena = 5
			pintar_puntos()
			display.flip()
		elif escena == 2:                                      #ESCENA 2  FLECHAS Y PREGUNTAS 
			screen.blit(mapa2,(0,0))
			movimiento(obstaculos2)	
			if xPlayer + 28 >= mapa1.get_width() - 4:	xPlayer = mapa1.get_width() - 28
			if xPlayer <= 5:
					xPlayer = 1250
					escena = 3
			if yPlayer + 32 >= mapa1.get_height()-5:
					yPlayer = 6
					escena = 1
			if yPlayer <= 4:	yPlayer = 4
			if xPlayer > 850 and xPlayer < 900 and yPlayer > 260 and yPlayer < 300:
				escena = 6
			pintar_puntos()
			display.flip()
		elif escena == 3:                                      #ESCENA 3
			screen.blit(mapa3,(0,0))
			movimiento(obstaculos3)	
			if xPlayer + 28 >= mapa1.get_width()-4:
					xPlayer = 2
					escena = 2
			if xPlayer <= 3: xPlayer = 3
			if yPlayer + 32 >= mapa1.get_height()-4:
					yPlayer = 2
					escena = 4
			if yPlayer <= 0: yPlayer = 0
			if xPlayer > 630 and xPlayer < 650 and yPlayer < 370 and yPlayer > 340:	escena = 9
			if xPlayer > 260 and xPlayer < 300 and yPlayer < 230 and yPlayer > 200:	escena = 11
			pintar_puntos()
			display.flip()
		elif escena == 4:                                      #ESCENA 4
			screen.blit(mapa4,(0,0))
			movimiento(obstaculos4)						
			if xPlayer + 28 >= mapa1.get_width()-3:
					xPlayer = 2
					escena = 1 
			if xPlayer <= 3: xPlayer = 3
			if yPlayer + 32 >= mapa1.get_height():
					yPlayer = mapa1.get_height() -35
			if yPlayer <= 0:
					yPlayer = 688
					escena = 3
			if xPlayer < 90 and yPlayer > 200 and yPlayer < 280:
				escena = 8
				xPlayer = 100
			pintar_puntos()
			display.flip()
    
    


