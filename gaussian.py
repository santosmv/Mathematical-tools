import numpy as np
import matplotlib.pyplot as plt

from distributions import gaussian

mu_list = [0, -5, 3]
sigma_list = [1, 2, 4]

x = np.linspace(-15, 15, 500)

for i in range(len(mu_list)):
    mu = mu_list[i]
    sigma = sigma_list[i]
    plt.plot(x, gaussian(x, mu, sigma), label=r'$\mu = %d$'%mu + r'   $\sigma = %d$'%sigma)

markerline, stemlines, baseline = plt.stem(mu_list, gaussian(np.array(mu_list), np.array(mu_list), np.array(sigma_list)), '--', label='Expected value')
plt.setp(stemlines, 'color', 'gainsboro')
plt.setp(markerline, 'color', 'silver')
plt.setp(baseline, visible=False)

plt.xlabel('x', fontsize=15)
plt.ylabel(r'$P(x, \mu, \sigma)$', fontsize=15)
plt.xlim(-15,15)
plt.ylim(0,0.5)
plt.legend()
plt.show()