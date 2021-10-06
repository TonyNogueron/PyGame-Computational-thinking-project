from pygame import *
import sys, random
import sys, time

init()
screen = display.set_mode((1280,720))

def cargar_animacion(nombre,extension, n):
    images = []
    for i in range(1,n+1):
        name = nombre+str(i)+extension
        images.append(image.load(name))
    return images

def mostrar_animacion(images, freq, x, y):
    frame = int(time.time()*freq) % len(images)
    screen.blit(images[frame],(x, y))



mapa1 = image.load("mapa1.jpeg")
mapa1 = transform.scale(mapa1, (1280,720))

playerizq = cargar_animacion("left/left", ".png", 3)
playerder = cargar_animacion("right/right", ".png", 3)
playerup = cargar_animacion("up/up", ".png", 3)
playerdown = cargar_animacion("down/down", ".png", 3)

player = image.load("player.png")
player = transform.scale(player, (28,32))

moviendose = False

xMapa1 = 0
cuadro = 40

xPlayer = 1
yPlayer = 1


speedPlayer = 0.15    

while True:
    screen.fill((255,255,255))
    for e in event.get():
        if e.type == QUIT: sys.exit()
        #if e.type == KEYDOWN and e.key == K_p:
    
    screen.blit(mapa1,(0,0))

    #Movimiento
    if key.get_pressed()[K_w]:
        yPlayer = yPlayer - speedPlayer
        mostrar_animacion(playerup,10,xPlayer,yPlayer)
        moviendose = True
    elif key.get_pressed()[K_s]:
        yPlayer = yPlayer + speedPlayer
        mostrar_animacion(playerdown,10,xPlayer,yPlayer)
        moviendose = True
    elif key.get_pressed()[K_a]:
        xPlayer = xPlayer - speedPlayer
        mostrar_animacion(playerizq,10,xPlayer,yPlayer)
        moviendose = True
    elif key.get_pressed()[K_d]:
        xPlayer = xPlayer + speedPlayer
        mostrar_animacion(playerder,10,xPlayer,yPlayer)
        moviendose = True
    else:
        screen.blit(player, (xPlayer, yPlayer))
        
    if xPlayer + 28 >= mapa1.get_width():
        xPlayer = mapa1.get_width() - 28
    if xPlayer <= 0:
        xPlayer = 0
    if yPlayer + 32 >= mapa1.get_height():
        yPlayer = mapa1.get_height() - 32
    if yPlayer <= 0:
        yPlayer = 0
    

         


            
    playerRect = Rect(xPlayer, yPlayer, player.get_width(), player.get_height())
       



    display.flip()
    
    