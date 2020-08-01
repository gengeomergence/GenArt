## This is an example of a flow field using a custom made pseudo-noise function. Its setup to draw some fancy lines in a donut shape
## The noise functuon itself is at the bottom, called jnoise (lame name but I never took the time to come up with something clever)
## For a fun experiment, mess around with the forcing function the noise value is used with. This is found in draw, variable ang
## Also mess with how the noise value itself is computed. Feel free to use this code as you'd like!
## Joshua Bagley, 08/01/2020, @gengeomergence on instagram

from PARTICLES import Particle

parts = []  ## ARRAY FOR PARTICLES

## This is an offset for the pseudo noise function. This gives a new field each run. Set to specific values for "seeds"
xoff = random(-5000, 5000)
yoff = random(-5000, 5000)

## COLORS ##
bacg = color(241, 247, 237)
penb = color(52, 52, 52)
acc1 = color(237, 37, 78)
acc2 = color(34, 170, 161)  ## Accent color 2
weight = 5                  ## Stroke Weight
###################

sca = 0.0005  ## scaling for noise input
step = 2  ## Modifies amount of particles spawned. increase for better performance, less particles. minimum 1

## GENERAL SETTINGS ##
w = 1000  ## Width of canvas
h = 1000  ## Height of canvas

outer_dia = 800  ## inner diameter of donut
inner_dia = 300  ## outer diameter of donut



def setup():
    size(w, h)
    frameRate(600)

    ## PARTICLE INITIALIZATION ##
    background(0)
    stroke(255)
    strokeWeight(1)
    noFill()
    circle(width/2, height/2, outer_dia)
    circle(width/2, height/2, inner_dia)
    loadPixels()
    for x in range(step, width, step):
        for y in range(step, height, step):
            if red(pixels[x+y*width]) > 100: parts.append(Particle(x, y))
    updatePixels()
    ##############################
    
    ## DRAW AREA DEFINITION ##
    background(0)
    fill(255)
    noStroke()
    circle(width/2, height/2, outer_dia)
    fill(0)
    circle(width/2, height/2, inner_dia)
    loadPixels()
    ##########################
    
    ## FINAL SETUP ##
    background(bacg)
    noFill()
    strokeWeight(weight)

def draw():
    pushStyle()
    strokeWeight(weight + 1)
    stroke(penb)
    circle(width/2, height/2, outer_dia)
    circle(width/2, height/2, inner_dia)
    popStyle()
    for p in parts:
        x = floor(p.pos.x)
        y = floor(p.pos.y)

        inde = constrain(x+y*width, 0, width*height-1)

        n = jnoise(x*sca, y*sca)

        ang = (sin(radians(x*n))+cos(radians(y*n)))*TAU
        
        m = floor(map(n, 0, 1, 0, 50))

        p.angForce(ang, 1)
        p.move()
        
        if pixels[inde] == -1:
            if m % 11 == 0: stroke(acc1)
            elif m % 13 == 0: stroke(acc2)
            else: stroke(penb)
            p.display()
        elif frameCount > 100: parts.remove(p)
        
## SCREENSHOTTER ##  (press any key while sketch is running to save a screenshot) ## EDIT: for some reason this breaks the sketch. I think it has something to do with the fact that I'm using pixels
def keyPressed():
    save("IMAGE_TITLE_HERE" + "_" + str(frameCount) + ".png")
    print("Saved!")
    
def jnoise(xi, yi):
    
    xi += xoff
    yi += yoff
    
    x = lerp(xi, yi, abs(sin(radians(xi))))
    y = lerp(yi, xi, abs(cos(radians(yi))))
    
    return norm(sin(radians(x+y)) * cos(radians(y-x)), -1, 1)
