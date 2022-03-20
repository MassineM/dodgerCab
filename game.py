import pygame
import random
import time

pygame.init()
W=1080
H=600
carW=40
carH=60
gameDisplay = pygame.display.set_mode((W, H))
gameDisplay.fill((255,255,255))
pygame.display.set_caption("Dodger Cab")
C=True
gameExit=False
clock=pygame.time.Clock()
Car1=pygame.image.load('car1.png')
Car2=pygame.image.load('car2.png')
overlay=pygame.image.load('Overlay.png')
overlay2=pygame.image.load('Overlay.png')
score=0
best=0
yPos = H-200
xPos = W/2
xPos_change=0
tick=5
xTraffic1=random.randrange(-W,-299,carH)
xTraffic2=xTraffic1+W+300
yTraffic=-carW
yTraffic_change=tick
gameStop=True
fontb=pygame.font.SysFont("comicsansms",50)
fontl=pygame.font.SysFont("comicsansms",25)
def msgOut_b(msg,color):
    text=fontb.render(msg,True,color)
    gameDisplay.blit(text,[10,100])
def msgOut_l(msg,color):
    text=fontl.render(msg,True,color)
    gameDisplay.blit(text,[10,200])
xMovement=tick+2
msgOut_b("DODGER CAB", (0,240,0))
msgOut_l("Press space to start...", (0,0,0))
pygame.display.update()
yOverlay=0
while gameStop and not gameExit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameExit=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                gameDisplay.blit(overlay,[0,0])
                pygame.display.update()
                gameStop=False
while not gameExit:
    pygame.display.update()
    while not gameExit and not gameStop:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    xMovement=-xMovement
                    xPos_change=xMovement
        if xPos-4 > W-40 or xPos+4 < 0:
            gameStop=True
        if xPos+4 <= xTraffic1+W and yPos <= yTraffic + carW-4 and not yPos + carH < yTraffic:
            gameStop=True
        if xPos+carW-4 >= xTraffic2 and yPos <= yTraffic + carW-4 and not yPos + carH < yTraffic:
            gameStop=True
        xPos+=xPos_change
        gameDisplay.blit(overlay2,[0,yOverlay-H])
        gameDisplay.blit(overlay,[0,yOverlay])
        gameDisplay.blit(Car1,[xPos,yPos])
        gameDisplay.blit(Car2,[xTraffic1,yTraffic])
        gameDisplay.blit(Car2,[xTraffic2,yTraffic])
        yOverlay+=yTraffic_change
        yTraffic+=yTraffic_change
        pygame.display.update()
        if yOverlay>=H:
            yOverlay=0
        if yTraffic<yPos and C:
            score+=1
            C=False
        if yTraffic>=H:
            C=True
            yTraffic=-carH
            xTraffic1=random.randrange(-W,-299,carH)
            xTraffic2=xTraffic1+W+300
            tick+=1/5
            if xMovement<0:
                xMovement=-tick-2
            else:
                xMovement=tick+2
            yTraffic_change=tick
        if gameStop:
            if score>best:
                best=score
            msgOut_b("OUCH!", (240,0,0))
            msgOut_l("Your score:%d." %score, (0,0,0))
            msgOut_l("                           Best:%d." %best, (0,0,0))
            pygame.display.update()
        while gameStop and not gameExit:
            tick=5
            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    gameExit=True
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_SPACE:
                        xMovement=tick+2
                        xTraffic1=random.randrange(-W,-299,carH)
                        xTraffic2=xTraffic1+W+300
                        yTraffic_change=tick
                        yTraffic=-carW
                        xPos_change=0
                        score=0
                        xPos= W/2
                        gameStop=False
        clock.tick(100)
pygame.quit()
quit()
        
getc()