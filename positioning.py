import numpy as np


def raw_view_position(width_in, height_in):
    puffer = 10
    flx = 480
    fuxmin = 250
    fuxmax = 400
    fux = np.maximum(fuxmin, np.minimum(width_in - flx - 3*puffer, fuxmax))

    # plot frame dimensions
    xop = puffer
    yop = puffer
    xlp = np.maximum(width_in-3*puffer-fux, np.minimum(flx, width_in-2*puffer))
    ylp = np.maximum(height_in - 2*puffer, 200)

    # pump one frame dimensions
    xopo = 2*puffer + xlp
    yopo = puffer
    xlpo = fux
    ylpo = (height_in - 3*puffer)/2

    # pump two frame dimensions
    xopt = xopo
    yopt = 2*puffer + ylpo
    xlpt = xlpo
    ylpt = ylpo

    return xop, yop, xlp, ylp, xopo, yopo, xlpo, ylpo, xopt, yopt, xlpt, ylpt


def raw_generate_position(width_in, height_in, furatio=[2, 1]):
    puffer = 10
    fux1min = 100
    fux1max = 1000
    fuy1min = 200
    fuy1max = 400
    fuy2min = 200
    fuy2max = 400
    fu3min = 300

    # overview canvas dimensions
    xp1 = puffer
    yp1 = puffer
    xl1 = np.maximum(fux1min, np.minimum(fux1max, width_in-3*puffer)/3)
    yl1 = np.maximum(fuy1min, np.minimum(fuy1max, (height_in-3*puffer)/2))

    # import settings canvas dimensions
    xp2 = puffer
    yp2 = 2*puffer + yl1
    xl2 = xl1
    yl2 = np.maximum(fuy2min, np.minimum(fuy2max, (height_in-3*puffer)/2))

    # draw canvas dimensions
    r3 = furatio[0]/furatio[1]
    xmax3 = np.maximum(fu3min, width_in - xl1 - 3*puffer)
    ymax3 = np.maximum(fu3min, height_in - 2*puffer)
    if r3 >= 1:  # wide
        yl3 = np.minimum(xmax3 / r3, ymax3)
        xl3 = yl3 * r3
        xp3 = xl1 + 2*puffer
        yp3 = np.maximum((ymax3 - yl3)/2 + puffer, puffer)
    else:  # tall
        xl3 = np.minimum(r3*ymax3, xmax3)
        yl3 = xl3 / r3
        yp3 = puffer
        xp3 = np.maximum((xmax3 - xl3)/2 + xl1 + 2*puffer, xl1 + 2*puffer)
        #print(xl1)
        #print((xmax3 - xl3)/2 - xl1 + 2*puffer)
        #print(xl1 + 2*puffer)
    return xp1, yp1, xl1, yl1, xp2, yp2, xl2, yl2, xp3, yp3, xl3, yl3
