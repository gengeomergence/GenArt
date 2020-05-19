import random

######################
## General Settings ##
######################

h = 2000 # Canvas height
w = 2000 # Canvas Width

h_off = 200  # Offsets where glyphs are drawn, distance from
w_off = 200  # canvas edges

x_spacing = 200 
y_spacing = 200 # Space in between glyphs

thickness = 5  # Stroke Weight

glyphcol = color(238, 66, 102)  # Glyph Color
bgcolor = color(84, 13, 110)  # Background Color

animate = False  # Logic for animations (True will animate glyphs)
frame_rate = 30  # Frame rate if animated, set to 60 if no animation to remove 
                 # slight delay

if animate == False:
    noLoop()
    
#############################################
### Glyph Specific Setup...Things to Edit ###
#############################################

sideLength = 25  ## side length of glyph line
minLines = 2   # Minimum number of lines per glyph
maxLines = 5  # Maximum number of lines per glyph

### Points on a curve...Don't edit these ###

p1 = (0, 0)
p2 = (0, -2*sideLength)
p3 = (0, 2*sideLength)
p4 = (sideLength*sqrt(3), sideLength)
p5 = (sideLength*sqrt(3), -sideLength)
p6 = (-sideLength*sqrt(3), sideLength)
p7 = (-sideLength*sqrt(3), -sideLength)
opts = [p1, p2, p3, p4, p5, p6, p7]

##########
## MAIN ##
##########

def setup():
    size(w, h)
    background(bgcolor)
    stroke(glyphcol)
    noFill()
    strokeWeight(thickness)
    for i in range(w_off, width-w_off + x_spacing, x_spacing):
        for j in range(h_off, height-h_off + y_spacing, y_spacing):
            num = random.randrange(minLines, maxLines, 1)
            pushMatrix()
            translate(i, j)
            for val in range(num):
                ans = (random.choice(opts) + random.choice(opts) + random.choice(opts) + random.choice(opts))
                bezier(*ans)
            popMatrix()
