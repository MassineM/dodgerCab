import pygame
import random
import time

pygame.init()
W=600
H=600
carW=40
carH=60
gameDisplay = pygame.display.set_mode((W, H))
gameDisplay.fill((255,255,255))
pygame.display.set_caption("Crazy Cab: Cops Escape")
gameExit=False
clock=pygame.time.Clock()
score=0
best=0
yPos = H-200
xPos = W/2
xPos_change=0
tick=5
xTraffic1=random.randrange(-600,-239,carH)
xTraffic2=xTraffic1+840
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
lol=tick+1
msgOut_b("Crazy Cab: Cops Escape", (0,240,0))
msgOut_l("Press space to start...", (0,0,0))
pygame.display.update()
while gameStop and not gameExit:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            gameExit=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                gameDisplay.fill((255,255,255))
                pygame.display.update()
                gameStop=False
while not gameExit:
    pygame.display.update()
    while not gameExit and not gameStop:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                gameExit=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_KP_ENTER:
                    lol=-lol
                    xPos_change=lol
        if xPos > W-40 or xPos < 0:
            gameStop=True
        if xPos <= xTraffic1+600 and yPos <= yTraffic + carW and not yPos + carH < yTraffic:
            gameStop=True
        if xPos+carW >= xTraffic2 and yPos <= yTraffic + carW and not yPos + carH < yTraffic:
            gameStop=True
        xPos+=xPos_change
        gameDisplay.fill((255,255,255))
        pygame.draw.rect(gameDisplay, (0,0,240), [xPos,yPos,carW,carH])
        pygame.draw.rect(gameDisplay,(50,50,50),[xTraffic1,yTraffic,600,carW])
        pygame.draw.rect(gameDisplay,(50,50,50),[xTraffic2,yTraffic,600,carW])
        yTraffic+=yTraffic_change
        pygame.display.update()
        if yTraffic>=H:
            score+=1
            yTraffic=-carH
            xTraffic1=random.randrange(-600,-239,carH)
            xTraffic2=xTraffic1+840
            tick+=1/4
            if lol<0:
                lol=-tick-1
            else:
                lol=tick+1
            yTraffic_change=tick
        if gameStop:
            if score>best:
                best=score
            msgOut_b("YOU LOSE", (240,0,0))
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
                        lol=tick+1
                        xTraffic1=random.randrange(-600,-239,carH)
                        xTraffic2=xTraffic1+840
                        yTraffic_change=tick
                        yTraffic=-carW
                        xPos_change=0
                        score=0
                        xPos= W/2
                        gameStop=False
        clock.tick(60)
pygame.quit()
quit()
        
