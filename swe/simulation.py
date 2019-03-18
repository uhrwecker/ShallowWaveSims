from boundary_condition import bc_handler
from initial_condition import ic_handler
from simulator import swe_sim
from swe_config import config

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

SimulationHandler('./swe/swe_config/config.json')
