import pybamm
import matplotlib.pyplot as plt

# pybamm.Exerperiment ->
    # Allows for making an experiment simulation in English
    # Creates a synthetic experiment based on paramters
experiment = pybamm.Experiment(
    [
        (
            "Discharge at C/10 for 10 hours or until 3.3 V",
            "Rest for 1 hour",
            "Charge at 1 A until 4.1 V",
            "Hold at 4.1 V until 50mA",
            "Rest for 1 hour",
        )
    ]
    * 3,
)

# loads the model and parameter values
model = pybamm.lithium_ion.DFN()
sim = pybamm.Simulation(model, experiment=experiment)
solution = sim.solve()
solution.plot()