
import numpy as np


X = 1
Y = 1
N = 1

data = np.array([X, Y, N])


def vinkel(x, y):
    
    if x == 0:
        alpha = 0
    else:
        alpha = np.arctan(y / x)
    return alpha

def kraft(x, y):
    To = np.sqrt(x**2 + y**2)
    return np.sign(To) * np.sqrt((2 * np.abs(To)) / ( 1025 * 0.4 * (0.08 ** 4)))


def allokering(u):

    l1y = 40
    l2y = 35
    l3y = 30
    l4x = 4.5
    l4y = 45
    l5x = 4.5
    l5y = 45

    We = np.eye(9)


    Te = np.array([[0, 1, 0, 1, 0, 1, 0, 1, 0],
                  [1, 0, 1, 0, 1, 0, 1, 0, 1],
                  [l1y, 0, l2y, 0, l3y, l4x, -l4y, -l5x, -l5y]])

    T_Wt = np.linalg.inv(We) @ Te.T @ np.linalg.inv(Te @ np.linalg.inv(We) @ Te.T)

    fe = T_Wt @ u

    rps = np.array([kraft(fe[0], 0), kraft(fe[1], fe[2]), kraft(fe[3], fe[4]), kraft(fe[5], fe[6]), kraft(fe[7], fe[8])]) # gir [u1, u2, u3, u4, u5]
    rot = np.array([vinkel(fe[1], fe[2]), vinkel(fe[3], fe[4]), vinkel(fe[5], fe[6]), vinkel(fe[7], fe[8])]) # git [r2, r3, r4 ,r5]

    return rps, rot

rps, rot = allokering(data)

print('RPS: ', rps)
print('ROT:', rot)