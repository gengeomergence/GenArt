class Particle(object):
    def __init__(self, posx, posy):
        self.pos = PVector(posx, posy)
        self.vel = PVector(random(-2, 2), random(-2, 2))
        self.acc = PVector(0, 0)

        
    def angForce(self, angle, strength):
        force = PVector.fromAngle(angle)
        force.setMag(strength)
        self.acc.add(force)
        
    def gravForce(self, centx, centy, st):
        grav = PVector(centx, centy)
        grav.sub(self.pos)
        grav.setMag(st)
        self.acc.add(grav)
        
    def genForce(self, fx, fy):
        genf = PVector(fx, fy)
        self.acc.add(genf)
    def move(self):
        self.vel.add(self.acc)
        self.vel.limit(0.5)
        self.pos.add(self.vel)
        self.acc.mult(0)
        
    def display(self):

        point(self.pos.x, self.pos.y)
