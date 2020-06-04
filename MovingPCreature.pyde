sca = 0.003
off = 1000
mi = 0
ma = 400

white = color(255)

def setup():
    
    size(1000, 1000)
    
    stroke(255)
    
    noiseDetail(6)
    

def draw():
    global mi, ma
    background(0)
    loadPixels()
    
    for x in range(mi, ma):
        for y in range(mi, ma):
            nx = noise(x*sca, y*sca)
            ny = noise(y*sca, x*sca)
            
            mx = floor(map(nx, 0, 1, 0, off))
            my = floor(map(ny, 0, 1, 0, off))
            
            i = (my*width) + mx
            
            pixels[i] = white
    
    updatePixels()
    
    mi += 5
    ma += 5
    # saveFrame("movingPCREATURE/###.png")
    
