from boundary_condition import bc

class BoundaryConditionHandler():
    '''
    Class that handles the setup of the different
    boundary conditions from config dict
    '''
    def __init__(self, config):
        self.config = config

        self.bc_dict = self._setup_boundary_conditions()

    def _setup_boundary_conditions(self):
        bc_u = self._setup_bc('u')
        bc_v = self._setup_bc('v')
        bc_h = self._setup_bc('h')
        return {'u': bc_u, 'v': bc_v, 'h': bc_h}

    def _setup_bc(self, idnt):
        bc_list = self.config[idnt]
        boundary_conditions = []
        for item in bc_list:
            for bc_class in item.keys():
                bc_obj = bc.__dict__[bc_class](**item[bc_class])
                boundary_conditions.append(bc_obj)
        return boundary_conditions

def main():
    from swe_config import config
    c = config.SWEConfig('./swe_config/config.json')
    BoundaryConditionHandler(c.get_boundary_setup())

if __name__ == '__main__':
    main()
