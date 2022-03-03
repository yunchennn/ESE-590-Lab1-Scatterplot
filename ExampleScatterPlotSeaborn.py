"""
ExampleScatterPlotSeaborn
Author: Vibha Mane
Date Created: September 21, 2018
Last Update:  July 13, 2021

Scatter Plot with the "seaborn" module.
"""
#******************************************************************************
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
#******************************************************************************

#****************************************
# Generate data from multivariate normal distribution, and put it in a dataframe
meanX = [0, 1]
covX = [(1, .5), (.5, 1)]
NSamples = 200
data = np.random.multivariate_normal(meanX, covX, NSamples)
df = pd.DataFrame(data, columns=["x", "y"])

#****************************************
# Scatter Plot with "jointplot"
plt.figure(1)
sns.set(style="white", color_codes=True)
sns.jointplot(x="x", y="y", data=df)
plt.title('Scatter Plot, Multivariate Data', color="b")
plt.show()


#****************************************
# Load Iris data; in the following "iris" is a pandas DataFrame
# Scatter Plots and density estimates with "jointplot"
iris = sns.load_dataset("iris")

plt.figure(2)
sns.jointplot(x="sepal_width", y="petal_length", data=iris, kind="kde", space=0, color="g")
plt.title('Scatter Plot, Iris Data', color="g")
plt.show()

#****************************************
# Scatter Plots with "pairplot"
sns.pairplot(iris, hue="species", palette="husl")

#****************************************
# More Scatter Plots
sns.relplot(x="sepal_length", y="sepal_width", hue="species", data=iris);
sns.relplot(x="petal_length", y="petal_width", hue="species", data=iris);
