from swe.simulation import SimulationHandler

def main():
    sim = SimulationHandler('./swe/swe_config/config.json')

    sim.simulate()

    sim.plot()

if __name__ == '__main__':
    main()
