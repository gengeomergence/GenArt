import datetime

timestamp = datetime.datetime.now().strftime('%y-%m-%d')

def pCreature(tSize, step, sca, offset):
    
    for i in range(-tSize, tSize + step, step):
        for j in range(-tSize, tSize + step, step):
            
            x = map(noise(i*sca, j*sca), 0, 1, -offset, offset)
            y = map(noise(j*sca, i*sca), 0, 1, -offset, offset)
            
            point(x, y)

def setup():
    
    size(2000, 2000)
    background(247, 243, 227)
    strokeWeight(1)
    
    for xval in range(600, width, 750):
        for yval in range(600, height, 750):
            
            noiseSeed(int(random(100000)))
            pushMatrix()
            translate(xval, yval)
            pCreature(500, 1, 0.002, 500)
            popMatrix()
    

    textSize(30)
    fill(0)
    text("EXPEDITION DATE:" + " " + timestamp, 100, height - 150)
    lat = random(10000)
    lon = random(10000)
    text("LOCATION: " + str(lat) + "30\xB0" + ", " + str(lon) + "30\xB0", 100, height - 100)
    text("EF-109W", 100, 100)
    text("716 Tau Cd", 100, 150)
    text("OCEAN/COG-5/NR/UNIQUE", 100, 200)
    save("EXPEDITION_FINDINGS_7.png")
