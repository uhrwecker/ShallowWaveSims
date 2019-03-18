import numpy as np

class InitialCondition():
    '''
    Base Class that will be used to setup the initial conditions for
    h, u, v, and H
    '''
    def __init__(self, nx, ny):
        self.nx = nx
        self.ny = ny
        
        self.array = self._setup_array() #will be set in sub_class

    def get_array(self):
        assert type(self.array) == type(np.array([])), 'array must be numpy.array!'
        assert self.array.shape == (self.nx, self.ny), 'initial condition does not properly setup the right array shape'
        
        return self.array

    def _setup_array(self):
        '''
        MUST be implemented in sub-class; this will specify,
        what your indivdual initial condition should look like
        '''
        raise NotImplementedError

class AllZeros(InitialCondition):
    '''
    All values set to 0
    '''
    def __init__(self, nx, ny):
        super().__init__(nx, ny)

    def _setup_array(self):
        return np.zeros(shape=(self.nx, self.ny))

class AllOnes(InitialCondition):
    '''
    All values set to 1
    '''
    def __init__(self, nx, ny):
        super().__init__(nx, ny)

    def _setup_array(self):
        return np.ones(shape=(self.nx, self.ny))

class BasicStartingHeight(InitialCondition):
    '''
    Starting height is a row of specified height
    '''
    def __init__(self, nx, ny, height=0.1):
        self.height = height
        super().__init__(nx, ny)

    def _setup_array(self):
        h = np.zeros(shape=(self.nx, self.ny))
        h[0, :] = self.height
        return h

class BasicStartingSurface(InitialCondition):
    '''
    Surface condition; should be negative
    Outer edges are twice as high as elsewhere
    '''
    def __init__(self, nx, ny, height=-1):
        self.height = height
        super().__init__(nx, ny)
        

    def _setup_array(self):
        H = np.zeros(shape=(self.nx, self.ny))
        H[:, :] = self.height
        #H[:2, :] = self.height/2
        #H[-2:, :] = self.height/2
        return H

def main():
    ao = BasicStartingSurface(10, 10)
    print(ao.get_array())

if __name__ == '__main__':
    main()
