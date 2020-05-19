######################
## General Settings ##
######################

h = 2000 # Canvas Height
w = 2000 # Canvas Width

## offset Perlin Noise generation area, equal distances from edges
h_off = 500  # height offset
w_off = 500  # width offset

bgcolor = color(60, 60, 60)  # background color



########################################################################
##                          Colors                                    ##
########################################################################
##          This generator uses two colors per terrain area.          ##
## There are three terrain types: ocean (lowest), lowlands, highlands ##  
##         Ocean doesn't necissarily need to be actual oceans         ##  
##            I used coolors.co to generate these palettes            ##       
########################################################################
## Example Color Schemes:
    
## color scheme 1: Titan Like Colors:
highcolor1 = color(201, 162, 39)
highcolor2 = color(182, 145, 33)
lowcolor1 = color(164, 126, 27)
lowcolor2 = color(146, 108, 21)
oceancolor1 = color(128, 91, 16)
oceancolor2 = color(118, 82, 14)

## color scheme 2: tropical:
# highcolor1 = color(222, 239, 183)
# highcolor2 = color(200, 221, 150)
# lowcolor1 = color(115, 181, 95)
# lowcolor2 = color(114, 135, 74)
# oceancolor1 = color(101, 118, 63)
# oceancolor2 = color(86, 104, 44)

## color scheme 3: purple strange:
# highcolor1 = color(196, 181, 152)
# highcolor2 = color(201, 175, 154)
# lowcolor1 = color(182, 149, 140)
# lowcolor2 = color(144, 99, 99)
# oceancolor1 = color(123, 76, 66)
# oceancolor2 = color(97, 59, 50)

###########################
## Perlin Noise Settings ##
###########################

seeded = False  ## True to use a specific noise seed (for consistant patterns),
               ## False to use new pattern each run
seed_val = 1

noise_detail = 10 ## amount of detail in noise generation

sca = 0.002  ## noise scaling, lower values result in a closer view of terrain
mapLow = 0     ## maps noise values (from 0.0 to 1.0) to a more usable range 
mapHigh = 125  ## Note that min and max values dont seem to be reached often

## Rule Set: Noise is colored first based on if it is in a range of values 
## (high values - highland, mid values - lowland, low values - ocean), then 
## color variation for each region is determined by if the value is divisible
## by a certain value. This takes experimentation to get the look you want. the
## rules list below determines the divisible values

rules = [20, 20, 20]

## MAIN SKETCH ##

def setup():
    size(w, h)
    background(bgcolor)
    noiseDetail(noise_detail)
    if seeded == True:
        noiseSeed(seed_val)
    
    for i in range(w_off, width-w_off):
        for j in range(h_off, height-h_off):
            n = noise(i*sca, j*sca)
            m = round(map(n, 0.0, 1.0, mapLow, mapHigh))
            
            # Highlands
            if m >= 75:
                if m % rules[0] == 0:
                    stroke(highcolor1)
                else:
                    stroke(highcolor2)
            
            # Lowlands
            elif 75 > m >= 60:
                if m % rules[1] == 0:
                    stroke(lowcolor1)
                else:
                    stroke(lowcolor2)
            
            # oceans
            else:
                if m % rules[2] == 0:
                    stroke(oceancolor1)
                else:
                    stroke(oceancolor2)
            point(i, j)
                    
    
