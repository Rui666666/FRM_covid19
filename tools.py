import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def logistic_function(t, N_0, K, r):
    N_t = N_0*np.exp(r*t)/(1+(N_0/K)*(np.exp(r*t)-1))
    return N_t

def logistic_function_growth_rate(t, r_max, r_min, t_peak, k):
    r_t = r_max - ((r_max - r_min)/(1 + np.exp(k*(t - t_peak))))
    return r_t

def hubbert_curve(t, N_0, K, r):
    nominator = np.exp(r*t)*N_0*(K-N_0)
    denominator = K*((1+(N_0/K)*(np.exp(r*t)-1))**2)
    return nominator/denominator

def hubbert_curve_asy(t, K, r_max, r_min, t_peak, k):
    nominator = logistic_function_growth_rate(t, r_max, r_min, t_peak, k) * K * np.exp(-logistic_function_growth_rate(t, r_max, r_min, t_peak,k)*(t-t_peak))
    denominator = (1 + np.exp(-logistic_function_growth_rate(t, r_max, r_min, t_peak, k)*(t-t_peak)))**2
    return nominator/denominator

def two_hubbert_curve(t, N_0_1, K_1, r_1, N_0_2, K_2, r_2):
    return hubbert_curve(t, N_0=N_0_1, K=K_1, r=r_1) + hubbert_curve(t, N_0=N_0_2, K=K_2,r=r_2)

def two_hubbert_curve_asy(t, K_1, r_max_1, r_min_1, t_peak_1, k_1, K_2, r_max_2, r_min_2, t_peak_2, k_2):
    return hubbert_curve_asy(t, K=K_1, r_max=r_max_1, r_min=r_min_1, t_peak=t_peak_1, k=k_1)+\
           hubbert_curve_asy(t, K=K_2, r_max=r_max_2, r_min=r_min_2, t_peak=t_peak_2, k=k_2)

def wkh_function(t, alpha1, beta1, alpha2, beta2):
    y = np.exp(-(t-alpha1)/beta1) / (beta1*(1 + np.exp(-(t-alpha1)/beta1))**2 ) + np.exp(-(t-alpha2)/beta2) / (beta2*(1 + np.exp(-(t-alpha2)/beta2))**2 )
    return y

class Plot(object):
    def __init__(self):
        self.figure = plt.figure(figsize=(16,9))
        
    def title(self, title):
        self.title = plt.title(title)
        
    def addplot(self, xvalues, yvalues):
        self.x = xvalues
        self.y = yvalues
        plt.plot(self.x, self.y)
        plt.legend()
    
