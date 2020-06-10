
c1 = color(22, 15, 41)
c2 = color(36, 106, 115)

c3 = color(54, 143, 139)
c4 = color(243, 223, 193)

c5 = color(221, 190, 168)
c6 = color(219, 244, 167)


sca  = 0.003
# sca2 = 0.03
g = 1
rad = 3000
grad = 200


def setup():
    global rad, grad
    size(2000, 2000)
    # fullScreen()
    
    background(0)
    noFill()

    noiseDetail(5)

    loadPixels()
    
    for y in range(0, 2000):
        for x in range(0, 2000):
            
            d = dist(1250, 1250, x, y)
            
            amt = map(d, 0, 1000, 0, 1)
            
            sca2 = map(y, 250, 1500, 0.005, 0.08)
            
            nx = noise(x*sca, y*sca)
            ny = noise(x*sca, y*sca)
            
            mx = map(nx, 0, 1, 1000, 1000+width)
            my = map(ny, 0, 1, 1000, 1000+height)
            
            n = noise(mx*sca2, my*sca2)
            m = map(n, 0, 1, 0, 170)
            
            
            if m < 10:
                col = lerpColor(c1, c2, amt)
            elif 20 <= m < 30:
                col = lerpColor(c1, c3, amt)
            elif 30 <= m < 40:
                col = lerpColor(c1, c4, amt)
            elif 40 <= m < 50:
                col = lerpColor(c1, c5, amt)
            elif 50 <= m < 60:
                col = lerpColor(c1, c6, amt)
            elif 60 <= m < 70:
                col = lerpColor(c2, c3, amt)
            elif 70 <= m < 80:
                col = lerpColor(c2, c4, amt)
            elif 80 <= m < 90:
                col = lerpColor(c2, c5, amt)
            elif 90 <= m < 100:
                col = lerpColor(c2, c6, amt)
            elif 100 <= m < 110:
                col = lerpColor(c3, c4, amt)
            elif 110 <= m < 120:
                col = lerpColor(c3, c5, amt)
            elif 120 <= m < 130:
                col = lerpColor(c3, c6, amt)
            elif 130 <= m < 140:
                col = lerpColor(c4, c5, amt)
            elif 150 <= m < 160:
                col = lerpColor(c4, c6, amt)
            else:
                col = lerpColor(c5, c6, amt)
            
            i = (y*width)+x
            
            pixels[i] = col
        
    updatePixels()
    strokeWeight(5)
    for r in range(1500, 5000):
        circle(width/2, height/2, r)

    for r in range(1500, 1700):
        stroke(grad)
        circle(width/2, height/2, r)
        grad -= 1

    # save("PerlinLerpVariableScale_3.png")
