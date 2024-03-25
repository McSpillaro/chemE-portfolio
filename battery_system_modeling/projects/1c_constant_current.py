import pybamm

# pybamm.{model} -> specific model from pybamm package to run sim
model = pybamm.lithium_ion.DFN() # {Battery material}.{Model type}
# DFN -> Doyle-Fuller-Newman model
sim = pybamm.Simulation(model) # Initializes the simulation based on specified model
sim.solve([0, 3600]) # solves for 1 hour of run time
# Solves the simulation var in a time range (units of seconds)
sim.plot()