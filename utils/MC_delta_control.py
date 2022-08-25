
import numpy as np
import scipy.stats as ss
from src.option import Delta, Vanilla


#BlackScholes Monte Carlo for European call with Delta-based control variate
def BS_MC_delta_control(K, T, S, sig, r, div, N, M):
    dt = T/N
    nudt = (r - div - 0.5*sig*sig)*dt
    sigsdt = sig*np.sqrt(dt)
    erddt = np.exp((r-div)*dt)
    
    beta1 = -1
    
    sum_CT = 0
    sum_CT2 = 0
    
    option = Vanilla(St, t, K, T, sig, r, div)

    for j in range(M):
        St = S
        cv = 0
        
        for i in range(N):
            t = (i-1)*dt
            delta = option.Delta()
            eps = np.random.standard_normal()
            Stn = St*np.exp(nudt + sigsdt*eps)
            cv += delta*(Stn - St*erddt)
            St = Stn
        
        CT = max(0, St - K) + beta1 * cv
        sum_CT = sum_CT + CT
        sum_CT2 = sum_CT2 + CT*CT
        
    call_value = sum_CT/M*np.exp(-r*T)
    SD = np.sqrt((sum_CT2 - sum_CT*sum_CT/M) * np.exp(-2*r*T)/(M-1))
    SE = SD/np.sqrt(M)