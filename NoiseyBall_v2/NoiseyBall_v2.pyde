from NoiseBall import NoiseBall

nballs = []
col = color(0)

sca1 = 0.003
sca2 = 0.001
sca3 = 0.004
sca4 = 0.005

minn = 1000
maxx = 3000
mval = 5

step = 50

def setup():
    size(2000, 2000)
    background(255)
    # for x in range(step, width, step):
        
    nballs.append(NoiseBall(width/2, height/2))
    
def draw():
    # background(255)
    # global minn, maxx
    for nb in nballs:
        x = nb.pos.x
        y = nb.pos.y
        x2 = width - x
        y2 = height - y
        
        ns = floor(map(noise(x*sca1, y*sca1), 0, 1, 2, 50))
        
        n1 = noise(x*sca1, y*sca1)
        n2 = noise(x2*sca1, y2*sca1)
        
        offx = map(n1, 0, 1, -mval, mval)
        offy = map(n2, 0, 1, -mval, mval)
        
        nb.move(offx, offy)
        nb.setSiz(ns)
        nb.display(col)
        
def mousePressed():
    nballs.append(NoiseBall(mouseX, mouseY))
