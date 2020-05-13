import pytest
import numpy as np

from sirum.models import sir_model


def test_sum_to_n():
    """Test that output of solve_ODE sums to N"""

    sir = sir_model.SIR()

    N = 15e6
    beta = 0.2
    gamma = 0.5
    I_0, R_0 = 100, 0
    S_0 = N - I_0 - R_0
    days = 90
    res = sir.solve_ODE(Initial_vals=[S_0,I_0,R_0], days=days, beta_0=beta, gamma=gamma)

    assert np.sum(res, axis=1) == pytest.approx(N), "S, I and R do not sum to N for at least one time unit"
