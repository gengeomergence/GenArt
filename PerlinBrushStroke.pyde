######################
## General Settings ##
######################

w = 2000
h = 2000

pencolor = color(100)
bgcolor = color(0)
thickness = 2
    
###########################
## Perlin Noise Settings ##
##    mess with these    ##
###########################

seeded = False  ## Set to true to use seeds for consistant noise
colored = True  ## False for b/w, True for set color selection
blended = False  ## True adds transparancy and blend effect
manipulateAngle = False  ## True will drastically change effect

sca = 0.02  #  noise scalar
mapMin = 0  # minimum y-axis deviation
mapMax = 100  # maximum y-axis deviation
noise_detail = 1  # noise detail
noise_seed = 2  # noise seed if seeding
minRadius = 0 # arc inner radius
maxRadius = 700  # arc outer radius
minAngle = 0  # arc start angle
maxAngle = 270  # arc stop angle
radiusStep = 1  # arc density
angleStep = 1  # rotational steps

#################################
## Colors (if colored == true) ##
#################################

pencolor1 = color(8, 126, 139)
pencolor2 = color(255, 90, 90)
pencolor3 = color(0, 0, 0)
rules = [7, 11]  # divisor rules to color noise

## MAIN ##
##########

def setup():
    size(w, h)
    background(bgcolor)
    stroke(pencolor)
    fill(0)
    if blended == True:
        blendMode(ADD)
    strokeWeight(thickness)
    if seeded == True:
        noiseSeed(noise_seed)
    translate(width/2, height/2)
    noiseDetail(noise_detail)
    for angle in range(minAngle, maxAngle, angleStep):
        for radius in range(minRadius, maxRadius, radiusStep):
            n = noise(radius*sca, angle*sca)
            m = round(map(n, 0.0, 1.0, mapMin, mapMax))
            if colored == True:
                if m % rules[0] == 0:
                    stroke(pencolor1)
                elif m % rules[1] == 0:
                    stroke(pencolor2)
                else:
                    stroke(pencolor3)
                    # noStroke()
            pushMatrix()
            if manipulateAngle == True:
                rotate(radians(angle*n))
            else:
                rotate(radians(angle))
            translate(radius, m)
            point(0, 0)
            popMatrix()
    
    save("perlinStrokes_8.png")
