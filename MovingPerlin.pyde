sca = 0.003
step = 1
ma = 1000


def setup():
    
    size(1000, 1000)
    background(255)
    
    noiseDetail(6)
    
def draw():
    global ma, step, sca
    
    background(0)

    loadPixels()
    
    
    for x in range(width):
        for y in range(height):
            nx = noise(x*sca, y*sca)
            ny = noise(y*sca, x*sca)
            
            mx = map(nx, 0, 1, 0, ma)
            my = map(ny, 0, 1, 0, ma)
        
            n = noise(mx*sca, my*sca)
            
            col = color(255*n)    
                        
            i = (y*width) + x
                
            pixels[i] = col
    
    updatePixels()

    ma += 5
    
    # saveFrame("boilingPerlin/###.png")

            
