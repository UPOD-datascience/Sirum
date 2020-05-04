import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import logging
log = logging.getLogger("SIR_logger")

'''
 add parameters/coefficient matrix routine
'''

class SIR:
    def __init__(self, beta_0=None, gamma=None, beta_changepoints=None):
        """
        beta_0: initial transferrability rate
        gamma: initial recovery/fatality rate
        beta_changepoints: list of tuples with (day_of_change, change_factor/change_function)
        """        
        self.beta_0 = beta_0
        self.beta_changepoints = beta_changepoints
        self.gamma = gamma
    
    def _ODE(self, y, t, p):
        ds = -p[0]*y[0]*y[1]
        di = p[0]*y[0]*y[1] - p[1]*y[1]  
        dr = p[1]*y[1] 
        return [ds, di, dr]
    def solve_ODE(self, Initial_vals, days, beta_0=None, gamma=None):
        """
        This is a ODE implementation of SIR model. 

        Initial_val[list of length 3]: It is the initial condition, such that S = Initialval[0], I = Initialval[1], R = Initialval[2]
        days: is the time interval for solution based on days
        params [list of length 3]: This is the paramters of ODE SIR model, such that beta = params[0], gamma = params[2], N = params[2]
        """
        assert days is not None, "Please enter the number of simulation days"
        if  (beta_0 is None) and (self.beta_0 is None):
            raise(ValueError, "A beta_0 must be set")
        elif (beta_0 is None):
            beta_0 = self.beta_0
        if (gamma is None) and (self.gamma is None):
            raise(ValueError, "A gamma must be set")
        elif (gamma is None):
            gamma = self.gamma

        # Initial conditions vector
        S, I, R = [Initial_vals[0]], [Initial_vals[1]], [Initial_vals[2]]
        N = S[0]+I[0]+R[0]

        time = np.linspace(0, days, days + 1) # A grid of time points (in days)
        beta = np.full((days + 1,), beta_0)

        #### varying beta
        if self.beta_changepoints is not None:
            for _cp in self.beta_changepoints:
                if isinstance(_cp[1], float):
                    beta[_cp[0]:] = _cp[1] * beta[_cp[0] - 1]
                elif isinstance(_cp[1], object):
                    beta[_cp[0]:] = _cp[1](time[_cp[0]:])

        # Simulation of differential equation using Numerical differentiation
        # dx/dt = (x[t] - x[t-1])/dt
        # E.g. S[t] = S[t-1] + dt *(B*S*I/N)  dt = 1 # In our simulation dt is 1-day
        log.info("Starting SIR with; Beta 0:{}, Gamma:{}, S0:{}, I0:{}, R0:{}, N:{}".format(beta[0], gamma, S[0], I[0], R[0], N))
        for idx, t in enumerate(time):
            term1 = (beta[idx]/N) * S[-1] * I[-1]
            term2 = gamma * I[-1]
            S.append(S[-1] - term1)
            I.append(I[-1] + term1 - term2)
            R.append(R[-1] + term2)
        self.S = np.array(S)
        self.I = np.array(I) 
        self.R = np.array(R)

        return np.vstack([S, I, R]).T
        #return [S, I, R]

    def plot(self, ax=None, figsize=(10, 7)):
        if ax is None:
            fig, ax = plt.subplots(figsize=figsize)
        ax.plot(self.S, label='Susceptible')
        ax.plot(self.I, label='Infected')
        ax.plot(self.R, label='Recovered or Death')
        ax.set_xlabel('Time (days)')
        ax.set_ylabel('Population Number')
        ax.legend(loc='upper right')
        plt.show()
