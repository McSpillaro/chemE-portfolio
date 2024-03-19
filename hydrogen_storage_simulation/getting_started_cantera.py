import cantera as ct
import numpy as np

# 1st thing to do:
    # Set var to represent some phase of matter
gas1 = ct.Solution('gri30.yaml')
# Allows for viewing of the gas1() object as function
    # Gives all parameters & details of the gas
gas1()
# Setting the state's temperature and pressure
gas1.TP = 1200, 101325 # in Kelvin (K), Pascals (Pa)
# Setting state properties -> temperature, density
gas1.TD = 1200, 0.0204723 
# Setting state properties -> specific enthalpy, pressure
gas1.HP = 1.32956e7, 101325 # Joules (J), Pascal (Pa)
# Extensive properties must be in per unit mass

# Properties can be ready independently of each other
gas1_temp = gas1.T # Shows temperature of gas1
gas1_enthalpy = gas1.h # Shows enthalpy of gas1

