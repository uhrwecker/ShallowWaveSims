import numpy as np

class GeneralNumericHandler():
    '''
    Class that handles the derivatives and check
    inputs/output types
    '''
    def __init__(self):
        self.x = 0

    def d_dx(self, array, dx):
        try:
            return np.gradient(array, dx, axis=0)
        except:
            raise ValueError('In d/dx: array-type is not numpy.array')

    def d_dy(self, array, dy):
        try:
            return np.gradient(array, dy, axis=1)
        except:
            raise ValueError('In d/dy: array-type is not numpy.array')
