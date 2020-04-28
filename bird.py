class Bird:

    def __init__(self):
        self.pos = PVector(100, height / 2)
        self.vel = PVector(0, 0)
        self.gravity = PVector(0, 0.5)
        self.dia = 10
        self.gameOver = False

    def update(self):
        self.vel.add(self.gravity)
        if 0 < self.pos.y < height:
            self.pos.add(self.vel)
        else:
            self.gameOver = True
            self.pos.sub(self.vel)

    def show(self):
        if not self.gameOver:
            self.update()
            fill(255, 100, 0)
            noStroke()
            ellipse(self.pos.x, self.pos.y, self.dia, self.dia)
        else:
            fill(255, 100, 0)
            noStroke()
            ellipse(self.pos.x, self.pos.y, self.dia, self.dia)
