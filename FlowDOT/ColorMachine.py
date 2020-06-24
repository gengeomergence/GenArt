
def colMachine(m, colArray, amt):
    
    if m < 10:
        col = lerpColor(colArray[0], colArray[1], amt)
    elif 20 <= m < 30:
        col = lerpColor(colArray[0], colArray[2], amt)
    elif 30 <= m < 40:
        col = lerpColor(colArray[0], colArray[3], amt)
    elif 40 <= m < 50:
        col = lerpColor(colArray[0], colArray[4], amt)
    elif 50 <= m < 60:
        col = lerpColor(colArray[0], colArray[5], amt)
    elif 60 <= m < 70:
        col = lerpColor(colArray[1], colArray[2], amt)
    elif 70 <= m < 80:
        col = lerpColor(colArray[1], colArray[3], amt)
    elif 80 <= m < 90:
        col = lerpColor(colArray[1], colArray[4], amt)
    elif 90 <= m < 100:
        col = lerpColor(colArray[1], colArray[5], amt)
    elif 100 <= m < 110:
        col = lerpColor(colArray[2], colArray[3], amt)
    elif 110 <= m < 120:
        col = lerpColor(colArray[2], colArray[4], amt)
    elif 120 <= m < 130:
        col = lerpColor(colArray[2], colArray[5], amt)
    elif 130 <= m < 140:
        col = lerpColor(colArray[3], colArray[4], amt)
    elif 150 <= m < 160:
        col = lerpColor(colArray[3], colArray[5], amt)
    else:
        col = lerpColor(colArray[4], colArray[5], amt)
        
    return col
