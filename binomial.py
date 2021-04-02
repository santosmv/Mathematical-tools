import numpy as np
import matplotlib.pyplot as plt

from distributions import binomial

p_list = [0.1, 0.5, 0.1]
N_list = [10, 20, 40]

n = np.arange(0, 20)

for i in range(len(p_list)):
    p = p_list[i]
    N = N_list[i]
    plt.plot(n, binomial(n, N, p), 's', label=r'$p = %.1f$'%p + r'   $N = %i$'%N)

markerline, stemlines, baseline = plt.stem(np.array(N_list) * np.array(p_list), binomial(np.array(N_list) * np.array(p_list), np.array(N_list), np.array(p_list)), '--', label='Expected value')
plt.setp(stemlines, 'color', 'gainsboro')
plt.setp(markerline, visible=False)
plt.setp(baseline, visible=False)

plt.xlabel('n', fontsize=15)
plt.ylabel(r'$P(n, N, p)$', fontsize=15)
plt.xticks(range(0,20))
plt.xlim(0,16)
plt.ylim(0,0.5)
plt.legend()
plt.show()