import numpy as np
from matplotlib import pyplot, cm, animation
from mpl_toolkits.mplot3d import Axes3D

'''
h_t+1 = - d[(H+h)*u]/dx
u_t+1 = - u * du/dx - g * dh/dx - bu + nu * d²u/dx²
'''

def d_dx(array, dx):
    return np.gradient(array, dx, axis=0)

def dh_dt(h, u, H=-1, dx=0.5):
    dhdt = d_dx((H+h)*u, dx)
    return dhdt

def du_dt(u, h, g=10, b=0.1, nu=1, dx=0.5):
    sum_1 = - u * d_dx(u, dx)
    sum_2 = - g * d_dx(h, dx)
    sum_3 = - b * u
    sum_4 = nu * d_dx(d_dx(u, dx), dx)
    return sum_1 + sum_2 + sum_3 + sum_4

def step(u, h, ax, X, Y, H, dt=1, i=0):
    new_u = du_dt(u, h) * dt + u
    new_h = dh_dt(h, u, H=H) * dt + h
    new_u[0, :] = 0.1
    new_u[-1, :] = 0
    new_h[0, :] = 0
    new_h[-1, :] = 0
    if i % 2 == 0:
        ax.plot_surface(X, Y, new_h[:], antialiased=True)
        ax.set_zlim(0, .1)
        pyplot.savefig('./here{}.png'.format(i))
        ax.clear()
    return new_u, new_h

def main():
    u = np.zeros(shape=(10, 10))
    u[0, :] = 0.1
    h = np.zeros(shape=(10, 10))
    h[0, :] = 0.1
    H = np.ones(shape=(10, 10))
    H = -1*H
    H[:, 5] = -0.5

    fig = pyplot.figure()
    ax = fig.gca(projection='3d')
    X, Y = np.meshgrid(np.linspace(0, 10, 10), np.linspace(0, 10, 10))
    ax.set_zlim(0, .1)

    for i in range(0, 60):
        u, h = step(u, h, ax, X, Y, H, dt=0.1, i=i)
    print(h)
    print(u)

    
    surf = ax.plot_surface(X, Y, h[:], antialiased=True)
    pyplot.show()


    

if __name__ == '__main__':
    main()
    


    
