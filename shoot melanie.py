import pgzrun
import random
WIDTH=726
HIGHT=763
melanie=Actor("melanie")
melanie.pos=(300,300)

def draw():
    screen.fill("light blue")
    melanie.draw()

pgzrun.go()
