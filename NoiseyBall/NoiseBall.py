class NoiseBall(object):
    def __init__(self, posx, posy):
        self.pos = PVector(posx, posy)
        self.vel = PVector(0, 0)
        self.acc = PVector(0, 0)
        self.siz = 1
        self.life = 0
        
    def applyForce(self, force):
        self.acc.add(force)
        
    def move(self):
        self.vel.add(self.acc)
        self.vel.limit(2)
        self.pos.add(self.vel)
        self.acc.mult(0)
        
    def grow(self):
        if self.siz < 15:
            self.siz += 1
    
    def shrink(self):
        if self.siz > 2:
            self.siz -= 1
    def setSiz(self, val):
        self.siz = val
    
    def age(self):
        self.life += 1
        
    def display(self, col):
        stroke(col)
        strokeWeight(self.siz)
        point(self.pos.x, self.pos.y)
        
    def edge(self):
        if self.pos.x > width: self.pos.x = 0
        if self.pos.x < 0: self.pos.x = width
        if self.pos.y > height: self.pos.y = 0
        if self.pos.y < 0: self.pos.y = height
