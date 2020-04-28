class Wall:

    def __init__(self):
        self.pos_ = PVector(width, 0)
        self.width_ = 50
        self.yGap = 150
        self.xGap = 200
        self.upH = int(random(50, height - self.yGap))
        self.downH = height - (self.yGap + self.upH)
        self.vel = PVector(-2, 0)
        self.terminate = False

    def update(self):
        self.pos_.add(self.vel)

    def show(self):
        self.update()
        if self.pos_.x > 0 - self.width_:
            fill(33, 248, 87)
            stroke(0, 150, 0)
            strokeWeight(2)
            rect(self.pos_.x, self.pos_.y, self.width_, self.upH)
            rect(self.pos_.x, self.upH + self.yGap, self.width_, self.downH)
        else:
            self.terminate = True
