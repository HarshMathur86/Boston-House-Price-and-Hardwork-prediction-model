#!/usr/bin/env python
# coding: utf-8

# # Surface Plot | Data Visualisation
# Surface plots are used to 
#  - Vistalise loss fuction in Machine Learining
#  - Visualise State or State Value Function in Feinforcement Learning

# In[8]:


import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axis3d


# In[19]:


#a = np.array([1,2,3])
#b = np.array([4,5,6,7])

a = np.arange(-1, 1,0.02)
b = a

a, b = np.meshgrid(a, b)
#print(a, b, sep='\n\n')


# In[22]:


fig = plt.figure()
axes = fig.gca(projection='3d')
axes.plot_surface(a,b, a**2+b**2, cmap = 'rainbow')
#red denotes high value region 
#blue denotes low value region


# In[29]:


fig = plt.figure()
axes = fig.gca(projection='3d')
axes.contour(a,b, a**2+b**2, cmap = 'rainbow')
plt.title("Contour plot")
plt.show()


# In[ ]:




