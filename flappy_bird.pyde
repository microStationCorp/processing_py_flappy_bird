from bird import Bird
from wall import Wall

go = 'game over'
walls = []

def setup():
    global bird, walls
    size(800, 500)
    bird = Bird()
    walls.append(Wall())

def draw():
    global bird, go, walls
    background(152, 253, 240)

    if walls[len(walls) - 1].pos_.x + walls[len(walls) - 1].xGap <= width:
        walls.append(Wall())

    for i in range(len(walls) - 1, -1, -1):
        if walls[i].pos_.x <= bird.pos.x <= (walls[i].pos_.x + walls[i].width_) and (0 < bird.pos.y < walls[i].upH or (height - walls[i].downH) < bird.pos.y < height):
            bird.gameOver = True

        if not walls[i].terminate:
            walls[i].show()
        else:
            walls.pop(i)

    if not bird.gameOver:
        bird.show()
    else:
        textSize(60)
        fill(255, 50, 50)
        text(go, (width - len(go) * 25) / 2, height / 2)
        bird.show()
        noLoop()


def keyPressed():
    global bird, walls
    if keyCode == 38:
        bird.vel.set(0, -8)
    elif keyCode == 40:
        bird.vel.add(0, 2, 0)
    elif keyCode == 10:
        bird = Bird()
        walls = []
        walls.append(Wall())
        loop()
