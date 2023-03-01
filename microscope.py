import math



def dist(coords, base):
    dsquared = (coords[0]-base[0])**2 + (coords[1]-base[1])**2 + (coords[2]-base[2])**2
    return math.sqrt(dsquared)

def closeDist(coords, base, vec):
    x = coords[0] - base[0]
    y = coords[1] - base[1]
    z = coords[2] - base[2]
    
    a = x
    if a > vec[0]:
        a = vec[0]
    elif a < 0:
        a = 0
        
    b = y
    if b > vec[1]:
        b = vec[1]
    elif b < 0:
        b = 0
        
    c = z
    if c > vec[2]:
        c = vec[2]
    elif c < 0:
        c = 0
        
    dsquared = (x-a)**2 + (y-b)**2 + (z-c)**2
    return math.sqrt(dsquared)




