#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


my_list1 = [1,2,3,4]


# In[3]:


my_array1 = np.array(my_list1)


# In[4]:


my_array1


# In[5]:


my_list2 = [11,22,33,44]


# In[6]:


my_lists = [my_list1,my_list2]


# In[7]:


my_array2 = np.array(my_lists)


# In[8]:


my_array2


# In[10]:


my_array2.shape  #shpe 


# In[15]:


my_array2.dtype  #type


# In[17]:


np.ones([5,5])  #crate table with 1*5, 1*5


# In[19]:


np.eye(5) # matrikx 


# In[20]:


np.arange(5)


# In[21]:


np.arange(5,50,2)  #arange(start,stop,dtype)


# In[ ]:




