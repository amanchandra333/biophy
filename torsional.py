import  numpy as np
from numpy import linalg as LA
import math

with open('data.txt') as f:
    lines = f.readlines()

data, phi, psi, omega = ([] for i in range(4))

for line in lines:
    val = (line.rstrip()).split(" ")
    if len(val) != 4:
        continue
    data.append([val[0], np.array([float(val[1]), float(val[2]), float(val[3])])])

for i in range(0, len(data) - 3):
    bl1 = data[i][1] - data[i+1][1]
    bl2 = data[i+1][1] - data[i+2][1]
    bl3 = data[i+2][1] - data[i+3][1]

    theta = math.acos(np.dot(np.cross(bl1,bl2), np.cross(bl2, bl3))/
                (LA.norm(np.cross(bl1,bl2))*LA.norm(np.cross(bl2,bl3))))

    atom = data[i][0]
    if atom == 'N':
        psi.append(theta)
    elif atom == 'CA':
        phi.append(theta)
    elif atom == 'C':
        omega.append(theta)
    else:
        continue
