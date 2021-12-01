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
    if dandi.__version__>='0.32.0':
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


get_ipython().system('dandi download https://dandiarchive.org/dandiset/000006/draft')


# Once the cell above completes running, you will see a new folder 📁"00006" wherever you're running this notebook. Usefully, the code above will also print a list of individual NWB files that have been downloaded in this folder.

# ## Option 2: Streaming the Dandiset
# 
# The folks at NWB have also developed a clever way to stream Dandisets so that small bits of them can be viewed without downloading the entire dataset. First, you need to set up your environment with the right version of a package called `h5py`. [There are instructions here for how to do that.](https://pynwb.readthedocs.io/en/stable/tutorials/advanced_io/streaming.html#sphx-glr-tutorials-advanced-io-streaming-py). Once you're done, you can restart the kernel for this notebook, and run the code below.
# 
# First, we need to figure out the correct URL for the dataset on the Amazon S3 storage system. There is a tool to do so within the dandiapi, which we'll use below to get the URL for one session from the data we downloaded above.

# In[1]:


from dandi.dandiapi import DandiAPIClient

dandiset_id = '000006'  # ephys dataset from the Svoboda Lab
filepath = 'sub-anm372795/sub-anm372795_ses-20170718.nwb'  # 450 kB file
with DandiAPIClient() as client:
    asset = client.get_dandiset(dandiset_id, 'draft').get_asset_by_path(filepath)
    s3_path = asset.get_content_url(follow_redirects=1, strip_query=True)
    
print(s3_path)


# Now, we can read this path, but we'll stream it, rather than downloading it!

# In[2]:


from pynwb import NWBHDF5IO

with NWBHDF5IO(s3_path, mode='r', load_namespaces=True, driver='ros3') as io:
    nwbfile = io.read()
    print(nwbfile)
    print(nwbfile.acquisition['lick_times'].time_series['lick_left_times'].data[:])


# In[4]:


from nwbwidgets import nwb2widget

nwb2widget(nwbfile)


# The following section will go over the the structure of an NWBFile and how to access data from this new file type. 
