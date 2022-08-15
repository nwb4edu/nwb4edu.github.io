#!/usr/bin/env python
# coding: utf-8

# # Interactive NWB Data Exploration
# 
# As we saw in the last section, the NWB file contains a ton of information about the experiment, as well as the actual data. We can look through each of the groups in the NWB file to pull out this information, or we can use a handy widget created by the NWB team.
# 
# This widget will also let us take a sneak peak at the behavioral and neural data as well. As a first pass, it can be very useful to explore the dataset in this high level way. This allows you to inspect the data for quality, and look for any interesting trends. 
# 
# First, let's set up our notebook and read the NWB file that we previously downloaded.

# In[5]:


# import necessary packages
from pynwb import NWBHDF5IO
from nwbwidgets import nwb2widget

# set the filename
filename = '000006/sub-anm369962/sub-anm369962_ses-20170310.nwb'

# assign file as an NWBHDF5IO object
io = NWBHDF5IO(filename, 'r')

# read the file
nwb_file = io.read()

print('NWB file found and read.')
print(type(nwb_file))


# Below, we'll take advantage of the [`nwbwidgets` package](https://github.com/NeurodataWithoutBorders/nwb-jupyter-widgets) to explore the data. This package usefully automatically renders information and visualizations of the data, depending on what it is. We'll use the nwb2widget function to explore the dataset we read above.
# 
# To take a peek at the neural data here, you can look under the "Units" header below. 

# In[4]:


nwb2widget(nwb_file)


# ### Questions for consideration
# * What is the raw data being used to plot the visualizations in "units"? What is this data showing us?
# * What kinds of visualizations do you see under "units"? Which of these are summary visualizations, versus more raw visualizations?
# * Do you see any interesting trends in the data?

# ### Chapter Wrap Up
# 
# In this chapter, we showed you how to explore an NWB file. We discussed common elements in the structure, and how you can use `nwbwidgets` to explore the data at a high level. 
# 
# Hopefully now you can:
# 
#     ✔️ Explain the three common features of datasets: metadata, raw data, and processed data
# 
#     ✔️ Identify and implement multiple ways to obtain a NWB dataset via DANDI
# 
#     ✔️ Explore the metadata contained in a typical Dandiset
# 
#     ✔️ Use an interactive widget for a big picture view of a Dandiset
# 
# In the following chapters, we'll demonstrate different kinds of visualizations and analyses that you might do with the data.
# 
# Before moving on, try the chapter problem set to test your understanding and to put some of these new skills to work. 💪

# ### Additional Resources
# * [Ben Dichter provides an overview of NWBWidgets](https://training.incf.org/lesson/nwbwidgets-inteactively-exploring-nwb-files)
