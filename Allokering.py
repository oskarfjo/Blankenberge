import numpy as np

### Fiktiv kontrollerdata ###
X = 1
Y = 1
N = 1

dataCtrl = np.array([X, Y, N])

W1_data = 1      # Tunell thruster (Statisk)
W2_data = 1      # Swing-up thruster (Azimuth)
W3_data = 1      # Swing-up thruster (Azimuth)
W4_data = 1      # Akter thruster babord (Azimuth)
W5_data = 1      # Akter thruster styrbord (Azimuth)
dataThrusterAktiv = np.array([W1_data, W2_data, W3_data, W4_data, W5_data])
##############################


### Thruster momentarm [m] ###

l1x = 40
l2y = 0
l2x = 35
l3y = 0
l3x = 30
l4y = 4.5
l4x = 45
l5y = 4.5
l5x = 45

### Thruster aktivering; 0 = deaktivert ###

W1 = dataThrusterAktiv[0]
W2 = dataThrusterAktiv[1]
W3 = dataThrusterAktiv[2]
W4 = dataThrusterAktiv[3]
W5 = dataThrusterAktiv[4]

### Vessel parameters ###

KT0 = 0.4
rho = 1025


def vinkel(x, y):
    if x == 0:
        alpha = 0
    else:
        alpha = np.arctan(y / x)
    return alpha

def rps(x, y, propellerDiameter):
    T0 = np.sqrt(x**2 + y**2)
    return np.sign(T0) * np.sqrt((2 * np.abs(T0)) / ( rho * KT0 * (propellerDiameter ** 4)))

def pseudoinv(W, T):
    return np.linalg.inv(W) @ T.T @ np.linalg.inv(T @ np.linalg.inv(W) @ T.T)

def allokering(u):

    We = np.array([[W1, 0, 0, 0, 0, 0, 0, 0, 0],
                  [0, W2, 0, 0, 0, 0, 0, 0, 0],
                  [0, 0, W2, 0, 0, 0, 0, 0, 0],
                  [0, 0, 0, W3, 0, 0, 0, 0, 0],
                  [0, 0, 0, 0, W3, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, W4, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0, W4, 0, 0],
                  [0, 0, 0, 0, 0, 0, 0, W5, 0],
                  [0, 0, 0, 0, 0, 0, 0, 0, W5]])

    Te = np.array([[0, 1, 0, 1, 0, 1, 0, 1, 0],
                  [1, 0, 1, 0, 1, 0, 1, 0, 1],
                  [l1x, l2y, l2x, l3y, l3x, l4y, -l4x, -l5y, -l5x]])

    T_Wt = pseudoinv(We, Te)

    fe = T_Wt @ u

    print('fe: ', Te @ fe)

    RPS = np.array([rps(fe[0], 0, 1), 
                    rps(fe[1], fe[2], 1), 
                    rps(fe[3], fe[4], 1), 
                    rps(fe[5], fe[6], 1.5), 
                    rps(fe[7], fe[8], 1.5)]) # gir [u_w1, u_w2, u_w3, u_w4, u_w5]
    
    VINKEL = np.array([vinkel(fe[1], fe[2]), 
                       vinkel(fe[3], fe[4]), 
                       vinkel(fe[5], fe[6]), 
                       vinkel(fe[7], fe[8])]) # gir [r_w2, r_w3, r_w4 ,r_w5]

    return RPS, VINKEL

RPS, VINKEL = allokering(dataCtrl)

print('RPS: ', RPS)
print('ROT:', RPS)
