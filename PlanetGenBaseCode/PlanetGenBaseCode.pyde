from random import choice
from PlanetGen import gasGiant
from AtmoGlow import atmoGlow
from Background import nebU
from Colors import c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, backc1, backc2

atmo1 = color(36, 106, 115)  # Blueish
atmo2 = color(122, 48, 108)  # Purple
atmo3 = color(216, 201, 155) # Pale Yellow
atmo4 = color(212, 244, 221) # Light Blue/green
atmo5 = color(242, 100, 25)  # Vibrant Orange
atmo6 = color(255, 51, 102)  # Vibrant Pink
atmo7 = color(244, 243, 238) # White
atmo8 = color(41, 112, 69)   # Green
atmo9 = color(238, 241, 239) # White

## VALUES FOR SCALING ##
# [0.001, 0.01], [0.001, 0.001], [0.008, 0.008], [0.001, 0.005]

scmin = 0.001
scmax = 0.002

# pcs = [c1, c2, c3, c4, c5, c6, c7, c8, c9]
# atmos = [atmo1, atmo2, atmo3, atmo4, atmo5, atmo6, atmo7, atmo8, atmo9]
# shad = 200

def setup():
    global shad
    
    size(2000, 2000)
    background(0)
    noiseDetail(5) ## RECCOMEND 5-10 ##
    
    nebU(backc1, backc2)
    
    # pc1 = choice(pcs)
    # pc2 = choice(pcs)
    # at1 = choice(atmos)
    # at2 = choice(atmos)
    
    ## gasGiant(center_x, center_y, diameter, gradientStart_x, gradientStart_y, ScaleGradientStart_y, ColorScheme, scaleMin, scaleMax)
    
    gasGiant(1000, 1000, 1800, 400, 1600, height/2, c11, scmin, scmax)
    atmoGlow(1000, 1000, 1800, atmo9, 50)
    
    # pushStyle()
    # strokeWeight(1)
    # noStroke()
    # fill(0, 0, 0, 5)
    # for _ in range(50):
    #     circle(900, 1400, shad)
    #     shad -=1
    # popStyle()
           

    # save("AGiantAndHerSon_8.png")
