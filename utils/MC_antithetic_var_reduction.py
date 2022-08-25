import numpy as np
import scipy.stats as ss

#BlackScholes-world Monte Carlo for European call with antithetic variance reduction
def BS_MC_antithetic(K, T, S, sig, r, div, N, M):
    dt = T/N
    nudt = (r - div - 0.5*sig*sig)*dt
    sigsdt = sig*np.sqrt(dt)
    lnS = np.log(S)
    
    sum_CT = 0
    sum_CT2 = 0
    
    for j in range(M):
        lnSt1 = lnS
        lnSt2 = lnS
        
        for i in range(N):
            eps = np.random.standard_normal()
            lnSt1 += nudt + sigsdt*eps
            lnSt2 += nudt + sigsdt*(-eps)
            
        St1 = np.exp(lnSt1)
        St2 = np.exp(lnSt2)
        CT = 0.5*(max(0, St1 - K) + max(0, St2 - K))
        sum_CT = sum_CT + CT
        sum_CT2 = sum_CT2 + CT*CT
    
    call_value = sum_CT/M*np.exp(-r*T)
    SD = np.sqrt((sum_CT2 - sum_CT*sum_CT/M)*np.exp(-2*r*T)/(M-1))
    SE = SD/np.sqrt(M)
    return call_value, SD, SE