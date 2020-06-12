from random import choice

def nebU(bc1, bc2):

    chance = []
    stars = [color(214, 255, 246), color(248, 182, 181), color(153, 219, 255)]

    for _ in range(1000):
        chance.append(0)
    chance.append(1)

    loadPixels()

    for x in range(width):
        for y in range(height):
            
            i = (y*width)+x
            
            cha = choice(chance)
            
            n = noise(x*0.003, y*0.003)
            
            if cha == 1:
                
                coll = choice(stars)
                
            else:
                coll = lerpColor(bc1, bc2, n)
                
            pixels[i] = coll
        
    updatePixels()
