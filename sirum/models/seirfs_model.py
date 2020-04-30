import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class SEIRFS:
    def __init__(self, beta_0, gamma, eta, sigma, mu, N, beta_changepoints=None):
        """
        If mu is 0: SEIRS
        If eta is 0: SEIRF
        If sigma is 0: SIRFS
        If mu, eta, sigma are 0: SIR
        """
        self.beta_0 = beta_0
        self.beta_changepoints = beta_changepoints
        self.gamma = gamma
        self.eta = eta
        self.sigma = sigma
        self.mu = mu
        self.N = N
        
    def solve_ODE(self, Initial_val, days):
        """
        This is a ODE implementation of SIR model. 

        Initial_val[list of length 3]: It is the initial condition, such that S = Initialval[0], I = Initialval[1], R = Initialval[2]
        days: is the time interval for solution based on days
        params [list of length 3]: This is the paramters of ODE SIR model, such that beta = params[0], gamma = params[2], N = params[2]
        """
        # Initial conditions vector
        S, E, I, R, F = [Initial_val[0]], [Initial_val[1]], [Initial_val[2]], [Initial_val[3]], [Initial_val[4]]
        # Simulation of differential equaiton using Numerical differentiation
        # dx/dt = (x[t] - x[t-1])/dt
        # E.g. S[t] = S[t-1] + dt *(B*S*I/N)  dt = 1 # In our simulation dt is 1-day

        time = np.linspace(0, days, days + 1) # A grid of time points (in days)
        beta = np.full((days + 1,), self.beta_0)

        #### varying beta
        if self.beta_changepoints is not None:
            for _cp in self.beta_changepoints:
                if isinstance(_cp[1], float):
                    beta[_cp[0]:] = _cp[1] * beta[_cp[0] - 1]
                elif isinstance(_cp[1], object):
                    beta[_cp[0]:] = _cp[1](time[_cp[0]:])


        for idx, t in enumerate(time):
            term1 = (beta[idx]/self.N) * S[-1] * I[-1]
            term2 = eta*R[-1]
            term3 = sigma*E[-1]
            term4 = gamma*I[-1]
            term5 = mu*I[-1]

            S.append(S[-1] - term1 + term2)
            E.append(E[-1] + term1 - term3)
            I.append(I[-1] + term3 - term4 - term5)
            R.append(R[-1] + term4 - term2)
            F.append(F[-1] + term5)
        self.S = np.array(S)
        self.E = np.array(E)
        self.I = np.array(I) 
        self.R = np.array(R)
        self.F = np.array(F)

    def plot(self):
        fig, ax = plt.subplots()
        ax.plot(self.S, label='Susceptible')
        ax.plot(self.E, label='Exposed')
        ax.plot(self.I, label='Infected')
        ax.plot(self.R, label='Recovered or Death')
        ax.plot(self.F, label='Early fatalities')
        ax.set_xlabel('Time (days)')
        ax.set_ylabel('Population Number')
        ax.legend(loc='upper right')
        plt.show()