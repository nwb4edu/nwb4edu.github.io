#!/usr/bin/env python
# coding: utf-8

# #  Setup
# 
# This notebook will ensure that your coding environment is set up for the interactive activities in this textbook.

# ## Package Requirements
# 
# If you're *not* running the code on the Dandihub, then we have to ensure that your coding environment has all of the proper packages installed. The packages required are:
# 
# ```
# numpy==1.23.1
# dandi==0.45.1
# h5py==2.10.0
# ```
# 
# The code below will ensure that you have these packages or newer.
# 
# First, we need to ensure that you have the [`DANDI` client](https://pypi.org/project/dandi/) installed in your coding environment. The cell below will try to import DANDI. If you have an old version of DANDI, it will prompt you to install a newer version. Type "Y" if you would like to install a new version (this is recommended). If you don't have DANDI at all, it will install the most recent version.

# In[1]:


# This will ensure that the correct version of dandi is installed
try:
    import dandi
    if dandi.__version__>='0.45.1':
        print('Updated DANDI installed.')
    else:
        response = input('Old version of DANDI installed. Would you like to install a newer version of DANDI? (Y/N)')
        if response.upper() == 'Y':
            get_ipython().system('pip install --upgrade dandi')
except ImportError as e:
    get_ipython().system('pip install dandi')


# Next, we'll check for pyNWB, the python package for NWB.

# In[2]:


# Check for pywnb
try:
    import pynwb
    print('pyNWB installed.')
except ImportError as e:
    get_ipython().system('pip install pwynb')


# Finally, also need to make sure you have the correct version of NumPy.

# In[3]:


try:
    import numpy
    if numpy.__version__>='1.23.1':
        print('Updated NumPy installed.')
    else:
        response = input('Old version of NumPy installed. Would you like to install a newer version of NumPy? (Y/N)')
        if response.upper() == 'Y':
            get_ipython().system('pip install --upgrade numpy')
except ImportError as e:
    get_ipython().system('pip install numpy')

