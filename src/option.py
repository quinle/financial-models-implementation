import numpy as np
import scipy.stats as ss
from math import e
import utils

class Option():
    def __init__(self, S0, K, div, r, T, sig):
        self.S0 = S0        #current price of underlying asset
        self.K = K          #strike price
        self.div = div      #dividend yield
        self.r = r          #risk-free rate
        self.T = T          #time until expiration
        self.sig = sig      #volatility
        
    #def get_r(self):
    #    return r


class Vanilla(Option):
    def __init__(self, S0, K, delta, r, T, sig):
        super(Vanilla, self).__init__(S0, K, delta, r, T, sig)

    #Greek letters:
    #Delta (option price/value of underlying asset)
    def Delta(self):
        dfq = e ** (-self.q * self.T)
        if self.Type == 1:
            return dfq * ss.norm.cdf(self.d1)
        else:
            return dfq * (ss.norm.cdf(self.d1) - 1)

    #Gamma (Delta/value of underlying asset)
    def Gamma(self):
        return e ** (-self.q * self.T) * ss.norm.pdf(self.d1) / (self.S * self.sigmaT)
    
    # Vega for 1% change in vol (option price/volatility)
    def Vega(self):
        return 0.01 * self.S * e ** (-self.q * self.T) * \
          ss.norm.pdf(self.d1) * self.T ** 0.5
    
    # Theta for 1 day change (option proce/time to maturity)
    def Theta(self):
        df = e ** -(self.r * self.T)
        dfq = e ** (-self.q * self.T)
        tmptheta = (1.0 / 365.0) \
            * (-0.5 * self.S * dfq * ss.norm.pdf(self.d1) * \
               self.sigma / (self.T ** 0.5) + \
            self.Type * (self.q * self.S * dfq * ss.norm.cdf(self.Type * self.d1) \
            - self.r * self.K * df * ss.norm.cdf(self.Type * self.d2)))
        return tmptheta
    
    #Rho (option price / interest rate)
    def Rho(self):
        df = e ** -(self.r * self.T)
        return self.Type * self.K * self.T * df * 0.01 * ss.norm.cdf(self.Type * self.d2)

    def get_r(self, t):
        #allow r to vary
        # implement function
        return self.r(t)

    def BS_closed_form(self):
        pass

    def MC(self):
        pass

    def FDM_PDE(self):
        #implicit, explicit, Crank-Nicholson?
        pass
    def Fourier_inversion(self):
        #https://pfadintegral.com/docs/Schmelzle2010%20Fourier%20Pricing.pdf
        pass

class Exotic(Option):
    def __init__(self):
        pass
    
    def MCAntitheticVariablePricer(self):
        #MC antitheticvariable pricer (reduce simulation size)`
        pass

    def TrinomialTree(self):
        pass
