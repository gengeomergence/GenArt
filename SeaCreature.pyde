
from random import choice, randint

def pCreature(tSize, step, sca, offset):
    
    for i in range(0, tSize + step, step):
        for j in range(0, tSize + step, step):
            
            x = round(map(noise(i*sca, j*sca), 0, 1, -offset, offset))
            y = round(map(noise(j*sca, i*sca), 0, 1, -offset, offset))

            point(x, y)

def setup():

    size(1000, 1000)
    background(0)

    for x in range(width):
        for y in range(height):
            col = random(50)
            stroke(col)
            point(x, y)
    
    stroke(50)
    strokeWeight(1)
    blendMode(ADD)
    
    noiseDetail(10)
    a = int(random(100000))
    noiseSeed(a)
    
    pushMatrix()
    translate(width/2 - 100, height/2 - 100)
    pCreature(250, 1, 0.003, 500)
    popMatrix()
    
    b = int(random(100000))
    noiseSeed(b)
    
    pushMatrix()
    translate(width/2 - 50, height/2 - 50)
    pCreature(250, 1, 0.003, 500)
    popMatrix()
    
    b = int(random(100000))
    noiseSeed(b)
    
    pushMatrix()
    translate(width/2, height/2)
    pCreature(250, 1, 0.003, 500)
    popMatrix()
    
    b = int(random(100000))
    noiseSeed(b)
    
    pushMatrix()
    translate(width/2 + 50, height/2 + 50)
    pCreature(250, 1, 0.003, 500)
    popMatrix()
    
    c = int(random(100000))
    noiseSeed(c)
    
    pushMatrix()
    translate(width/2 + 100, height/2 + 100)
    pCreature(250, 1, 0.003, 500)
    popMatrix()
    
    textSize(14)
    fill(255)
    
    m = ["01", "02", "03", "04", "05", "06", "07", "08", "09", 10, 11, 12]
    d = ["01", "02", "03", "04", "05", "06", "07", "08", "09"]
    for da in range(10, 32):
        d.append(da)
    
    y = randint(30, 40)
    lat = round(random(10000), 2)
    lon = round(random(10000), 2)
    depth = round(random(100000), 1)
    lcap = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
            "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    llow = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", 
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    nid = floor(random(900))
    resp = ["NR", "PR", "HR"]
    
    text("COG" + str(int(random(10))) + " / " + choice(resp), 25, height-275)
    text("WHOT", 25, height-250)
    
    text("EF: " + str(choice(lcap)) + str(choice(lcap)) + str(choice(lcap)) + "-" + str(nid) + str(choice(llow)), 25, height - 200)
    text("SYS: " + str(nid) + " " + str(choice(lcap)) + str(choice(llow)) + str(choice(llow)) + " " + str(choice(lcap)) + str(choice(llow)), 25, height - 175)
    
    text("DOE: " + str(choice(m)) + "." + str(choice(d)) + "." + str(y), 25, height - 125)
    text("LOC: " + str(lat) + "30\xB0" + ", " + str(lon) + "30\xB0", 25, height - 100)
    text("DPT: " + str(depth) + "m", 25, height - 75)
    
    text("CID " + str(a) + ", " + str(b) + ", " + str(b), 25, height - 25)
    
    save("Findings_Report_iter_21.png")
