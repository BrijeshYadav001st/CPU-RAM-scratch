#!/usr/bin/env python
# coding: utf-8

# # Author : Brijesh Yadav
#   

# # Gmail: bkumaryadav096@gmail.com

# # Date: 06 Oct 2021

# # !/usr/bin/env python

# In[1]:


import os
import psutil


# # Getting loadover15 minutes

# In[2]:



load1, load5, load15 = psutil.getloadavg()
  
cpu_usage = (load15/os.cpu_count()) * 100
  
print("The CPU usage is : ", cpu_usage)


# # gives a single float value

# In[3]:


psutil.cpu_percent()


# # gives an object with many fields

# In[4]:


psutil.virtual_memory()


# # you can convert that object to a dictionary 

# In[5]:


dict(psutil.virtual_memory()._asdict())


# # you can have the percentage of used RAM

# In[6]:


psutil.virtual_memory().percent


# # you can calculate percentage of available memory

# In[7]:


psutil.virtual_memory().available * 100 / psutil.virtual_memory().total


# # Getting % usage of virtual_memory 

# In[8]:


print('RAM memory % used:', psutil.virtual_memory()[2])


# # Thank You
