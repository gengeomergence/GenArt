class Ball(object):
    
    def __init__(self, posx, posy, vinx, viny):
        self.posx = posx
        self.posy = posy
        self.posV = PVector(self.posx, self.posy)
        self.vinx = vinx
        self.viny = viny
        self.vel = PVector(self.vinx, self.viny)
        
    def move(self, offset):
        
        
        offV = PVector.fromAngle(radians(offset))
        
        self.vel.add(offV)
                     
        self.vel.limit(2)

        self.posV.add(self.vel)
                
        point(self.posV.x, self.posV.y)
        
