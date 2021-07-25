#!/usr/bin/python3
#-------------------------------------------------------------------#
# MOURAD TOUNSI                                                     #
#-------------------------------------------------------------------#

import math,pygame,sys

# initialisation -----------------------------$
pygame.init()
screen=pygame.display.set_mode((400,400))
pygame.display.set_caption("cube wave")
clock=pygame.time.Clock()
fps=60

# classes ------------------------------------$
class Barre():
    def __init__(self):
        self.pos=(50,250)
        self.const=40
        self.height=50
        self.width=20
        self.color1=(230,200,0)
        self.color2=(200,100,0)
        self.color3=(0xFF,0x57,0x33)
    
    def draw(self):
        self.height=int(self.height)
        self.width=int(self.width)
        pygame.draw.polygon(screen,self.color1,(self.pos,(self.pos[0],self.pos[1]-self.height),(self.pos[0]-int(self.width/2),self.pos[1]-self.height-5),(self.pos[0]-int(self.width/2),self.pos[1]-5)))
        pygame.draw.polygon(screen,self.color2,(self.pos,(self.pos[0],self.pos[1]-self.height),(self.pos[0]+int(self.width/2),self.pos[1]-self.height-5),(self.pos[0]+int(self.width/2),self.pos[1]-5)))
        pygame.draw.polygon(screen,self.color3,((self.pos[0],self.pos[1]-self.height),(self.pos[0]+int(self.width/2),self.pos[1]-self.height-5),(self.pos[0],self.pos[1]-self.height-10),(self.pos[0]-int(self.width/2),self.pos[1]-self.height-5)))
    
class VU():
    def __init__(self):
        self.x=(10+1,5+1)
        self.y=(10+2,-5-1)

# fonctions ----------------------------------$
def add(a,b):
    return (a[0]+b[0],a[1]+b[1])

def mult(k,a):
    return (k*a[0],k*a[1])

# declaration --------------------------------$
tab=[]
var=0
k=15
for i in range(0,k,1):
    tab.append([])

for i in range(0,len(tab),1):
    for j in range(0,k,1):
        tab[i].append(Barre())

for i in range(0,len(tab),1):
    for j in range(0,len(tab[i]),1):
        tab[i][j].pos=add(tab[i][j].pos,add(mult(i,VU().x),mult(j,VU().y)))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # change height --------------------------$
    for i in range(0,len(tab),1):
        for j in range(0,len(tab[i]),1):
            tab[i][j].height=(math.sin(-var+math.sqrt((i/2-(3.5))**2+(j/2-(3.5))**2))+1)*tab[i][j].const
    var+=(1/20)
    var=var%6.283
    
    # draw -----------------------------------$
    screen.fill((0,0,40))
    for i in range(0,len(tab),1):
        for j in range(len(tab[i])-1,-1,-1):
            tab[i][j].draw()

    # update ---------------------------------$
    pygame.display.flip()
    clock.tick(fps)
