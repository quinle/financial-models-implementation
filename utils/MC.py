import numpy as np
import scipy.stats as ss


#BlackScholes Monte Carlo for European call 
#M: number of simulation, N: number of time steps
def BS_MC(K, T, S, sig, r, div, N, M):
    dt = T/N
    nudt = (r - div - 0.5*sig*sig)*dt
    sigsdt = sig*np.sqrt(dt)
    lnS = np.log(S)
    
    sum_CT = 0
    sum_CT2 = 0

    for j in range(M):
        lnSt = lnS
        for i in range(N):
            eps = np.random.standard_normal()
            lnSt += nudt + sigsdt * eps
        ST = np.exp(lnSt)
        CT = max(ST - K, 0)
        sum_CT += CT
        sum_CT2 += CT*CT
    
    call_value = sum_CT/M*np.exp(-r*T)
    SD = np.sqrt((sum_CT2 - sum_CT*sum_CT/M)*np.exp(-2*r*T)/(M-1))
    SE = SD/np.sqrt(M)
    return call_value, SD, SE




    



