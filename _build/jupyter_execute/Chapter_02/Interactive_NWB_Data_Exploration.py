#!/usr/bin/env python
# coding: utf-8

# # Interactive NWB Data Exploration
# 
# As we saw in the last section, the NWB file contains a ton of information about the experiment, as well as the actual data. We can look through each of the groups in the NWB file to pull out this information, or we can use a handy widget created by the NWB team.
# 
# This widget will also let us take a sneak peak at the behavioral and neural data as well. As a first pass, it can be very useful to explore the dataset in this high level way. This allows you to inspect the data for quality, and look for any interesting trends. To take a peek at the neural data here, you can look under the "Units" header below. 
# 
# Below, we'll take advantage of the [`nwbwidgets` package](https://github.com/NeurodataWithoutBorders/nwb-jupyter-widgets) to explore the data. This package usefully automatically renders information and visualizations of the data, depending on what it is. We'll use the nwb2widget function to explore one of the datasets we downloaded earlier.

# In[2]:


from pynwb import NWBHDF5IO
from nwbwidgets import nwb2widget

# read the NWB file
fpath = '000006/sub-anm369962/sub-anm369962_ses-20170310.nwb'
nwb_file = NWBHDF5IO(fpath, 'r').read()


# In[3]:


nwb2widget(nwb_file)


# ### Additional Resources
# * [Ben Dichter provides an overview of NWBWidgets](https://training.incf.org/lesson/nwbwidgets-inteactively-exploring-nwb-files)
