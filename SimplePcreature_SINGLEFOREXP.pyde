import datetime
from random import choice

timestamp = datetime.datetime.now().strftime('%y-%m-%d')

def pCreature(tSize, step, sca, offset):
    
    for i in range(-tSize, tSize + step, step):
        for j in range(-tSize, tSize + step, step):
            
            x = round(map(noise(i*sca, j*sca), 0, 1, -offset, offset))
            y = round(map(noise(j*sca, i*sca), 0, 1, -offset, offset))

            point(x, y)

def setup():
    
    size(2000, 2000)
    background(30)

    for x in range(width):
        for y in range(height):
            col = random(100)
            stroke(col)
            point(x, y)
    

    stroke(30)
    strokeWeight(1)
    blendMode(ADD)
    
    noiseDetail(10)
    a = int(random(100000))
    noiseSeed(a)
    print(a)
    
    pushMatrix()
    translate(width/2 + 100, height/2 + 100)
    pCreature(1000, 1, 0.002, 900)
    popMatrix()
    
    textSize(30)
    fill(255)
    
    text("EXPEDITION DATE:" + " " + timestamp, 100, height - 150)
    lat = random(10000)
    lon = random(10000)
    depth = floor(random(100000))
    text("LOCATION: " + str(lat) + "30\xB0" + ", " + str(lon) + "30\xB0", 100, height - 100)
    
    text("DEPTH: " + str(depth) + "m", 100, height - 50)
    text("EF-109W", 100, 100)
    text("716 Tau Cd", 100, 150)
    resp = ["NR", "PR", "HR"]
    cogs = [1, 2, 3, 4, 5]

    
    # text("OCEAN//UNIQUE", 100, 200)
    text("CID " + str(a), 1750, height - 150)
    text("COG" + str(choice(cogs)) + " / " + choice(resp), 1750, height-100)
    text("WHOT", 1750, height-50)
    
    save("DETAIL_14.png")
