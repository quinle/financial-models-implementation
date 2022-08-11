import numpy as np
import scipy.stats as ss

class Option():
    def __init__(self, S0, K, div, r, T, sig):
        self.S0 = S0        #current price of underlying asset
        self.K = K          #strike price
        self.div = div      #dividend yield
        self.r = r          #risk-free rate
        self.T = T          #time until expiration
        self.sig = sig  #volatility
        
    #def get_r(self):
    #    return r


class EuropeanOption(Option):
    def __init__(self, S0, K, delta, r, T, sig):
        super(EuropeanOption, self).__init__(S0, K, delta, r, T, sig)
    
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

class AsianOption(Option):
    def __init__(self):
        pass
    
    def MCAntitheticVariablePricer(self):
        #MC antitheticvariable pricer (reduce simulation size)`
        pass

    def TrinomialTree(self):
        pass
