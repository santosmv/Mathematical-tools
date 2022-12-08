import numpy as np
from iminuit import Minuit

def model(a,b,x):
    y = a*x + b
    return y

Ndata_list = np.random.rand(100)
#some variable, like position
x = np.linspace(0,100,100)

#chi-square
def chi_square_f(a,b):
    chi_list = []
    for i in range(len(Ndata_list)):
        Nmodel = model(a,b,x[i])
        Ndata = Ndata_list[i]
        chi = (Ndata - Nmodel)**2/Nmodel
        chi_list.append(chi)
    chi_total = sum(chi_list)
    return chi_total

#defining minimization function
min_chi = Minuit(chi_square_f, a=0.5, b=0.5)
#defining limits of parameters
min_chi.limits['a'] = (0,10)
min_chi.limits['b'] = (0,10)
#defining if profiles or contours are bounded by least squares or max likelihood
min_chi.errordef = Minuit.LEAST_SQUARES
#minimize the function
min_chi.migrad()
print(min_chi)