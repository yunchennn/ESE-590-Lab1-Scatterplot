#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[24]:


df = pd.read_csv("test.csv", sep=r'\s*,\s*',header=0, encoding='ascii', engine='python')


# In[25]:


from sklearn import tree
features = list(df.columns[:5])
X = df[features]
y = df['final']


# In[26]:


classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(X, y)
tree.plot_tree(classifier)


# In[37]:


import graphviz
from graphviz import Source
from IPython.display import SVG

g = graphviz.Graph(format='png')

dot_data = tree.export_graphviz(classifier, out_file=None,  feature_names=features,  filled=True, rounded=True, special_characters=True)
graph = graphviz.Source(dot_data)
graph.render('dtree_render_',view=True)
#graph = Source( tree.export_graphviz(classifier, out_file=None, feature_names=X.columns))
#SVG(graph.pipe(format='svg'))


# In[ ]:





# In[ ]:




