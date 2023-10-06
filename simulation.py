import Utilities
import numpy as np
import AIC, CUSUM
import simulation_func

Max_RL = 2000 # Max RunLength for each run to break 
repeated_times = 1000 # repeated times for Monte Carlo simulation
tau=25 # the term to introduce shift
type = 'norm'
delta_list = [1,2,3]
arg2func = {'AIC': [2], 'CUSUM': (0,1,0.5,5.3)}
name2func = {'AIC': AIC.aic_precise, 'CUSUM': CUSUM.cusum}

if __name__ == "__main__":
    ARLs = simulation_func.get_ARLs(name2func, type, repeated_times, Max_RL, tau, delta_list, arg2func)
    Utilities.serialize(ARLs, 'ARLs.pickle')
    print ('Computing ARL: Done')