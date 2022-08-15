#!/usr/bin/env python
# coding: utf-8

# # Spike Sorting
# 
# When you record extracellular electrophysiology data, the first step is figuring out which action potentials (or "spikes") came from which neurons. The process of doing this is called **spike sorting**.
# 
# Below, we'll work with [this dataset](https://dandiarchive.org/dandiset/000053/0.210819.0345) from [Lisa Giocomo's lab at Stanford](https://giocomolab.weebly.com/) to demonstrate the simplest form of spike sorting: thresholding, followed by feature detection.
# 
# <mark>**Note**:  The code below requires a different dataset than the one we interacted with in the last chapter. Because this dataset contains all of the raw recording data, it is much, much bigger. As a result, the best way to work with it is through the Dandihub. Check out the Setup page for instructions on how to run this on the Dandihub.</mark>
# 
# First, we need to find the correct URL for the dataset on the NWB's Amazon S3 storage system. There is a tool to do so within the dandiapi, which we'll use below to get the URL for one session within the dataset.

# In[1]:


from dandi.dandiapi import DandiAPIClient

dandiset_id = '000053' # giocomo data
filepath = 'sub-npI5/sub-npI5_ses-20190414_behavior+ecephys.nwb' 

with DandiAPIClient() as client:
    asset = client.get_dandiset(dandiset_id, 'draft').get_asset_by_path(filepath)
    s3_path = asset.get_content_url(follow_redirects=1, strip_query=True)
    
print(s3_path)


# Now, we can read this path, but we'll stream it, rather than downloading it! Below, we'll print some useful information about this experiment. We will also access a dataset we haven't interacted with yet: "ElectricalSeries". As the name suggests, this contains raw electrophysiology data -- exactly what we need to sort! We will assign a portion of this to an object called `ephys_data`.

# In[2]:


from pynwb import NWBHDF5IO

with NWBHDF5IO(s3_path, mode='r', load_namespaces=True, driver='ros3') as io:
    nwbfile = io.read()
    print(nwb_file.experiment_description)
    print(nwbfile.acquisition['ElectricalSeries'].data.shape)
    sampling_freq = nwbfile.acquisition['ElectricalSeries'].resolution # get the sampling frequency in Hz
    ephys_data = (nwbfile.acquisition['ElectricalSeries'].data[:3000000, 99])*nwbfile.acquisition['ElectricalSeries'].conversion


# Before we dive into spike sorting, let's take a look at the data. Below, we'll import a couple additional packages, generate a list of timestamps, and plot it.

# In[ ]:


# import necessary packages
import numpy as np
import matplotlib.pyplot as plt

# generate a vector of timestamps
timestamps = np.arange(start=0,stop=100,1/sampling_frequency)

fig,ax = plt.subplots(1,1,figsize=(15,3))
plt.plot(timestamps,ephys_data)
plt.ylabel('Voltage (V)')
plt.xlabel('Seconds (s)')
#plt.xlim(1.053,1.055)
plt.show()


# In the data above,there are clear places where the data "spikes". These are extracellularly recorded action potentials!
# 
# One of the most straightforward ways to spike sort is to simply detect these using a threshold. Whenever the signal passes this threshold, we'll clip that out. We can determine a reasonable threshold using one rule of thumb: when the signal is 5 times the noise MAD, that's enough signal to noise that it's likely to be an action potential. We'll calculate that below.

# In[ ]:


noise_std = np.std(ephys_data)
noise_mad = np.median(np.absolute(ephys_data)) / 0.6745  # WHY .6745??
recommended_threshold = -5 * noise_mad
print('Noise Estimate by Standard Deviation: ', noise_std)
print('Noise Estimate by MAD Estimator     : ', noise_mad)
print('Recommended Spike Threshold         : ', recommended_threshold)


# The next few steps require more functions than we need to look at in detail. Below, we'll import those functions by running a script to create them. We'll then use the `%whos` magic command to see the functions we imported.

# In[4]:


get_ipython().run_line_magic('run', 'spikesorting_helperfunctions.py')
get_ipython().run_line_magic('whos', '')


# Now, we can use those functions to detect threshold crossings. Below, we'll use two separate functions `detect_threshold_crossings` and `align_to_minimum` to find these spikes. We'll then plot our original signal with the detected spikes marked.

# In[ ]:


crossings = detect_threshold_crossings(ephys_data, sampling_freq, recommended_threshold, 0.003) # dead time of 3 ms
spks = align_to_minimum(ephys_data, sampling_freq, crossings, 0.002) # search range 2 ms

fig = plt.figure(figsize=(20,5))
plt.plot(timestamps,ephys_data)
plt.xlabel('Time (s)')
plt.ylabel('Voltage (uV)')
plt.plot(spks,[recommended_threshold]*spks.shape[0], 'ro', ms=2)
plt.xlim([0,len(ephys_data)])
plt.show()


# Finally, we can cut out the waveforms from these detected spikes so that we can look at their shape. The location (the channel on the electrode shank) and shape of a waveform is one of the main pieces of evidence to show that the waveform was recorded from a cell. This will help us determine whether or not there is just one or more neurons recorded on this channel. 

# In[ ]:


pre = 0.001 # 1 ms
post= 0.002 # 2 ms
waveforms = extract_waveforms(ephys_data, sampling_freq, spks, pre, post)
plot_waveforms(waveforms, sampling_freq, pre, post, n=500)


# Looking at the plot above, would you say there is just one waveform here, or multiple?
# 
# Indeed, it looks like there might be two -- one that is very high amplitude, and another that is lower amplitude. We can use **feature detection** to investigate our waveforms. Below, we'll plot the minimum and maximum voltages in the recorded waveforms to see if there are distinct clusters of waveforms.

# In[ ]:


min_voltage = np.amin(waveforms, axis=1)
max_voltage = np.amax(waveforms, axis=1)

plt.figure(figsize=(8,8))
plt.plot(min_voltage, max_voltage,'.')
plt.xlabel('Minimum Voltage (V)')
plt.ylabel('Maximum Voltage (V)')
plt.title('Min/Max Spike Voltages')

plt.show()


# Looking at the scatterplot above, would you say there is more than one cluster of waveforms?
# 
# ### Notebook summary
# In this notebook, we've looked closely at just 100 seconds of one channel in a 384-channel recording. You can imagine how long spike sorting would take if we needed to do this for *all* of the data. Thankfully, there are more automated spikesorting tools which enable researchers to automatically sort their data, with just a little bit of sorting by hand. In the next notebook, we'll work with data that has already been sorted for us. The resulting data simply has spike times for each sorted neuron (or "unit") -- the moments in the experiment where a spike happened. This is the most common format for data sharing of extracellularly recorded data, since it's much more concise, and the hard work of spike sorting has already happened.

# ## Additional resources
# https://pynwb.readthedocs.io/en/stable/pynwb.ecephys.html
# 
# https://pynwb.readthedocs.io/en/stable/tutorials/domain/ecephys.html
