from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

import numpy as np

class TwoDSurfacePlot():
    def __init__(self, dim):
        nx, ny = dim

        self.x_scale, self.y_scale = np.meshgrid(np.linspace(0, nx, ny),
                                                 np.linspace(0, nx, ny))
        self.fig = pyplot.figure()
        self.axis = self.fig.gca(projection='3d')

    def plot(self, h, show=True):
        surface = self.axis.plot_surface(self.x_scale, self.y_scale,
                                         h[:], antialiased=True)
        pyplot.show()

    def plot_without_show(self, h):
        self.surface = self.axis.plot_surface(self.x_scale, self.y_scale,
                                         h[:], antialiased=True)
        pyplot.pause(0.05)
        self.axis.clear()

    def show(self):
        pyplot.show()
