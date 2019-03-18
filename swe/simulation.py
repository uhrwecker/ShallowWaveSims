from swe.boundary_condition import bc_handler
from swe.initial_condition import ic_handler
from swe.simulator import swe_sim
from swe.swe_config import config
from swe.visualization import low_level

import numpy as np

class SimulationHandler():
    '''
    This class handles the setup of the simulation process,
    implements the predefined simulation scenario,
    starts the simulation
    and handles the integration of boundary conditions.
    '''
    def __init__(self, config_path):
        self.config = config.SWEConfig(config_path)

        self.dimensions = self.config.get_array_dimensions()
        self.sim_params = self.config.get_simulation_setup()
        self.phys_params = self.config.get_physical_setup()
        

        self.initial = ic_handler.InitialConditionHandler(self.config.get_initial_setup(),
                                                          self.dimensions)
        self.boundary = bc_handler.BoundaryConditionHandler(self.config.get_boundary_setup())

        self.simulator = swe_sim.ShallowWaveSimulator(self.sim_params['dx'],
                                                      self.sim_params['dy'],
                                                      self.sim_params['dt'],
                                                      self.phys_params['g'],
                                                      self.phys_params['b'],
                                                      self.phys_params['nu'])
        self.visualizer = low_level.TwoDSurfacePlot(self.dimensions)

    def simulate(self):
        import time

        print('Setup arrays ...')
        self.setup_arrays()

        print('Starting Simulation ...')
        start_time = time.time()
        for index in range(self.sim_params['steps']):
            # do one step in_simulation
            self.h, self.u, self.v = \
                    self.simulator.step(self.h, self.u, self.v, self.H)
            print('- Step ({}/{})'.format(index+1, self.sim_params['steps'])) 
            # apply boundary conditions
            self.apply_boundary_conditions()
            print(' - Apply boundary conditions ...')

            if np.isnan(np.min(self.h)):
                print('Error: Simulation diverged. Adjust your simulation parameters.')
                break
            if index % 6 == 0:
                self.visualizer.plot_without_show(self.h)
        
        print('Simulation done. Took {}s (mean time: {}s)'.format(time.time()-start_time,
                                                                  (time.time()-start_time)/self.sim_params['steps']))
        self.visualizer.show()

    def plot(self):
        self.visualizer.plot(self.h)

    def setup_arrays(self):
        self.u = self.initial.get_initials('u')[0].get_array()
        self.v = self.initial.get_initials('v')[0].get_array()
        self.h = self.initial.get_initials('h')[0].get_array()
        self.H = self.initial.get_initials('H')[0].get_array()

    def apply_boundary_conditions(self):
        # boundaries for u:
        for bc in self.boundary.get_boundaries('u'):
            bc.apply(self.u)
        # boundaries for v:
        for bc in self.boundary.get_boundaries('v'):
            bc.apply(self.v)
        # boundaries for h:
        for bc in self.boundary.get_boundaries('h'):
            bc.apply(self.h)
            
