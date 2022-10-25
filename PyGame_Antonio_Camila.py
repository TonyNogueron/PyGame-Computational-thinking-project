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



escena = 5

pared = image.load("pared.jpg")
pared = transform.scale(pared, (1280,720))

flecha = image.load("flecha.png")
flecha = transform.scale(flecha, (196 // 2, 60 // 2))

playerJ = image.load("personaje.png")
playerJ = transform.scale(playerJ, (102, 174))

bat = image.load("bat.png")
bat = transform.scale(bat, (1104//8,749//8))

batsX = []
batsY = []

for i in range(6):
    batsX.append(random.randint(1280, 2500))
    batsY.append(random.randint(20,600))   

score = 0

xpared = 0
xpared1 = 1280

xplayerJ = 50
yplayerJ = 250

xflecha = 1000
yflecha = 1000

xbat = random.randint(801, 1600)
ybat = random.randint(20,500)

speedplayer = 1.4


mapa1 = image.load("mapas/mapa1.png")
mapa1 = transform.scale(mapa1, (1280,720))

mapa2 = image.load("mapas/mapa2.png")
mapa2 = transform.scale(mapa2, (1280,720))

mapa3 = image.load("mapas/mapa3.png")
mapa3 = transform.scale(mapa3, (1280,720))

mapa4 = image.load("mapas/mapa4.png")
mapa4 = transform.scale(mapa4, (1280,720))


playerizq = cargar_animacion("left/left", ".png", 3)
playerder = cargar_animacion("right/right", ".png", 3)
playerup = cargar_animacion("up/up", ".png", 3)
playerdown = cargar_animacion("down/down", ".png", 3)

player = image.load("player.png")
player = transform.scale(player, (28,32))

moviendose = False

xMapa1 = 0
cuadro = 40

xPlayer = 280
yPlayer = 120


speedPlayer = 2.5 # 0.8

obstaculos1 = image.load("mapas/mapa1_magenta.png")
obstaculos2 = image.load("mapas/mapa2_magenta.png")
obstaculos3 = image.load("mapas/mapa3_magenta.png")
obstaculos4 = image.load("mapas/mapa4_magenta.png")
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

scorenivel = 0

def escenaJuego(screen):
		global xflecha, yflecha, xplayerJ, yplayerJ, xpared, xpared1, scorenivel, playerJ
		while True:
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
							print("Pregunta!")
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


def escenaLago(screen):
	global score, escena, xplayer, yplayer
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
					escena = 1
					xplayer = 780
					yplayer = 50
					print("clic")
			if e.type == MOUSEBUTTONDOWN and e.button == 1 and not contestado:
				contestado = True
				if boton.collidepoint(mouse.get_pos()):
					if a == int(textoBoton):
						texto = "¡Correcto! Da un clic para continuar"
						score += 15
					else:
						texto  = "Esa no era la respuesta correcta, necesitas " + str(a) + " tablones para construir el barco. Da un clic para continuar"
				if boton2.collidepoint(mouse.get_pos()):
					if a == int(textoBoton2):
						texto = "¡Correcto! Da un clic para continuar"
						score += 15
					else:
						texto = "Esa no era la respuesta correcta, necesitas " + str(a) + " tablones para construir el barco. Da un clic para continuar"
				if boton3.collidepoint(mouse.get_pos()):
					if a == int(textoBoton3):
						texto = "¡Correcto! Da un clic para continuar"
						score += 15
					else:
						texto = "Esa no era la respuesta correcta, necesitas " + str(a) + " tablones para construir el barco. Da un clic para continuar"
		screen.blit(fondo, (0,0))
		multilineText(screen, myFont, texto, 1080, 110,75, 0,0,0)
		if contestado == False:
			pintar_boton(boton,fontB,textoBoton,255,255,255)
			pintar_boton(boton2,fontB,textoBoton2,255,255,255)
			pintar_boton(boton3,fontB,textoBoton3,255,255,255)
		else:
			pintar_boton(boton4,fontB,"Continuar",255,255,255)		
		display.flip()
	


# escena del volcán, hay que adaptarlo
def escenaVolcan(screen):
  a = random.randint(1,12)
  b = random.randint(1,12)
  c = a*b  
  fondo = image.load('fondos/Lava.jpg')
  fondo = transform.scale(fondo, (1280,720))
  myFont = font.Font("Gratise.ttf", 50)
  texto = 'Te has encontrado con un lago, necesitas un barco para pasar. Para construir el barco necesitas '+ str(c) + ' tablones de madera, si un árbol te da ' + str(b) + ' tablones, ¿cuántos árboles necesitas?'
  boton = Rect(200,350,180,100) 
  boton2 = Rect(550,350,180,100)
  boton3 = Rect(900,350,180,100)
  fontB = font.Font("Gratise.ttf", 50)
  textos = [str(a),str(a-random.randint(1,3)), str(a+random.randint(1,3))]
  random.shuffle(textos)
  textoBoton = textos[0]
  textoBoton2 = textos[1]
  textoBoton3 = textos[2]
  contestado = False
  while True:
    #
    screen.fill((60,65,60))
    for e in event.get():
      if e.type == QUIT: sys.exit()
      if e.type == MOUSEBUTTONDOWN and e.button == 1 and not contestado:
        contestado = True
        if boton.collidepoint(mouse.get_pos()):
          if a == int(textoBoton):
            print("¡Correcto!")
          else:
            print("Esa no era la respuesta correcta, necesitas " + str(a) + " tablones para construir el barco")
        if boton2.collidepoint(mouse.get_pos()):
          if a == int(textoBoton2):
            print("¡Correcto!")
          else:
            print("Esa no era la respuesta correcta, necesitas " + str(a) + " tablones para construir el barco")
        if boton3.collidepoint(mouse.get_pos()):
          if a == int(textoBoton3):
            print("¡Correcto!")
          else:
            print("Esa no era la respuesta correcta, necesitas " + str(a) + " tablones para construir el barco")
    screen.blit(fondo, (0,0))
    multilineText(screen, myFont, texto, 1080, 110,75, 0,0,0)
    pintar_boton(boton,fontB,textoBoton,255,255,255)
    pintar_boton(boton2,fontB,textoBoton2,255,255,255)
    pintar_boton(boton3,fontB,textoBoton3,255,255,255)

    display.flip()



init()
screen = display.set_mode((1280,720))

while True:
    screen.fill((255,255,255))
    for e in event.get():
        if e.type == QUIT: sys.exit()
        #if e.type == KEYDOWN and e.key == K_p:
    if escena == 5:
        escenaLago(screen)
    elif escena == 7:
        escenaJuego(screen)
    elif escena == 6:
        escenaVolcan(screen)
    elif escena == 1:                                   #ESCENA 1
        screen.blit(mapa1,(0,0))

        #Movimiento
        if key.get_pressed()[K_w]:
            pixelColor = obstaculos1.get_at((int(xPlayer),int(yPlayer - speedPlayer)))
            if (pixelColor != magenta):
                yPlayer = yPlayer - speedPlayer
            mostrar_animacion(playerup,10,xPlayer,yPlayer)
        elif key.get_pressed()[K_s]:
            pixelColor = obstaculos1.get_at((int(xPlayer),int(yPlayer + 32 + speedPlayer)))
            if (pixelColor != magenta):
                yPlayer = yPlayer + speedPlayer
            mostrar_animacion(playerdown,10,xPlayer,yPlayer)        
        elif key.get_pressed()[K_a]:
            pixelColor = obstaculos1.get_at((int(xPlayer - speedPlayer),int(yPlayer)))
            if (pixelColor != magenta):
                xPlayer = xPlayer - speedPlayer
            mostrar_animacion(playerizq,10,xPlayer,yPlayer)      
        elif key.get_pressed()[K_d]:
            pixelColor = obstaculos1.get_at((int(xPlayer + 28 + speedPlayer),int(yPlayer)))
            if (pixelColor != magenta):
                xPlayer = xPlayer + speedPlayer
            mostrar_animacion(playerder,10,xPlayer,yPlayer)
                
        else:
                screen.blit(player, (xPlayer, yPlayer))
                
        if xPlayer + 28 >= mapa1.get_width():
                xPlayer = mapa1.get_width() - 28
        if xPlayer <= 5:
                xPlayer = 1250
                escena = 4
        if yPlayer + 32 >= mapa1.get_height():
                yPlayer = mapa1.get_height() - 36
        if yPlayer <= 0:
                yPlayer = 688
                escena = 2
        if xPlayer > 700 and xPlayer < 732 and yPlayer < 275:
            escena = 5
        puntaje = "Puntos: " + str(score)
        fontB = font.Font("Gratise.ttf", 50)
        texto = fontB.render(puntaje, True, (255,255,255))
        screen.blit(texto, (1050,20))
        display.flip()
    elif escena == 2:                                      #ESCENA 2  FLECHAS Y PREGUNTAS 
        screen.blit(mapa2,(0,0))

        #Movimiento
        if key.get_pressed()[K_w]:
            pixelColor = obstaculos2.get_at((int(xPlayer),int(yPlayer - speedPlayer)))
            if (pixelColor != magenta):
                yPlayer = yPlayer - speedPlayer
            mostrar_animacion(playerup,10,xPlayer,yPlayer)
        elif key.get_pressed()[K_s]:
            pixelColor = obstaculos2.get_at((int(xPlayer),int(yPlayer + 32 + speedPlayer)))
            if (pixelColor != magenta):
                yPlayer = yPlayer + speedPlayer
            mostrar_animacion(playerdown,10,xPlayer,yPlayer)        
        elif key.get_pressed()[K_a]:
            pixelColor = obstaculos2.get_at((int(xPlayer - speedPlayer),int(yPlayer)))
            if (pixelColor != magenta):
                xPlayer = xPlayer - speedPlayer
            mostrar_animacion(playerizq,10,xPlayer,yPlayer)      
        elif key.get_pressed()[K_d]:
            pixelColor = obstaculos2.get_at((int(xPlayer + 28 + speedPlayer),int(yPlayer)))
            if (pixelColor != magenta):
                xPlayer = xPlayer + speedPlayer
            mostrar_animacion(playerder,10,xPlayer,yPlayer)
                
        else:
                screen.blit(player, (xPlayer, yPlayer))
                
        if xPlayer + 28 >= mapa1.get_width():
                xPlayer = mapa1.get_width() - 28
        if xPlayer <= 5:
                xPlayer = 1250
                escena = 3
        if yPlayer + 32 >= mapa1.get_height():
                yPlayer = mapa1.get_height() - 32
        if yPlayer <= 5:
                yPlayer = 3
        display.flip()
    elif escena == 3:                                      #ESCENA 3
        screen.blit(mapa3,(0,0))

        #Movimiento
        if key.get_pressed()[K_w]:
            pixelColor = obstaculos3.get_at((int(xPlayer),int(yPlayer - speedPlayer)))
            if (pixelColor != magenta):
                yPlayer = yPlayer - speedPlayer
            mostrar_animacion(playerup,10,xPlayer,yPlayer)
        elif key.get_pressed()[K_s]:
            pixelColor = obstaculos3.get_at((int(xPlayer),int(yPlayer + 32 + speedPlayer)))
            if (pixelColor != magenta):
                yPlayer = yPlayer + speedPlayer
            mostrar_animacion(playerdown,10,xPlayer,yPlayer)        
        elif key.get_pressed()[K_a]:
            pixelColor = obstaculos3.get_at((int(xPlayer - speedPlayer),int(yPlayer)))
            if (pixelColor != magenta):
                xPlayer = xPlayer - speedPlayer
            mostrar_animacion(playerizq,10,xPlayer,yPlayer)      
        elif key.get_pressed()[K_d]:
            pixelColor = obstaculos3.get_at((int(xPlayer + 28 + speedPlayer),int(yPlayer)))
            if (pixelColor != magenta):
                xPlayer = xPlayer + speedPlayer
            mostrar_animacion(playerder,10,xPlayer,yPlayer)
                
        else:
                screen.blit(player, (xPlayer, yPlayer))
                
        if xPlayer + 28 >= mapa1.get_width():
                xPlayer = 2
                escena = 2
        if xPlayer <= 3:
                xPlayer = 3
        if yPlayer + 32 >= mapa1.get_height()-4:
                yPlayer = 2
                escena = 4
        if yPlayer <= 0:
                yPlayer = 0
        display.flip()
    elif escena == 4:                                      #ESCENA 4
        screen.blit(mapa4,(0,0))

        #Movimiento
        if key.get_pressed()[K_w]:
            pixelColor = obstaculos4.get_at((int(xPlayer),int(yPlayer - speedPlayer)))
            if (pixelColor != magenta):
                yPlayer = yPlayer - speedPlayer
            mostrar_animacion(playerup,10,xPlayer,yPlayer)
        elif key.get_pressed()[K_s]:
            pixelColor = obstaculos4.get_at((int(xPlayer),int(yPlayer + 32 + speedPlayer)))
            if (pixelColor != magenta):
                yPlayer = yPlayer + speedPlayer
            mostrar_animacion(playerdown,10,xPlayer,yPlayer)        
        elif key.get_pressed()[K_a]:
            pixelColor = obstaculos4.get_at((int(xPlayer - speedPlayer),int(yPlayer)))
            if (pixelColor != magenta):
                xPlayer = xPlayer - speedPlayer
            mostrar_animacion(playerizq,10,xPlayer,yPlayer)      
        elif key.get_pressed()[K_d]:
            pixelColor = obstaculos4.get_at((int(xPlayer + 28 + speedPlayer),int(yPlayer)))
            if (pixelColor != magenta):
                xPlayer = xPlayer + speedPlayer
            mostrar_animacion(playerder,10,xPlayer,yPlayer)
                
        else:
                screen.blit(player, (xPlayer, yPlayer))
                
        if xPlayer + 28 >= mapa1.get_width()-3:
                xPlayer = 2
                escena = 1 
        if xPlayer <= 3:
                xPlayer = 3
        if yPlayer + 32 >= mapa1.get_height():
                yPlayer = mapa1.get_height() -35
        if yPlayer <= 0:
                yPlayer = 688
                escena = 3
        
        

        display.flip()
    
    


  