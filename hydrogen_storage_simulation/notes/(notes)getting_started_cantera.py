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

# Setting composition in molar (X) or mass (Y) fractions
phi = 0.8
gas1.X = {'CH4':1, 'O2':2/phi, 'N2':2*3.76/phi} # setting fractions in dict format
# This allows for the temp. & density to be const
# and only the pressure and other intensive prop. changes

# Specific properties of the gas can be held const. by the 'None'
gas1.SV = None, 2.1 # changes specific volume while keeping entropy const.

gas1.TPX = None, None, 'CH4:1.0, O2:0.5' # sets mass fractions and keeps temp. and pressure const.