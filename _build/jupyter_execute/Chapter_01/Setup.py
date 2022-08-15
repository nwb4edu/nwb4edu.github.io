#!/usr/bin/env python
# coding: utf-8

# #  Setup
# 
# This notebook will ensure that your coding environment is set up for the interactive activities in this textbook.

# ## DANDIhub setup
# 
# As mentioned in "how to use this book," you can run the code in this book on the DANDI Jupyter Hub (https://hub.dandiarchive.org/). **JupyterHub** is an online coding environment in which you can run code on a remote server. Usefully, the folks at DANDI have set up a JupyterHub so that you can easily access the tools and data. To do so, follow these directions:
# 1. If you do not have already, set up a [GitHub account](https://github.com/signup). It's free, and it's a great way to start tracking your code!
# 2. Go to the Dandihub at [https://hub.dandiarchive.org/](https://hub.dandiarchive.org/) and log in using your GitHub account.
# 3. Choose "Base" as your server option.
# 4. Open a Terminal.
# 5. Type `git clone https://github.com/nwb4edu/nwb4edu-dandi` and enter.
# 6. Look for the new `nwb4edu-dandi` folder on the left side list of folders.
# 7. Double click on a notebook to open it!

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

