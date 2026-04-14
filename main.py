import numpy as np
import matplotlib.pyplot as plt

#Parameters
gammas = [0.5, 1.0, 2.0]
sigmas = [0.5, 1.0, 2.0]

#Spectral Lineshape
w = np.linspace(-10,10,1000)
w0 = 0 #resonance frequency

def lorentzian(w, w0, gamma):
    return((1/np.pi)*(gamma/((w-w0)**2 + gamma**2)))

def gaussian(w, w0, sigma):
    return((1/(sigma*np.sqrt(2*np.pi)))*np.exp(-((w-w0)**2)/(2*sigma**2)))

#Dephasing
t = np.linspace(0,10,1000)
def exp_decay(t, gamma):
    return np.exp(-gamma*t)

def gauss_decay(t, sigma):
    return np.exp(-(sigma**2)*(t**2))

#plotting

#fig, axes = plt.subplot(1,2,figsize=(8,4))
fig = plt.figure(figsize=(8,4))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

#(a)Frequency domain
for g in gammas:
    ax1.plot(w,lorentzian(w,w0,g), label=f'Lorentzian $\gamma$={g}')
for s in sigmas:
    ax1.plot(w,gaussian(w,w0,s), linestyle='--', label=f'Gaussian $\sigma$={s}')

ax1.set_title("(a) Frequency Domain")
ax1.set_xlabel("Frequency (a.u.)")
ax1.set_ylabel("Normalized Intensity")
ax1.legend(fontsize=6)
ax1.grid()

#(b) Time domain
for g in gammas:
    ax2.plot(t,exp_decay(t,g), label=f'Exp $\gamma$={g}')
for s in sigmas:
    ax2.plot(t, gauss_decay(t,s), linestyle='--', label=f'Gauss $\sigma$={s}')

ax2.set_title("(b) Time Domain")
ax2.set_xlabel("Time (a.u.)")
ax2.set_ylabel("Coherence")
ax2.legend(fontsize=6)
ax2.grid()
plt.tight_layout()
plt.show()
