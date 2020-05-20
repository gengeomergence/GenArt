######################
## General Settings ##
######################

w = 2000  # Canvas width
h = 2000  # canvas height

bgColor = color(255, 255, 255)  # background color
penColor = color(0, 0, 0)  # stroke color
thickness = 2  # stroke thickness in pixels

###########################
## Perlin Noise Settings ##
###########################

seeded = False  # True to use specified noise seed
seed = 1

sca = 0.002  # noise scaling
detail = 10  # noise detail

mapMin = -1 # minimum value to map noise to
mapMax = 1  # maximum value to map noise to

#####################
## Object Settings ##
#####################

object_size = 800  # width and height boundaries of object
object_step = 200  # relates to number of curves created, used as step in loop
circle_logic = True  # set to False to remove circles at end of curves
circle_size = 10  # diameter of circle

#######################
## object definition ##
#######################

def noiseThing(leng, step):
    if seeded == True:
        noiseSeed(seed)
    else:
        noiseSeed(int(random(100000)))
    for i in range(-leng/2, leng/2 + step, step):
        for j in range(-leng/2, leng/2 + step, step):
            
            n = noise(i*sca, j*sca)
            m = map(n, 0, 1, mapMin, mapMax)
            
            i *= m*2
            j *= m
            
            bezier(0, 0, 0, j, i, 0, i, j)  # experiment with control points (4 middle values)
            if circle_logic == True:
                circle(i, j, circle_size)

def setup():
    size(w, h)
    background(bgColor)
    stroke(penColor)
    strokeWeight(thickness)
    noiseDetail(detail)
    noFill()
    translate(width/2, height/2)
    noiseThing(object_size, object_step)
