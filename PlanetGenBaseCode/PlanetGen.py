
def gasGiant(xpos, ypos, dia, lcentx, lcenty, dcenty, colArray, scaleMin, scaleMax):
    
    fill(255)
    noStroke()
    circle(xpos, ypos, dia)
    
    loadPixels()
    
    rad = dia/2
    sca1 = 0.005
    
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
            
            inde = (j*width) + i
            if pixels[inde] == -1:
                jsca = abs(dcenty - j)
                distl = dist(lcentx, lcenty, i, j)
                
                amt = map(distl, 0, rad + loff, 0, 1)
                sca2 = map(jsca, 0, rad, scaleMin, scaleMax)
                
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
                
                
                
                pixels[inde] = col
    
    updatePixels()
