#!/usr/bin/env python
# coding: utf-8

# # Visualizing Large Scale Recordings
# Now that we are familiar with the structure of an NWB file as well as the groups encapsulated within it, we are ready to work with the data. In this chapter you will learn to search the NWB file for its available data and plot visualizations such as raster plots.
# 
# Below, we'll import some now familiar packages and once again work with the dataset we obtained in Chapter 3. This should look very familiar to you by now!
# 
# <mark>**Note**: The code below will only work if you downloaded this NWB dataset in Chapter 3.</mark>

# In[1]:


# import necessary packages
from pynwb import NWBHDF5IO
from nwbwidgets import nwb2widget
import matplotlib.pyplot as plt
import numpy as np

# set the filename (slightly modified to ensure it looks in chapter 03 for the data)
filename = '../Chapter_03/000006/sub-anm369962/sub-anm369962_ses-20170310.nwb'

# assign file as an NWBHDF5IO object
io = NWBHDF5IO(filename, 'r')

# read the file
nwb_file = io.read()

print('NWB file found and read.')
print(type(nwb_file))


# The first group that we will look at is `units` because it contains information about spikes times in the data. This time, we will subset our dataframe to only contain neurons with `Fair` spike sorting quality. This means that the researchers are more confident that these are indeed isolated neurons.  
# 
# > Need a refresher on how we subset a dataframe? Review the Pandas page.

# In[2]:


# Get the units data frame
units_df = nwb_file.units.to_dataframe()
 
# Select only "Fair" units
fair_units_df = units_df[units_df['quality']=='Fair']

# Print the subsetted dataframe
fair_units_df.head()


# The `spike_times` column contains the times at which the recorded neuron fired an action potential. Each neuron has a list of spike times for their `spike_times` column. Below, we'll return the first 10 spike times for a given neuron. 

# In[3]:


# Return the first 10 spike times for your neuron of choice
unit_id = 5
print(units_df['spike_times'][unit_id][:10])


# A **spike raster plot** can be created using the function `plt.eventplot`. A spike raster plot displays the spiking of neurons over time. In a raster plot, each row corresponds to a different neuron or a different trial, and the x-axis represents the time. Each small vertical line in the plot represents the spiking of a neuron. Spike raster plots are useful as they reveal firing rate correlations between groups of neurons. For more information on `plt.eventplot` please visit the <a href = 'https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.eventplot.html'> matplotlib documentation</a>. 
# 
# Below, we'll create a function called `plot_raster()` that creates a raster plot from the `spike_times` column in `units`. `plot_raster()` takes the following arguments:
# 
# - `unit_df`: dataframe containing spike time data
# - `neuron_start`: index of first neuron of interest 
# - `neuron_end`: index of last neuron of interest
# - `start_time`: start time for desired time interval (in seconds)
# - `end_time`: end time for desired time interval (in seconds)

# In[4]:


# Function for creating raster plots for Units group in NWB file 
def plot_raster(units_df,neuron_start,neuron_end,start_time,end_time): 
    '''
    Takes a dataframe containing the units group of a nwb file (units_df) and creates 
    a raster plot with a given set of neurons (indexed by neuron_start, neuron_end) and a start and end time.
    '''
    
    neural_data = units_df['spike_times'][neuron_start:neuron_end] # Select the data
    num_neurons = neuron_end - neuron_start # Calculate # of neurons
    my_colors = ['C{}'.format(i) for i in range(num_neurons)]  #Generate a list of colors (C0, C1...)
    
    plt.eventplot(neural_data,colors=my_colors)  # Plot our raster plot 

    plt.xlim([start_time,end_time]) # Set axis limits to only include points in our data
    
    # Label our figure 
    plt.title('Spike raster plot')
    plt.ylabel('Neuron #')
    plt.xlabel('Time (s)')
    plt.yticks(np.arange(0,num_neurons))
    plt.show()

# Use our new function
plot_raster(units_df, neuron_start = 2, neuron_end = 11, start_time = 330, end_time = 335)


# The plot above is only contains neural spikes from nine neurons in a five second time interval. While there are many spikes to consider in this one graph, each neuron has much more than five seconds worth of spike recordings! To summarize these spikes over time, we can compute a **firing rate**.

# ## Binning Firing Rates 

# Raster plots are great for seeing individual neural spikes, but difficult to see the overall firing rates of the units. To get a better sense of the overall firing rates of our units, we can bin our spikes into time bins of 1 second using the function below, `plot_firing_rates()`.

# In[5]:


def plot_firing_rates(spike_times, start_time = None, end_time = None):
    '''
    plots the binned firing rate for the spike times in the list it is given in 1 second time bins.

    Parameters
    ----------
    spike_times : list
                  spike times, in seconds

    start_time  : int
                  start time for spike binning in seconds; sets lower-most bound for x axis
                  
    end_time    : int
                  end time for spike binning in seconds ; sets upper-most bound for x axis
    '''
    
    # Assign total number of bins 
    num_bins = int(np.ceil(spike_times[-1]))
    binned_spikes = np.empty(num_bins)
  
    # Assign the frequency of spikes over time
    for j in range(num_bins):
        binned_spikes[j] = len(spike_times[(spike_times>j)&(spike_times<j+1)])
          
    plt.plot(binned_spikes)
    plt.xlabel('Time (s)')
    plt.ylabel('Firing Rate (Hz)')
        
    if (start_time != None) and (end_time != None):
        plt.xlim(start_time, end_time)


# Let's use the function we just created to plot our data. Below, we will store all of the spike times from the same unit as above as `single_unit` and plot the firing rates over time.

# In[6]:


# Plot our data
single_unit = units_df['spike_times'][unit_id]
plot_firing_rates(single_unit,300,500)
plt.show()


# <font color="red">Note: I'm considering making this a 'problem set' activity rather than an example here.</font>
# 
# ## Compare firing rates at different depths of cortex
# 
# The units in our data were recorded from various cortical depths, therefore we can compare the firing units from differing cortical depths to test for differing firing rates. Let's first take a look at the distribution of depth from our units.

# In[7]:


# Plot distribution of neuron depth 
plt.hist(units_df['depth'], bins=30)
plt.title('Distribution of depth')
plt.xlabel('Depth (\u03bcm)') # The random letters in here are to create a mu symbol using unicode
plt.ylabel('Frequency')
plt.show()


# We will compare one unit recorded from 1165 microns to one unit recorded from 715 microns.

# In[8]:


# Assign dataframes for different depths 
depth_1165 = units_df[units_df['depth']==1165]
depth_715 = units_df[units_df['depth']==715]

# Create list of containing 1 entry from each depth
neural_list_1165 = depth_1165['spike_times'].iloc[0]
neural_list_715 = depth_715['spike_times'].iloc[0]

# Plot firing rates
plot_firing_rates(neural_list_1165, 300, 500)
plot_firing_rates(neural_list_715, 300, 500)
plt.legend(['1165','715'])
plt.show()


# It looks like the neuron that's more superficial (at a depth of 715 microns) has a higher firing rate! But we'd certainly need more data to make a conclusive argument about that.
# 
# <hr>
# 
# ## Additional resources
# 
# For more ideas about how to play with this dataset, see this [Github repository](https://github.com/vathes/DJ-NWB-Economo-2018/blob/master/notebooks/Economo-2018-examples.ipynb).
# 
# <font color="red">Note: Reproducing the above analysis, comparing left vs right in the upper ALM PT neurons would be fantastic...</font>
