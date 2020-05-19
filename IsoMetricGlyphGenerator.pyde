import random

######################
## General Settings ##
######################

h = 2000 # Canvas height
w = 2000 # Canvas Width

h_off = 200  # Offsets where glyphs are drawn, distance from
w_off = 200  # canvas edges

spacing = 200  # Space in between glyphs

thickness = 20  # Stroke Weight

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

sideLength = 25  ## Half side length of glyph line
minLines = 2   # Minimum number of lines per glyph
maxLines = 10  # Maximum number of lines per glyph

## Lines of an IsoMetric Cube ##

l1 = (0, 0, -sideLength*sqrt(3), -sideLength)
l2 = (-sideLength*sqrt(3), -sideLength, 0, -2*sideLength)
l3 = (0, -2*sideLength, sideLength*sqrt(3), -sideLength)
l4 = (sideLength*sqrt(3), -sideLength, 0, 0)
l5 = (sideLength*sqrt(3), -sideLength, sideLength*sqrt(3), sideLength)
l6 = (sideLength*sqrt(3), sideLength, 0, 2*sideLength)
l7 = (0, 2*sideLength, -sideLength*sqrt(3), sideLength)
l8 = (0, 2*sideLength, 0, 0)
l9 = (-sideLength*sqrt(3), -sideLength, -sideLength*sqrt(3), sideLength)

opts = [l1, l2, l3, l4, l5, l6, l7, l8, l9]

#################
## Main Sketch ##
#################

def setup():
    size(h, w)
    background(bgcolor)
    strokeWeight(thickness)
    stroke(glyphcol)
    frameRate(frame_rate)
    
def draw():
    background(bgcolor)
    
    for i in range(w_off, width-w_off + spacing, spacing):
        for j in range(h_off, height-h_off + spacing, spacing):
            num = random.randrange(minLines, maxLines, 1)
            pushMatrix()
            translate(i, j)
            for val in range(num):
                line(*random.choice(opts))
            popMatrix()
    # save("IsoGlyph_1.png")
    
