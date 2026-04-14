# CARS Dephasing Simulator

## Overview

This project simulates Coherent Anti-Stokes Raman Scattering (CARS)-relevant spectral dephasing dynamics using Lorentzian and Gaussian lineshape models. It demonstrates how different broadening mechanisms affect both frequency-domain spectral profiles and time-domain coherence decay.

---

## Physical Concepts

The simulation explores the connection between:

- **Lorentzian lineshape** → homogeneous broadening  
- **Gaussian lineshape** → inhomogeneous broadening  
- **Time-domain dephasing** → loss of coherence  
- **Frequency-domain response** → spectral intensity distribution  

This reflects the fundamental relationship between time and frequency domains in optical spectroscopy.

---

## Theoretical Model

The simulation is based on standard spectral response functions used in optical spectroscopy.

### Lorentzian lineshape

$L(\omega)=\frac{1}{\pi}\frac{\gamma}{(\omega-\omega_0)^2-\gamma^2}$

### Gaussian Lineshape

$G(\omega)=\frac{1}{\sigma\sqrt{2\pi}}exp\left[-\frac{(\omega-\omega_0)^2}{2\sigma^2}\right]$

### Time-domain dephasing

- Homogeneous (exponential decay): $exp(-\gamma t)$

- Inhomogeneous (Gaussian decay): $exp(-\sigma^2 t^2)$

#### Symbol Definations

- $\omega$: Angular frequency of the probing em field (a.u.)
- $\omega_0$: Resonance frequnecy of vibrational mode (a.u.)
- $\gamma$: Homogeneous dephasing rate (ontroles Lorentzian linewidth and exponential decay)
- $\sigma$: Inhomogeneous broadening parameter (controls Gaussian linewidth and Gaussian decay)
- $t$: Time (a.u.)

---

## What This Simulation Shows

### Frequency Domain
- Lorentzian profile controlled by damping parameter $\gamma$
- Gaussian profile controlled by width parameter $\sigma$

### Time Domain
- Exponential decay:  
  coherence loss ~ $e^{-\gamma t}$
- Gaussian decay:  
  coherence loss ~ $e^{-\sigma^2 t^2}$

---

## Key Insight

The project visualizes how:

**Stronger dephasing → broader spectral lines + faster coherence decay**

This is directly relevant to CARS and nonlinear spectroscopy systems.

---

## Parameters Used

- $\gamma$: 0.5, 1.0, 2.0  
- $\sigma$: 0.5, 1.0, 2.0  
- Frequency range: -10 to 10 (a.u.)  
- Time range: 0 to 10 (a.u.)

---

## How to Run

```bash
pip install numpy matplotlib
python main.py
