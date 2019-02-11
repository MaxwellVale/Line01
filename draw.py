from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    if x0 < x1 or x0 == x1 and y0 < y1:
        nx0 = x0
        nx1 = x1
        ny0 = y0
        ny1 = y1
    else:
        nx0 = x1
        nx1 = x0
        ny0 = y1
        ny1 = y0
    x = nx0
    y = ny0
    A = ny1 - ny0 # change in y
    B = nx0 - nx1 # negative change in x
    if nx0 == nx1 or (ny1 - ny0) / (nx1 - nx0) >=1:
        d = A + 2 * B
        while y <= ny1:
            plot(screen, color, x, y)
            if d < 0:
                x += 1
                d += 2 * A
            y += 1
            d += 2 * B
    elif (ny1 - ny0) / (nx1 - nx0) >= 0 and (ny1 - ny0) / (nx1 - nx0) < 1:
        d = 2 * A + B
        while x <= nx1:
            plot(screen, color, x, y)
            if d > 0:
                y += 1
                d += 2 * B
            x += 1
            d += 2 * A
    elif (ny1 - ny0) / (nx1 - nx0) <= 0 and (ny1 - ny0) / (nx1 - nx0) > -1:
        d = 2 * A - B
        while x <= nx1:
            plot(screen, color, x, y)
            if d < 0:
                y -= 1
                d -= 2 * B
            x += 1
            d += 2 * A
    else:
        #print (">= -1")
        #print ("Slope = " + str((ny1 - ny0) / (nx1 - nx0)))
        d = 2 * B - A
        while y >= ny1:
            #print ("(" + str(x) + ',' + str(y) + ")")
            plot(screen, color, x, y)
            if d > 0:
                x += 1
                d += 2 * A
            y -= 1
            d -= 2 * B
