## Alien blue-green-purple Scheme ##
c1 = [color(22, 15, 41),
      color(36, 106, 115),
      color(54, 143, 139),
      color(243, 223, 193),
      color(221, 190, 168),
      color(219, 244, 167)]
## Wack ##
c2 = [color(178, 170, 142),
      color(12, 27, 51),
      color(122, 48, 108),
      color(3, 181, 170),
      color(219, 254, 135),
      color(235, 81, 96)]

## OrangeBlackRed ##
c3 = [color(164, 36, 59),
      color(216, 201, 155),
      color(216, 151, 60),
      color(189, 99, 47),
      color(39, 62, 71),
      color(5, 6, 9)]

## RedBluePurp ##
c4 = [color(14, 124, 123),
      color(23, 190, 187),
      color(212, 244, 221),
      color(214, 34, 70),
      color(75, 29, 63),
      color(2, 4, 2)]

## 5 ##
c5 = [color(51, 101, 138),
      color(134, 187, 216),
      color(117, 142, 79),
      color(246, 174, 45),
      color(242, 100, 25),
      color(236, 145, 146)]

def setup():
    
    size(1000, 1000)
    
    background(0)
    
    strokeWeight(3)
    stroke(0)
    noFill()
    
    noiseDetail(6)
    

    gasGiant(width/2, height/2, 800, 100, 900, height/2+200, c5)
    
    save("PlanetGen_19.png")
    
def gasGiant(xpos, ypos, dia, lcentx, lcenty, dcenty, colArray):
    
    loadPixels()
    
    rad = dia/2
    sca1 = 0.005
    
    maxRcir = ceil(sqrt(sq(rad)*2)*2)
    
    loff = dist(xpos, ypos, lcentx, lcenty)
    
    if (xpos + rad) < width and (xpos - rad) > 0:
        xstart = xpos - rad
        xend = xpos + rad
    elif (xpos - rad) < 0:
        xstart = 0
        xend = xpos + rad
    else:
        xstart = xpos - rad
        xend = width


    if (ypos + rad) < height and (ypos - rad) > 0:
        ystart = ypos - rad
        yend = ypos + rad
    elif (ypos - rad) < 0:
        ystart = 0
        yend = ypos + rad
    else:
        ystart = ypos - rad
        yend = height

    for i in range(xstart, xend):
        for j in range(ystart, yend):
            
            jsca = abs(dcenty - j)
            distl = dist(lcentx, lcenty, i, j)
            
            amt = map(distl, 0, rad + loff, 0, 1)
            sca2 = map(jsca, 0, rad, 0.03, 0.03)
            
            ni = noise(i*sca1, j*sca1)
            mi = map(ni, 0, 1, 1000, 1000+width)

            n = noise(mi*sca2, mi*sca2)
            m = map(n, 0, 1, 0, 170)
            
            if m < 10:
                col = lerpColor(colArray[0], colArray[1], amt)
            elif 20 <= m < 30:
                col = lerpColor(colArray[0], colArray[2], amt)
            elif 30 <= m < 40:
                col = lerpColor(colArray[0], colArray[3], amt)
            elif 40 <= m < 50:
                col = lerpColor(colArray[0], colArray[4], amt)
            elif 50 <= m < 60:
                col = lerpColor(colArray[0], colArray[5], amt)
            elif 60 <= m < 70:
                col = lerpColor(colArray[1], colArray[2], amt)
            elif 70 <= m < 80:
                col = lerpColor(colArray[1], colArray[3], amt)
            elif 80 <= m < 90:
                col = lerpColor(colArray[1], colArray[4], amt)
            elif 90 <= m < 100:
                col = lerpColor(colArray[1], colArray[5], amt)
            elif 100 <= m < 110:
                col = lerpColor(colArray[2], colArray[3], amt)
            elif 110 <= m < 120:
                col = lerpColor(colArray[2], colArray[4], amt)
            elif 120 <= m < 130:
                col = lerpColor(colArray[2], colArray[5], amt)
            elif 130 <= m < 140:
                col = lerpColor(colArray[3], colArray[4], amt)
            elif 150 <= m < 160:
                col = lerpColor(colArray[3], colArray[5], amt)
            else:
                col = lerpColor(colArray[4], colArray[5], amt)
            
            inde = (j*width) + i
            
            pixels[inde] = col
    
    updatePixels()
    
    for r in range(dia, maxRcir):
        circle(xpos, ypos, r)

    
