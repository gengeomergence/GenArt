

def setup():
    size(2000, 2000)
    background(60)
    stroke(255)
    # strokeWeight(5)
    # translate(0, height/2)
    noiseDetail(10)
    
    for j in range(500, height-500): 
        pushMatrix()
        translate(0, j)
        for x in range(500, width-500):
            no = noise(x*0.002, j*0.002)
            n = map(no, 0, 1, -1, 1)
            n1 = map(noise(j*0.002, x*0.002), 0, 1, -1, 1)
            y = sin(radians(x*n))*tan(radians(x*n1))*50
            
            point(x, y)
            
        popMatrix()
    save("SinTanPer_17.png")
