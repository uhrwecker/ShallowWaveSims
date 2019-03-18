import swe.simulator.numeric_handler as nh
import numpy as np

class ShallowWaveSimulator(nh.GeneralNumericHandler):
    '''
    Class that handles the implementation of the
    shallow wave equations, thus handling the simulation,
    NOT implementing the simulation (starting criteria/ending criteria etc)
    '''
    def __init__(self, dx=1, dy=1, dt=0.1, g=10, b=0.1, nu=1):
        super().__init__()

        self.dx = dx
        self.dy = dy
        self.dt = dt

        self.g = g
        self.b = b
        self.nu = nu

    def dh_dt(self, h, u, v, H):
        '''
        form:
        dh/dt = - d/dx[(H+h)*u] - d/dy[(H+h)*v]
        '''
        dhdt = - self.d_dx((H+h)*u, self.dx) - self.d_dy((H+h)*v, self.dy)
        return dhdt

    def du_dt(self, h, u, v):
        '''
        form:
        du/dt = -u du/dx - v du/dy - g dh/dx - b u + nu * (d²u/dx² + d²u/dy²)
              = sum_a + sum_b + sum_c + sum_d + sum_e1 + sum_e2
        '''
        sum_a = - u * self.d_dx(u, self.dx)
        sum_b = - v * self.d_dy(u, self.dy)
        sum_c = - self.g * self.d_dx(h, self.dx)
        sum_d = - self.b * u
        sum_e1 = self.nu * self.d_dx(self.d_dx(u, self.dx), self.dx)
        sum_e2 = self.nu * self.d_dy(self.d_dy(u, self.dy), self.dy)
        dudt = sum_a + sum_b + sum_c + sum_d + sum_e1 + sum_e2
        del sum_a, sum_b, sum_c, sum_d, sum_e1, sum_e2
        return dudt

    def dv_dt(self, h, u, v):
        '''
        form:
        dv/dt = -u dv/dx - v dv/dy - g dh/dx - b v + nu * (d²u/dx² + d²u/dy²)
              = sum_a + sum_b + sum_c + sum_d + sum_e1 + sum_e2
        '''
        sum_a = - u * self.d_dx(v, self.dx)
        sum_b = - v * self.d_dy(v, self.dy)
        sum_c = - self.g * self.d_dx(h, self.dx)
        sum_d = - self.b * v
        sum_e1 = self.nu * self.d_dx(self.d_dx(u, self.dx), self.dx)
        sum_e2 = self.nu * self.d_dy(self.d_dy(u, self.dy), self.dy)
        dudt = sum_a + sum_b + sum_c + sum_d + sum_e1 + sum_e2
        del sum_a, sum_b, sum_c, sum_d, sum_e1, sum_e2
        return dudt

    def step(self, h, u, v, H):
        new_h = self.dh_dt(h, u, v, H) * self.dt + h
        new_u = self.du_dt(h, u, v) * self.dt + h
        new_v = self.dv_dt(h, u, v) * self.dt + h

        return new_h, new_u, new_v

def main():
    swe = ShallowWaveSimulator()
    u = np.ones(shape=(5, 5))
    v = np.ones(shape=(5, 5))
    h = np.ones(shape=(5, 5))
    H = -1
    print(swe.step(h, u, v, H))

if __name__ == '__main__':
    main()
    
        

        
