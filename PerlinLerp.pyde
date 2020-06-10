
c1 = color(22, 15, 41)
c2 = color(36, 106, 115)

c3 = color(54, 143, 139)
c4 = color(243, 223, 193)

c5 = color(221, 190, 168)
c6 = color(219, 244, 167)


sca  = 0.003
sca2 = 0.05
g = 1


def setup():
    
    size(2000, 2000)
    # fullScreen()
    
    noiseDetail(10)
    pixelDensity(displayDensity(2))

    loadPixels()
    
    for x in range(width):
        for y in range(height):
        
            nx = noise(x*sca, y*sca)
            
            ny = noise(x*sca, y*sca)
            
            mx = map(nx, 0, 1, 0, width)
            my = map(ny, 0, 1, 0, height)
            
            n = noise(mx*sca2, my*sca2)
            
            m = map(n, 0, 1, 0, 170)
            
            # n = map(nn, 0, 1, 0, 0.1)

            if m < 10:
                col = lerpColor(c1, c2, nx*ny)
            elif 20 <= m < 30:
                col = lerpColor(c1, c3, nx*ny)
            elif 30 <= m < 40:
                col = lerpColor(c1, c4, nx*ny)
            elif 40 <= m < 50:
                col = lerpColor(c1, c5, nx*ny)
            elif 50 <= m < 60:
                col = lerpColor(c1, c6, nx*ny)
            elif 60 <= m < 70:
                col = lerpColor(c2, c3, nx*ny)
            elif 70 <= m < 80:
                col = lerpColor(c2, c4, nx*ny)
            elif 80 <= m < 90:
                col = lerpColor(c2, c5, nx*ny)
            elif 90 <= m < 100:
                col = lerpColor(c2, c6, nx*ny)
            elif 100 <= m < 110:
                col = lerpColor(c3, c4, nx*ny)
            elif 110 <= m < 120:
                col = lerpColor(c3, c5, nx*ny)
            elif 120 <= m < 130:
                col = lerpColor(c3, c6, nx*ny)
            elif 130 <= m < 140:
                col = lerpColor(c4, c5, nx*ny)
            elif 150 <= m < 160:
                col = lerpColor(c4, c6, nx*ny)
            else:
                col = lerpColor(c5, c6, nx*ny)
            i = (y*width)+x
            
            pixels[i] = col
        
    updatePixels()
    
    # save("UberREsPerlin_31_LARGE.png")
