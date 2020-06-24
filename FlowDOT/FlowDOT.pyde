from FlowBall import Ball
from ColorMachine import colMachine
from Colors import c1, c2, c3, c4, c5, c6, c7, c8, c9, c10

sca1 = 0.005
sca2 = 0.005
step = 2
balls = []
off = 1000
minn = 1000
maxx = 2000

def setup():
    size(1000, 1000)
    
    background(255)
    stroke(255)
    fill(255)
    # noFill()
    # rect(1, 1, width-1, height-1)
    # circle(width - 500, 500, 500)
    # circle(width/2, height/2, 500)
    loadPixels()
    for x in range(step, width, step):
        for y in range(step, height, step):
            i = y*width+x
            if pixels[i] == -1:
                vx = random(-10, 10)
                vy = random(-10, 10)
                balls.append(Ball(x+vx, y+vy, 0, 0))
    # for x in range(width):
        # y = height/2
        # y = x
        # balls.append(Ball(x, y, 0, 0))
    background(0)
    noiseDetail(10)
    # strokeWeight(5)
    stroke(255)
    
def draw():
    global minn, maxx
    background(0)
    for b in balls:
        
        x1 = b.posV.x + off
        y1 = b.posV.y + off

        ni = noise(x1*sca1, y1*sca1)
        mi = map(ni, 0, 1, minn, maxx)
        
        n1 = noise(mi*sca2, mi*sca2)
        m1 = map(n1, 0, 1, -360, 360)

        b.move(m1)

        if b.posV.x < 0:
            b.posV.x = width
        if b.posV.x > width:
            b.posV.x = 0
        if b.posV.y < 0:
            b.posV.y = height
        if b.posV.y > height:
            b.posV.y = 0
    minn += 1
    maxx += 1
    
    saveFrame("ItsALIVE/###.tif")
        # if frameCount % 500 == 0:
            # off += 1
# def keyPressed():
    # save("FLOWtry2_23.png")
