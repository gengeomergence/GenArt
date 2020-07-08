class NoiseBall(object):
    def __init__(self, posx, posy):
        self.pos = PVector(posx, posy)
        self.siz = 1
        self.life = 0
        
    def move(self, cx, cy):
        offV = PVector(cx, cy)
        self.pos.add(offV)
        
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
