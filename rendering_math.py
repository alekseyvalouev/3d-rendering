import math
import numpy as np

def convert_point(coords, camera, angle, w, h):

    """ coords: coordinates of object in 3D
    camera: coordinates of camera in 3D
    angle: angle of camera measured in radians 
    w: width of viewport
    h: height of viewport"""

    focal_distance = 1

    m1 = (
        [1, 0, 0],
        [0, math.cos(angle[0]), math.sin(angle[0])],
        [0, math.sin(angle[0]), math.cos(angle[0])]
    )

    m2 = (
        [math.cos(angle[1]), 0, -1*math.sin(angle[1])],
        [0, 1, 0],
        [math.sin(angle[1]), 0, math.cos(angle[1])]
    )

    m1 = np.dot(m1, m2)

    m2 = (
        [math.cos(angle[2]), math.sin(angle[2]), 0],
        [-1*math.sin(angle[2]), math.cos(angle[2]), 0],
        [0, 0, 1]
    )

    m1 = np.dot(m1, m2)

    m2 = (
        [coords[0] - camera[0]],
        [coords[1] - camera[1]],
        [coords[2] - camera[2]],
    )

    m1 = np.dot(m1, m2)

    try:
        x = focal_distance/m1[2][0]*m1[0][0]
        y = focal_distance/m1[2][0]*m1[1][0]

        u = w/2 * x + w/2
        v = h/2 * y + h/2
    except RuntimeWarning:
        return None

    return (u, v)
