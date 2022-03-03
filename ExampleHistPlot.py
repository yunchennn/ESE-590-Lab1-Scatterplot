"""
Spyder Editor
ExampleHistPlot
Author: Vibha Mane
Date Created: September 19, 2018
Last Update:  July 10, 2021

Histogram and Kernel Density Plots, with the "seaborn" Module
Data Generated from Mixture Normal Distribution, and Gamma Distribution
"""
#******************************************************************************

import numpy as np
import scipy  as sp
import matplotlib.pyplot as plt
import seaborn as sns
from IPython.core.pylabtools import figsize
#******************************************************************************

#****************************************
# Create samples from a mixture normal distribution (using NumPy)
mu1 = 0
sigma1 = 1.0
mu2 = 4.0
sigma2 = 1.5

cf = 0.3
SamplesTotal = 1000
SamplesN1 = int(cf*SamplesTotal)
SamplesN2 = int(SamplesTotal-SamplesN1)

x1 = np.random.normal(mu1, sigma1, SamplesN1)
x2 = np.random.normal(mu2, sigma2, SamplesN2)
x1 = np.append(x1 ,x2)        
    
#****************************************
# Histogram Plot and Kernel Density Plot with "distplot" 
figsize(9,9)
fa = plt.figure()
sns.displot(x1, bins=20, kde=True)
plt.title('Histogram and Kernel Density Estimate')
plt.grid(True)

#****************************************
# Histogram Plot and Kernel Density Plot with "kdeplot" 
fa = plt.figure()  # to generate new plot
sns.kdeplot(x1, bw_method=.1, label="bw: 0.1")
sns.kdeplot(x1, bw_method=.5, label="bw: 0.5")
sns.kdeplot(x1, bw_method=1.0, label="bw: 1.0")
plt.legend();

plt.title('Kernel Density Estimate with Different Bandwidths')
plt.grid(True)
plt.show()

#****************************************
# Save the plot to PDF file
fa.savefig('Example1.pdf')

#****************************************
# Fitting parametric distribution
# Generate samples from gamma distribution
fa = plt.figure()  # to generate new plot
x3 = np.random.gamma(6, scale=1.0, size=200)
sns.distplot(x3, bins=20, kde=False, fit=sp.stats.gamma, color='g')

plt.title('Fitting Parametric Distribution (Gamma) to Data')
plt.grid(True)
