import numpy as np
import matplotlib.pyplot as plt

from distributions import poisson

p_list = np.array([0.9, 0.8, 0.05])
N_list = np.array([5, 10, 50])
nu_list = p_list * N_list

n = np.arange(0, 20)

for i in range(len(p_list)):
    p = p_list[i]
    N = N_list[i]
    plt.plot(n, poisson(n, N, p), 's', label=r'$\nu = %.1f$'%(N*p) + r'    $N = %i$'%N)

markerline, stemlines, baseline = plt.stem(np.array(N_list) * np.array(p_list), poisson(np.array(N_list) * np.array(p_list), np.array(N_list), np.array(p_list)), '--', label='Expected value', use_line_collection=True)
plt.setp(stemlines, 'color', 'gainsboro')
plt.setp(markerline, 'color', 'gainsboro')
plt.setp(baseline, visible=False)

plt.xlabel('n', fontsize=15)
plt.ylabel(r'$P(n,\nu)$', fontsize=15)
plt.xticks(range(0,20))
plt.xlim(0,16)
plt.ylim(0,0.3)
plt.legend()
plt.show()