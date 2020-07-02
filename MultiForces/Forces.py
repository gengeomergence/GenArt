class Force(object):
    
    def __init__(self, x, y, st):
        
        self.fpos = PVector(x, y)
        self.strength = st

    def display(self, col, si):

        noStroke()
        fill(col)
        circle(self.fpos.x, self.fpos.y, si)
