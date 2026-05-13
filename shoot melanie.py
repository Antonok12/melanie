import pgzrun
import random
WIDTH=726
HIGHT=763
melanie=Actor("realmelanie.png")
mark= Actor("markiplierintheflesh.png")
melanie.pos=(300,300)
message =""

def draw():
    screen.fill("light blue")
    melanie.draw()
    mark.draw()
    screen.draw.text(message, center=(100,20),fontsize =30)


def update():
    pass
def on_mouse_down(pos):
    global message
    if melanie.collidepoint(pos):
        melanie.x = random.randint(10,498)
        melanie.y = random.randint(10,490)
        message="GO ON LAD"

    elif mark.collidepoint(pos):
        mark.x = random.randint(10,498)
        mark.y = random.randint(10,490)
        message="GO ON LAD"
    else:
         message="awwww"
    
    


pgzrun.go()
