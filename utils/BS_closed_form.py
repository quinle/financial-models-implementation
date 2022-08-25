
import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt


#BS pricer for European option on non-dividend stock\n",
#option_type = 'call' or 'put', S0: initial price, K: strike price, r: risk-free interest rate, sigma: violatility, T: mature time\n",
def BS_closed_form(option_type, S0, K, r, sigma, T):
    d1 = (np.log(S0/K) + (r + sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    if option_type == 'call':
        return S0 * ss.norm.cdf(d1) - K * np.exp(-r*T) * ss.norm.cdf(d2)
    elif option_type == 'put':
        return K * np.exp(-r*T) * ss.norm.cdf(-d2) - S0 * ss.norm.cdf(-d1)

#BS pricer for European option on stock with dividend paid at T
def BS_closed_form_div(div, option_type, S0, K, r, sigma, T): #d is the dividend on each ex-dividend date and x1, x2 were ex-divident date in months\n",
    div_present = div * np.exp(-r * T) 
    return BS_closed_form(option_type, S0 - div_present, K, r, sigma, T)

#BS pricer with continuous dividend div
def BS_closed_continous_div(div, option_type, S0, K, r, sigma, T):
    d1 = (np.log(S0/K) + (r-div+ sigma**2/2)*T)/(sigma*np.sqrt(T))
    d2 = d1 - sigma*np.sqrt(T)
    if option_type == 'call':
        return np.exp(-div*T)*S0*ss.norm.cdf(d1) - K * np.exp(-r*T) * ss.norm.cdf(d2)
    else:
        return K * np.exp(-r*T) * ss.norm.cdf(-d2) - np.exp(-div*T)*S0 * ss.norm.cdf(-d1)