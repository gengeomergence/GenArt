
def ncol(col, amt):
    
    r = red(col)
    g = green(col)
    b = blue(col)
    
    val = random(-amt, amt)
    
    nr = r+val
    ng = g+val
    nb = b+val
    ncol = color(nr, ng, nb)
    return ncol
