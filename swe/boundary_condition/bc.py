import numpy as np

class BoundaryCondition():
    '''
    Base class that will be used to control the boundary
    conditions after each simulation step for h, u and v
    '''
    def __init__(self, identifier='u'):
        self.id = identifier

    def apply(self, array):
        '''
        Main method that will be called to apply the boundary
        condition on the given array.
        '''
        raise NotImplementedError

class NoneCondition(BoundaryCondition):
    '''
    Defines a none-existing boundary
    '''
    def __init__(self, identifier='u'):
        super().__init__(identifier)

    def apply(self, array):
        return array

class WallCondition(BoundaryCondition):
    '''
    Will define a wall of given length where all
    values are set to a given level (should probably be 0)
    only horizontal/vertical
    '''
    def __init__(self, identifier='u', start=(0,0), end=(3, 3), level=0):
        super().__init__(identifier)
        self.start_x, self.start_y = start
        self.end_x, self.end_y = end
        self.level = level

    def apply(self, array):
        if self.start_x == self.end_x:
            self.end_x += 1
        if self.start_y == self.end_y:
            self.end_y += 1
        array[self.start_x:self.end_x, self.start_y:self.end_y] = self.level
        return array

class OuterBoxBoundary(WallCondition):
    '''
    Will define a box at the edge of an array and sets it
    to given value (default: 0)
    '''
    def __init__(self, identifier='u', start=(0,0), end=(1, 0), level=0):
        super().__init__(identifier, start, end, level)

    def apply(self, array):
        array[self.start_x, :] = self.level
        array[:, self.start_y] = self.level
        array[self.end_x-1, :] = self.level
        array[:, self.end_y-1] = self.level
        return array

def main():
    u = np.ones(shape=(10, 10))
    wc = WallCondition()
    print(wc.apply(u))
    box = OuterBoxBoundary(end=(10, 10))
    print(box.apply(u))

if __name__ == '__main__':
    main()
