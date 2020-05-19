import random

######################
## General Settings ##
######################

h = 2000 # Canvas height
w = 2000 # Canvas Width

h_off = 200  # Offsets where glyphs are drawn, distance from
w_off = 200  # canvas edges

x_spacing = 100  # Space between glyphs x-axis
y_spacing = 200  # space between glyphs y-axis

thickness = 4  # Stroke Weight

glyphcol = color(238, 66, 102)  # Glyph Color
bgcolor = color(84, 13, 110)  # Background Color
blending = True  # if true, overlaping lines create a nice transparancy effect

animate = False  # Logic for animations (True will animate glyphs)
frame_rate = 60  # Frame rate if animated, set to 60 if no animation to remove 
                 # slight delay, for animations set frame rate between 1 and 5

if animate == False:
    noLoop()

####################
## Glyph Settings ##
####################

side_length = 100  # side length of glyph lines
minimum_lines = 2  # minimum number of lines per glyph
maximum_lines = 5  # maximum number of lines per glyph
circle_diam = 15  # circle diameter 

def squareGlyph(linelength, minlines, maxlines, cirDiam):
    either = [0, linelength/2]
    num = random.randrange(minlines, maxlines, 1)
    for i in range(num):
        a = random.choice(either)
        b = random.choice(either)
        c = random.choice(either)
        d = random.choice(either)
        if (a, b) == (c, d):
            circle(a, b, cirDiam)
        else:
            line(a, b, c, d)

def setup():
    size(w, h)
    background(bgcolor)
    stroke(glyphcol)
    strokeWeight(thickness)
    fill(glyphcol)
    if blending == True:
        blendMode(ADD)
    frameRate(frame_rate)
    
def draw():
    background(bgcolor)
    for i in range(w_off, width-w_off + x_spacing, x_spacing):
        for j in range(h_off, height-h_off + y_spacing, y_spacing):
            pushMatrix()
            translate(i, j)
            squareGlyph(side_length, minimum_lines, maximum_lines, circle_diam)
            popMatrix()
    
