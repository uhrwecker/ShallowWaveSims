from initial_condition import ic

class InitialConditionHandler():
    '''
    Class that handles the setup of the different
    arrays for u, v and h and establishes the initial conditions
    on them.
    '''
    def __init__(self, config, dimensions):
        self.config = config
        self.dimensions = dimensions

        self.ic_dict = self._setup_initial_conditions()

    def get_initials(self, idnt):
        try:
            return self.ic_dict[idnt]
        except:
            raise KeyError('At get initials: wrong identifier')

    def _setup_initial_conditions(self):
        ic_u = self._setup_ic('u')
        ic_v = self._setup_ic('v')
        ic_h = self._setup_ic('h')
        ic_H = self._setup_ic('H')
        return {'u': ic_u, 'v': ic_v, 'h': ic_h, 'H': ic_H}

    def _setup_ic(self, idnt):
        ic_list = self.config[idnt]
        initial_conditions = []
        for ic_class in ic_list.keys():
            ic_obj = ic.__dict__[ic_class](self.dimensions[0],
                                           self.dimensions[1],
                                           **ic_list[ic_class])
            initial_conditions.append(ic_obj)
        return initial_conditions
