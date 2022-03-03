#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn import cluster, datasets, metrics
import matplotlib.pyplot as plt


# In[2]:


iris = datasets.load_iris()
iris_X = iris.data


# In[4]:


silhouette_avgs = []
ks = range(2, 11)
for k in ks:
    kmeans_fit = cluster.KMeans(n_clusters = k).fit(iris_X)
    cluster_labels = kmeans_fit.labels_
    silhouette_avg = metrics.silhouette_score(iris_X, cluster_labels)
    silhouette_avgs.append(silhouette_avg)

    


# In[5]:


plt.bar(ks, silhouette_avgs)
plt.show()
print(silhouette_avgs)


# In[ ]:




