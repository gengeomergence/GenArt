from Forces import Force
from Particles import Particle
from NoiseyColor import ncol
from random import choice

parts = []
forces = []
sca = 0.005

c1 = color(1, 22, 39)
c2 = color(253, 255, 252)
c3 = color(255, 0, 0)

step = 10

sts = [10]

def setup():
    global balls
    size(1000, 1000)
    
    for i in range(10):
        x = random(200, 800)
        y = random(200, 800)
        # strength = random(-2, 2)
        strength = choice(sts)
        # strength = sts[i]
        forces.append(Force(x, y, strength))
    # background(0)
    # noFill()
    # stroke(255)
    # strokeWeight(2)
    # circle(width/2, height/2, 900)
    # loadPixels()
    # for x in range(step, width, step):
    #     for y in range(step, height, step):
    #         if pixels[x+y*width] == -1:
    #             parts.append(Particle(x, y, 0, 0, 1))
    # updatePixels()

    # for x in range(50, 950 + step, step):
    #     y = 50
    #     parts.append(Particle(x, y, 0, 0, 1))
    #     y = 950
    #     parts.append(Particle(x, y, 0, 0, 1))
    
    # for y in range(50, 950+step, step):
    #     x = 50
    #     parts.append(Particle(x, y, 0, 0, 1))
    #     x = 950
    #     parts.append(Particle(x, y, 0, 0, 1))
    
    for _ in range(1000):
        x = random(width)
        y = random(height)
        parts.append(Particle(x, y, 0, 0, 1))
    
    loadPixels()
    for x in range(width):
        for y in range(height):
            c = ncol(c1, 10)
            pixels[x+y*width] = c
    updatePixels()

    
def draw():

    for p in parts:
        x = p.pos.x
        y = p.pos.y
        n = noise(x*sca, y*sca)

        for f in forces:
            
            force = PVector(f.fpos.x, f.fpos.y)
            
            r = dist(x, y, force.x, force.y)
            # st = f.strength/sq(r)

            art = tan(radians(r*n))
            st = f.strength*art
            
            force.sub(p.pos)
            force.setMag(st)
            p.applyForce(force)

            # f.display(c3, 10)
        
        p.move()
        # d = norm(dist(x, y, width/2, height/2), 100, 500)
        # col = lerpColor(c2, c1, d)

        p.display(c2, 2)

def keyPressed():
    save("gravStud_13.png")
    print("SAVED")
