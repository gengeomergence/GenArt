class Particle(object):
    
    def __init__(self, posx, posy, vx, vy, ma):
        
        self.pos = PVector(posx, posy)
        self.vel = PVector(vx, vy)
        self.acc = PVector(0, 0)
        self.mass = ma
        
    def applyForce(self, force):
        
        f = PVector.div(force, self.mass)
        self.acc.add(f)
    
    def move(self):
        
        self.vel.add(self.acc)
        self.vel.limit(2)
        self.pos.add(self.vel)
        self.acc.mult(0)
    
    def display(self, col, si):
        strokeWeight(si)
        stroke(col)
        point(self.pos.x, self.pos.y)
        
    
