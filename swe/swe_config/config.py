import json

class SWEConfig():
    '''
    Class that handles the reading and getting
    fields of the config.
    '''
    def __init__(self, path):
        fobj = open(path, 'r')
        self.config = json.load(fobj)
        fobj.close()

    def get_boundary_setup(self):
        return self.config['boundary_condition']

    def get_initial_setup(self):
        return self.config['initial_condition']

    def get_simulation_setup(self):
        return self.config['simulation_parameters']

    def get_physical_setup(self):
        return self.config['physical_parameters']

    def get_array_dimensions(self):
        return (self.get_simulation_setup()['nx'],
                self.get_simulation_setup()['ny'])

def main():
    d = {}
    d['boundary_condition'] = {'u': [{'NoneCondition': {}}],
                               'v': [{'NoneCondition': {}}],
                               'h': [{'OuterBoxBoundary': {'level': 0}}]}
    d['initial_condition'] = {'u': {'AllOnes': {}},
                              'v': {'AllOnes': {}},
                              'h': {'BasicStartingHeight': {'height': 0.1}},
                              'H': {'BasicStartingSurface': {'height': -1}}}
    d['physical_parameters'] = {'g': 10, 'b': 0.1, 'nu': 1}
    d['simulation_parameters'] = {'dx': 1, 'dy': 1, 'dt': 0.1,
                                  'nx': 10, 'ny': 10, 'steps': 100}
    fobj = open('./config.json', 'w')
    json.dump(d, fobj, indent=4, sort_keys=True)
    fobj.close()

if __name__ == '__main__':
    main()
