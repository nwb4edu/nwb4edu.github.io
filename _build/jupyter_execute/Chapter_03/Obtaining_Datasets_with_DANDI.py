#!/usr/bin/env python
# coding: utf-8

# # Obtaining Datasets with DANDI

# [DANDI](https://www.dandiarchive.org/) is an open source data archive for neuroscience datasets, called **Dandisets**. DANDI allows scientists to submit and download neural datasets to promote research collaboration and consistent and transparent data standards. DANDI also provides a solution to the difficulties that come from housing data in the many other general domains (i.e. Dropbox, Google Drive, etc.). Usefully for our purposes here, many of the datasets on DANDI are in NWB format. If you'd like to know more about DANDI, check out the [DANDI handbook](https://www.dandiarchive.org/handbook/).
# 
# There are two primary ways to work with Dandisets:
# 1. You can **download the datasets**, either via the [DANDI Web Application](https://gui.dandiarchive.org/#/dandiset) or using the DANDI Python client below. If you download via the website, you'll need to create an account.
# 2. You can **stream datasets directly** from DANDI. We'll show you how to do this online as well as on your local computer.
# 
# Below, we demonstrate how to do both of these. For additional information on either of these methods, please refer to the [DANDI documentation](https://gui.dandiarchive.org/). 

# ## Option 1: Downloading Dandisets using Python 

# The cell below will download [this dataset](https://gui.dandiarchive.org/#/dandiset/000006) from DANDI. This dataset contains 32-channel extracellular recordings from mouse cortex. We're using the [`download`](https://dandi.readthedocs.io/en/latest/cmdline/download.html) tool from dandi below.
# 
# <mark>**Note:** Downloading this dataset may take several minutes, depending on your internet connection.</mark>
# 
# <mark>**Note #2:** This step is *only possible* after completing the setup steps.

# In[1]:


from dandi.download import download as dandi_download
import os 

# Set the URL for the DANDI file
url = 'https://dandiarchive.org/dandiset/000006/draft'

# Download the file into the current working directory
# It will skip downloading any files you've already downloaded
dandi_download([url], output_dir = os.getcwd(), existing = "skip")


# Once the cell above completes running, you will see a new folder 📁"00006" wherever you're running this notebook. Usefully, the code above will also print a list of individual NWB files that have been downloaded in this folder.
# 
# **Once the data is done downloading, you're ready for the next step.**

# ## Option 2: Streaming the Dandiset
# 
# The folks at NWB have also developed a clever way to stream Dandisets so that small bits of them can be viewed without downloading the entire dataset. This is particularly useful for very large datasets! **This step is optional, and maybe a better option if you have limited hard drive space and/or are having issues with Option 1 above.**
# 
# 
# #### Streaming via the DANDI hub
# The easiest way to stream data is via the DANDI Jupyter Hub (https://hub.dandiarchive.org/). There are setup steps for this in Chapter 1. The code below should work without a hitch.
# 
# #### Streaming locally, after configuring your environment
# With some configuration, you can stream data on your local computer. First, you need to set up your environment with the right version of a package called `h5py`. [There are instructions here for how to do that](https://pynwb.readthedocs.io/en/stable/tutorials/advanced_io/streaming.html#sphx-glr-tutorials-advanced-io-streaming-py). Once you're done, you can restart the kernel for this notebook, and run the code below.
# 
# 
# ### Code for Data Streaming
# First, we need to figure out the correct URL for the dataset on the Amazon S3 storage system. There is a tool to do so within the dandiapi, which we'll use below to get the URL for one session from the data we downloaded above.

# In[2]:


from dandi.dandiapi import DandiAPIClient

dandiset_id = '000006'  # ephys dataset from the Svoboda Lab
filepath = 'sub-anm372795/sub-anm372795_ses-20170718.nwb'  # 450 kB file

with DandiAPIClient() as client:
    asset = client.get_dandiset(dandiset_id, 'draft').get_asset_by_path(filepath)
    s3_path = asset.get_content_url(follow_redirects=1, strip_query=True)
    
print(s3_path)


# Now, we can read this path, but we'll stream it, rather than downloading it! The cell below will print some of the data about this experiment. It uses another package, [**PyNWB**](https://pynwb.readthedocs.io/en/stable/index.html), which is specifically designed to work with NWB files in Python. As you might expect, this won't be the last time we see this package. Below, we'll use the `NWBHDF5IO` class from this package, which will allow us to read NWB files.
# 
# <mark>**Note**: The code below *will not work* unless you're on the Dandihub or have properly configured your environment. See above.

# In[3]:


from pynwb import NWBHDF5IO

with NWBHDF5IO(s3_path, mode='r', load_namespaces=True, driver='ros3') as io:
    nwbfile = io.read()
    print(nwbfile)
    print(nwbfile.acquisition['lick_times'].time_series['lick_left_times'].data[:])


# In addition, we can use a fancy widget to create an interactive display of this dataset while we are streaming it. More on this [later](https://nwb4edu.github.io/Chapter_03/Interactive_NWB_Data_Exploration.html)!

# In[ ]:


from nwbwidgets import nwb2widget

nwb2widget(nwbfile)


# The following section will go over the the structure of an NWBFile and how to access data from this new file type. 
