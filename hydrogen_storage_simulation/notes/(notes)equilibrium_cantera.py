import cantera as ct

# Setting gas mixture to equilibrium state ->
g = ct.Solution('gri30.yaml')
g.TPX = 300.0, 101325, 'CH4:095, O2:2, N2:7.52'
g.equilibrate('TP') # keeps temp. and pressure const. and sets to equ.
# doing => g.equilibrate('HP') | keeps enthalpy and pressure const. and sets to equ.
# Also works with UV, SV, and SP

# Checking if equilibrium is reached
rf = g.forward_rates_of_progress
rr = g.reverse_rates_of_progress
# Loop checks if the net rates of reversible reactions is zero
for i in range(g.n_reactions): 
    if g.reaction(i).reversible and rf[i] != 0.0:
        print(' %4i %10.4g ' % (i, (rf[i] - rr[i]) / rf[i]))
# As long as each number is VERY close to 0, then its in equilibrium
