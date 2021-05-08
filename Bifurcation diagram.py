Python 3.9.4 (tags/v3.9.4:1f2e308, Apr  6 2021, 13:40:21) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import numpy as np
import matplotlib.pyplot as plt

def logistic(n, r, x0):
    xn = []
    for i in range(1,n+1):
        x0 = r*x0*(1-x0)
        xn += [x0]
    xn = np.array(xn)
    return xn
        
def bifurcation(n, k, rmin, rmax, rstep, x0):
    plt.figure(figsize=(15,8))
    for r in np.arange(rmin, rmax, rstep):
        traj = []
        traj.append(logistic(n, r, x0))
        traj = np.array(traj)
        R = r*np.ones([1, n])
        plt.scatter(R[:, k:], traj[:, k:], s = 0.001, color = 'black')
    plt.show()

bifurcation(1000, 500, 2.4, 4, 0.0005, 0.2)