def perlinShape(sizee, step, sca, mapscale):
    for i in range(sizee/2, sizee + step, step):
        for j in range(sizee/2, sizee + step, step):
            
            ni = noise(i*sca, j*sca)
            nj = noise(j*sca, i*sca)
            mi = round(map(ni, 0, 1, -mapscale, mapscale))
            mj = round(map(nj, 0, 1, -mapscale, mapscale))
            # if mi > 100 or mi < -100 or mj > 100 or mj < -100 :
            #     stroke(8, 126, 139)

            # else:
            #     stroke(255, 90, 95)
            nvec = PVector(mi, mj)
            pos = PVector(i, j)
            pos.add(nvec)
            point(pos.x, pos.y)

def setup():
    size(3000, 3000)
    background(60)
    stroke(8, 126, 139)
    strokeWeight(1)
    noFill()
    rectMode(CENTER)
    noiseDetail(5)
    blendMode(ADD)
    
    translate(-750, -750)

    perlinShape(3000, 2, 0.002, 800)

    print("done")
    save("LargePerlinShape_19.png")
