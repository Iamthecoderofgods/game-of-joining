import random
import pgzrun

WIDTH = 700
HEIGHT = 600
TITLE = "Join"


def draw():
    
    screen.blit("space_backround",(0,0))
    for i in range(9):
        satilite = Actor("satilite")
        x = random.randint(0,WIDTH)
        y = random.randint(0,HEIGHT)
        satilite.pos = x,y
        satilite.draw()
        screen.draw.text(str(i+1),(x-7,y+20))

pgzrun.go()

