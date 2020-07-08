from NoiseBall import NoiseBall

nballs = []
col = color(0)
sca1 = 0.003
sca2 = 0.003
minn = 1000
maxx = 3000

def setup():
    size(2000, 2000)
    background(0)
    fill(255)
    circle(width/2, height/2, 900)
    loadPixels()
    background(255)
    # for _ in range(1):
        # x = random(width)
        # y = random(height)
        # nballs.append(NoiseBall(x, y))
    nballs.append(NoiseBall(width, height/2))
def draw():
    # background(255)
    global minn, maxx
    for nb in nballs:

        x = floor(nb.pos.x)
        y = floor(nb.pos.y)

        ni = noise(x*sca1, y*sca1)
        mi = map(ni, 0, 1, minn, maxx)
        n = noise(mi*sca2, mi*sca2)
        m = floor(map(ni, 0, 1, 2, 100))
        nb.setSiz(m)
            
        frc = PVector.fromAngle(n*TWO_PI)
        frc.setMag(0.1)
        nb.applyForce(frc)
        nb.move()
        nb.edge()
        inde = constrain(x+y*width, 0, width*height-1)
        if pixels[inde] == -1:
            nb.display(col)
    
    minn += 1
    maxx += 1
