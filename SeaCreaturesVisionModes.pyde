## IMPORTS ##
from random import choice, randint

## GENERAL (edit these) ##

w_h = 2000  # value for both width and height (forces square canvas)

text_size = 30  # Size of text, may need to adjust based on screen size

############# ONLY SET ONE TO TRUE, REST FALSE ######################

white_hot = True  # 'white is hot' infrared effect
black_hot = False  # 'black is hot' infrared effect
colored = False  # attempt at regular color image. set colors below
nvi = False  # Night vision

# if using colored, reccomend turning noiseReduction to False, and using dark shades of a color, 
# as there will be a blending effect that brightens pixels that overlap. Set background to darkest color,
# noisey background to medium, and creature to lightest. Try increments of 10 at first, adjust as needed

bgColored = color(0, 14, 41)
noiseyColored = color(10, 24, 51)
creatureColored = color(20, 34, 61)

#####################################################################

noiseReduction = False  # True removes background noise effect, false is more realistic

seeded = False  # if you have a creature id (noise seed), set to true and enter it below
creatureID = 9485

stacked = False  # True for multiple creature generation, stacked on top of each other, creating more complex creatures
stackedNum = 5  # Number of creatures to generate
## NOTE: stacked will not work if seeded is True ##

## Variables - Advanced (for regular use, leave these) ##

pOffset = w_h/2
pSize = pOffset
pStep = 1
pScale = 0.003

## MAIN ##

def pCreature(tSize, step, sca, offset):

    for i in range(0, tSize + step, step):
        for j in range(0, tSize + step, step):
            
            x = round(map(noise(i*sca, j*sca), 0, 1, -offset, offset))
            y = round(map(noise(j*sca, i*sca), 0, 1, -offset, offset))
            
            point(x, y)

def setup():
    global pOffset, pSize
    size(w_h, w_h)
    
    if white_hot == True:
        mode = 'WHOT'
        blendMode(ADD)
        background(0)
        stroke(20)
        npoints = width - (width/4)
        
    
    elif black_hot == True:
        mode = 'BHOT'
        blendMode(MULTIPLY)
        background(255)
        stroke(100)
        npoints = width/4
    
    elif colored == True:
        mode = 'CAM'
        blendMode(ADD)
        background(bgColored)
        stroke(noiseyColored)
        npoints = width - (width/4)

    elif nvi == True:
        mode = 'NVI'
        blendMode(ADD)
        background(21, 28, 13)
        stroke(31, 38, 23)
        npoints = width/4
    
    if noiseReduction == False:
        pushMatrix()
        translate(width/2 + 100, height/2 + 100)
        pCreature(npoints, 1, 0.3, width)
        popMatrix()
    
    noiseDetail(10)
    
    if colored == True:
        stroke(creatureColored)
    elif white_hot == True:
        stroke(100)
    elif black_hot == True:
        stroke(50)
    elif nvi == True:
        stroke(41, 48, 33)
    if seeded == True:
        cid = creatureID
    else:
        cid = int(random(100000))
    
    if stacked == False:
        noiseSeed(cid)
        pushMatrix()
        translate(width/2, height/2)
        pCreature(pSize, pStep, pScale, pOffset)
        popMatrix()
    
    elif stacked == True:
        
        pSize /= 2
        pushMatrix()
        translate(width/2, height/2)
        for _ in range(stackedNum):
            noiseSeed(int(random(100000)))
            pCreature(pSize, pStep, pScale, pOffset)
        popMatrix()
    
    ## TEXT GENERATION ##
    
    blendMode(BLEND)
    textSize(text_size)
    if white_hot == True:
        fill(255)
    elif black_hot == True:
        fill(0)
    
    m = ["01", "02", "03", "04", "05", "06", "07", "08", "09", 10, 11, 12]
    dayy = ["01", "02", "03", "04", "05", "06", "07", "08", "09"]
    for da in range(10, 32):
        dayy.append(da)
    
    y = randint(30, 40)
    lat = round(random(10000), 2)
    lon = round(random(10000), 2)
    depth = round(random(100000), 1)
    lcap = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    llow = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    nid = floor(random(900))
    resp = ["NR", "PR", "HR"]
    
    text("COG" + str(int(random(10))) + " / " + choice(resp), 25, height-550)
    text("MODE_" + mode, 25, height-500)
    
    text("EF: " + str(choice(lcap)) + str(choice(lcap)) + str(choice(lcap)) + "-" + str(nid) + str(choice(llow)), 25, height - 400)
    text("SYS: " + str(nid) + " " + str(choice(lcap)) + str(choice(llow)) + str(choice(llow)) + " " + str(choice(lcap)) + str(choice(llow)), 25, height - 350)
    
    text("DOE: " + str(choice(m)) + "." + str(choice(dayy)) + "." + str(y), 25, height - 250)
    text("LOC: " + str(lat) + "30\xB0" + ", " + str(lon) + "30\xB0", 25, height - 200)
    text("DPT: " + str(depth) + "m", 25, height - 150)
    
    # text("CID " + str(a) + "/" + str(b) + "/" + str(b) + "/" + str(c) + "/" + str(d) + "/" + str(e), 25, height - 25)
    text("CID " + str(cid) + "/" + str(pScale) + "/" + str(pSize) + "/" + str(pOffset), 25, height - 50)
    
    save("filename.png")
