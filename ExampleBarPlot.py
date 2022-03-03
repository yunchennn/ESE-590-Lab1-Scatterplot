"""
ExampleBarPlot
Author: Vibha Mane
Date Created: September 25, 2018
Last Update:  July 13, 2021

Utilizing the "seaborn" Module to plot Categorical Data
Bar Plots with Titanic Data Set
"""

#******************************************************************************
# Import necessary libraries
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd


#***********************************
# Load titanic data, from the built-in Seaborn Data Set
titanic = sns.load_dataset("titanic")

# The following command displays all columns
#pd.set_option('display.expand_frame_repr', False)
# slice some rows
#print(titanic[0:8])

# The following command displays the first few rows
print("First few rows of data")
print(titanic.head())

# The following command displays the last few rows
print("Last few rows of data")
print(titanic.tail())

# The following command writes dataframe to a .csv file 
titanic.to_csv('output.csv')

# Create a bar plot using "factorplot"
#g = sns.factorplot("class", "survived", hue="sex", col="deck", col_wrap=2, data=titanic, kind="bar", legend=True)               
g = sns.catplot(x="class", y="survived", hue="sex", data=titanic, palette="deep", kind="bar", legend=True)               

# Show plot
plt.show()