
def atmoGlow(xloc, yloc, dia, col, amount):
    
    noFill()
    strokeWeight(2)
    
    re = red(col)
    gr = green(col)
    bl = blue(col)
    
    glow = amount

    for r in range(dia-1, dia + amount):
        stroke(re, gr, bl, glow)
        
        circle(xloc, yloc, r)
        glow -= 1
