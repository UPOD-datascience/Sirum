import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

class SIR:
    def __init__(self, beta, gamma, N):
        self.beta = beta
        self.gamma = gamma
        self.N = N
        
    def solve_ODE(self, Initial_val, days):
        """
        This is a ODE implementation of SIR model. 

        Initial_val[list of length 3]: It is the initial condition, such that S = Initialval[0], I = Initialval[1], R = Initialval[2]
        days: is the time interval for solution based on days
        params [list of length 3]: This is the paramters of ODE SIR model, such that beta = params[0], gamma = params[2], N = params[2]
        """
        # Initial conditions vector
        S, I, R = [Initial_val[0]], [Initial_val[1]], [Initial_val[2]]
        # Simulation of differential equaiton using Numerical differentiation
        # dx/dt = (x[t] - x[t-1])/dt
        # E.g. S[t] = S[t-1] + dt *(B*S*I/N)  dt = 1 # In our simulation dt is 1-day
        for _ in range(days):
            term1 = (self.beta/self.N) * S[-1] * I[-1]
            term2 = self.gamma * I[-1]
            S.append(S[-1] - term1)
            I.append(I[-1] + term1 - term2)
            R.append(R[-1] + term2)
        self.S = np.array(S)
        self.I = np.array(I) 
        self.R = np.array(R)

    def plot(self):
        fig, ax = plt.subplots()
        ax.plot(self.S, label='Susceptible')
        ax.plot(self.I, label='Infected')
        ax.plot(self.R, label='Recovered or Death')
        ax.set_xlabel('Time (days)')
        ax.set_ylabel('Population Number')
        ax.legend(loc='upper right')
        plt.show()