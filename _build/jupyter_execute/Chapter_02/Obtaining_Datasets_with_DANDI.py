#!/usr/bin/env python
# coding: utf-8

# # Obtaining Datasets with DANDI

# [DANDI](https://www.dandiarchive.org/) is an open source data archive for neuroscience datasets, called **Dandisets**. DANDI allows scientists to submit and download neural datasets to promote research collaboration and consistent and transparent data standards. DANDI also provides a solution to the difficulties that come from housing data in the many other general domains (i.e. Dropbox, Google Drive, etc.). Usefully for our purposes here, many of the datasets on DANDI are in NWB format. If you'd like to know more about DANDI, check out the [DANDI handbook](https://www.dandiarchive.org/handbook/).
# 
# There are two primary ways to work with Dandisets:
# 1. You can **download the datasets locally**, either via the [DANDI Web Application](https://gui.dandiarchive.org/#/dandiset) or using the DANDI Python client below. If you download via the website, you'll need to create an account.
# 2. You can **stream datasets directly** from DANDI.
# 
# Below, we demonstrate how to do both of these. For additional information on either of these methods, please refer to the [DANDI documentation](https://gui.dandiarchive.org/). 

# ## Option 1: Downloading Dandisets using Python 

# First, we need to ensure that you have the [`DANDI` client](https://pypi.org/project/dandi/) installed on your computer. The cell below will try to import DANDI. If you have an old version of DANDI, it will prompt you to install a newer version. Type "Y" if you would like to install a new version (this is recommended). If you don't have DANDI at all, it will install the most recent version.

# In[1]:


try:
    import dandi
    if dandi.__version__>='0.35.0':
        print('DANDI installed & imported.')
    else:
        response = input('Old version of DANDI installed. Would you like to install a newer version of DANDI? (Y/N)')
        if response == 'Y':
            get_ipython().system('pip install --upgrade dandi')
except ImportError as e:
    get_ipython().system('pip install dandi')


# The cell below will download [this dataset](https://gui.dandiarchive.org/#/dandiset/000006) from DANDI. This dataset contains 32-channel extracellular recordings from mouse cortex. If you have previously run this cell, you do not need to run it again.
# 
# <mark>**Note:** Downloading this dataset may take several minutes, depending on your internet connection.</mark>

# In[2]:


from dandi.download import download as dandi_download
import os 

#url = "https://gui.dandiarchive.org/#/folder/5e72b6ac3da50caa9adb0498"
url = 'https://dandiarchive.org/dandiset/000006/draft'
dandi_download([url], os.getcwd(), existing="skip")

# Alternate way below -- this does not enable "skip" option
#!dandi download https://dandiarchive.org/dandiset/000006/draft


# Once the cell above completes running, you will see a new folder 📁"00006" wherever you're running this notebook. Usefully, the code above will also print a list of individual NWB files that have been downloaded in this folder.
# 
# **Once the data is done downloading, you're ready for the next step.**

# ## Option 2: Streaming the Dandiset
# 
# The folks at NWB have also developed a clever way to stream Dandisets so that small bits of them can be viewed without downloading the entire dataset. This is particularly useful for very large datasets! **This step is optional, and maybe a better option if you have limited hard drive space and/or are having issues with Option 1 above.**
# 
# ### Configuring your environment
# 
# With some configuration, you can use this method on your local computer. First, you need to set up your environment with the right version of a package called `h5py`. [There are instructions here for how to do that.](https://pynwb.readthedocs.io/en/stable/tutorials/advanced_io/streaming.html#sphx-glr-tutorials-advanced-io-streaming-py). Once you're done, you can restart the kernel for this notebook, and run the code below.
# 
# ### Streaming via the DANDI hub
# Alternatively, you can run the code below on the DANDI Jupyter Hub (https://hub.dandiarchive.org/). **JupyterHub** is an online coding environment in which you can run code on a remote server. Usefully, the folks at DANDI have set up a JupyterHub so that you can easily access the tools and data. To do so, follow these directions:
# 1. If you do not have already, set up a [GitHub account](https://github.com/signup). It's free, and it's a great way to start tracking your code!
# 2. Go to the Dandihub at [https://hub.dandiarchive.org/](https://hub.dandiarchive.org/) and log in using your GitHub account.
# 3. Choose "Base" as your server option.
# 4. Create a new Python 3 notebook and copy and paste the three code cells below.
# 
# 
# ### Code for Data Streaming
# First, we need to figure out the correct URL for the dataset on the Amazon S3 storage system. There is a tool to do so within the dandiapi, which we'll use below to get the URL for one session from the data we downloaded above.

# In[3]:


from dandi.dandiapi import DandiAPIClient

dandiset_id = '000006'  # ephys dataset from the Svoboda Lab
filepath = 'sub-anm372795/sub-anm372795_ses-20170718.nwb'  # 450 kB file

with DandiAPIClient() as client:
    asset = client.get_dandiset(dandiset_id, 'draft').get_asset_by_path(filepath)
    s3_path = asset.get_content_url(follow_redirects=1, strip_query=True)
    
print(s3_path)


# Now, we can read this path, but we'll stream it, rather than downloading it! The cell below will print some of the data about this experiment.

# In[4]:


from pynwb import NWBHDF5IO

with NWBHDF5IO(s3_path, mode='r', load_namespaces=True, driver='ros3') as io:
    nwbfile = io.read()
    print(nwbfile)
    print(nwbfile.acquisition['lick_times'].time_series['lick_left_times'].data[:])


# In addition, we can use a fancy widget to create an interactive display of this dataset. More on this later!

# In[ ]:


from nwbwidgets import nwb2widget

nwb2widget(nwbfile)


# The following section will go over the the structure of an NWBFile and how to access data from this new file type. 
