#!/usr/bin/env python
# coding: utf-8

# # Working with NWB in Python
# 
# On the previous page, we demonstrated how to obtain a dataset with DANDI. Now that you have a dataset downloaded, let's take a closer look at what it contains.
# 
# Working with our NWB file in Python requires yet another package, **PyNWB**. This is a package specifically designed to work with NWB files. As you might expect, this won't be the last time we see this package. Below, we'll use the `NWBHDF5IO` class from this package, which will allow us to easily read NWB files. For more information about PyNWB, [please read their documentation](https://pynwb.readthedocs.io/en/stable/index.html).
# 
# <mark>**Note**: This notebook will only work with the 2.10.0 version of the h5py package. The cell below will ensure that you have this version installed.</mark>
# 
# ## Step 1. Setup

# In[6]:


# Import modules from the PyNWB package
from pynwb import NWBHDF5IO

# This will ensure that the correct version of the h5py package is installed
try:
    import h5py
    if h5py.__version__ == '2.10.0':
         print('h5py version ' + h5py.__version__ + ' already installed')
    else:
        print(h5py.__version__ +' h5py installed; some features may not work.')
        
except ImportError as e:
    get_ipython().system("pip install h5py == '2.10.0'")


# ## Step 2. Read the NWB file
# 
# We can access the data in our NWB file in two steps:
# 
# 1. Assign our file as an NWBHDF5IO object
# 2. Read our file
# 
# The first step is done using the `NWBHDF5IO` class to create our `NWBHDF5IO` object and map our file to HDF5 format. Once we have done this, we can use the `read()` method to return our nwb file.
# 
# For more information on how to read NWB files, please visit the <a href = 'https://pynwb.readthedocs.io/en/stable/tutorials/general/file.html'> Reading an NWB file</a> section from the NWB Basics Tutorial. For more information on the NWBHDF5IO class, please visit the <a href = 'https://pynwb.readthedocs.io/en/stable/pynwb.html#pynwb.NWBHDF5IO'> pynwb package original documentation</a>.
# 
# <mark>**Note**: Each dataset may contain multiple NWB files for different subjects and sessions for a given experiment. Make sure you specify the exact file path to the single NWB file you wish to read. Below, we'll give the filename for one .nwb file within the folder that you downloaded in the last chapter.</mark>

# In[7]:


# read the NWB file
filename = '000006/sub-anm369962/sub-anm369962_ses-20170310.nwb'
io = NWBHDF5IO(filename, 'r')
nwb_file = io.read()
print('File found and read.')
print(type(nwb_file))


# ## Step 3. Access Groups, Datasets, and Attributes within the File Hierarchy
# 
# One of the first steps when working with a new dataset is to figure out what is in the dataset, and where. Each NWB file is composed of various groups, which either contain attributes of our file **metadata**) or entire datasets. Here are the main components:
# 
# ![NWB_file_structure.png](NWB_file_structure.png)
# 
# In order to see which groups are in our file, we can use the `fields` attribute to return a dictionary containing the the Groups of our NWB file. The dictionary **keys** are the various groups within the file which we will use to access the data we're ultimately interested in.

# In[8]:


# Get the Groups for the nwb file 
nwb_fields = nwb_file.fields
print(nwb_fields.keys())


# ### Experiment Metadata
# 
# Let's first pull out some metadata for the experiment we downloaded.
# 
# If you wish to access the related publications of the experimental data that you just downloaded, you can do so by accessing the `related_publications` attribute of your NWB file object. Plug in the "doi:" address that prints below into a browser window to check out the original publication describing this data.

# In[12]:


# Print the related publication
nwb_file.related_publications


# Each NWB file will also have information on where the experiment was conducted, what lab conducted the experiment, as well as a description of the experiment. These Groups can be accessed using `institution`, `lab`, and `experiment_description`, attributes on our nwb_file, respectively.

# In[10]:


# Get metadata from NWB file 
print('The experiment within this NWB file was conducted at ',nwb_file.institution,'.'      ,nwb_file.experiment_description)


# As you might have noticed at this point, we can access datasets from each group in our nwb_file with the following syntax: `nwb_file.GROUPNAME`, just as we would typically access an attribute of object in Python. Below we will demonstrate some of the most useful groups within an NWB object. 

# ### Acquisition 
# 
# The `acquisition` group contains datasets of acquisition data, mainly `TimeSeries` objects belonging to this NWBFile. 

# In[4]:


nwb_file.acquisition


# In this file, the acquisition group contains one dataset, `lick_times`. This dataset has one field, `time_series`, which contains two time series objects, `lick_left_times` and `lick_right_times`. To access the actual data arrays of these objects we must first subset our dataset of interest from the group. We can then use `timestamps[:]` to return a list of timestamps for when the animal licked.

# In[5]:


# select our dataset of interest 
dataset = 'lick_times'
field = 'lick_right_times'

lick_r_dataset = nwb_file.acquisition[dataset][field]

# return the first 10 values in data array 
lick_r_data_array = lick_r_dataset.timestamps[:10][:10]

print(lick_r_data_array)


# ### Intervals 
# 
# The `intervals` group contains all time interval tables from the experiment -- things like, did the animal respond on the behavioral trial? Usefully, we can take `intervals` and convert it to a tidy dataframe using `to_dataframe()`.

# In[8]:


# Select the group of interest from the nwb file 
intervals = nwb_file.intervals

# Pull out trials and assign it as a dataframe
interval_trials_df = intervals['trials'].to_dataframe()
interval_trials_df.head()


# In case you're wondering what these columns are, the `description` attribute provides a short description on each column of the dataframe.

# In[12]:


# return the description of each col in our dataframe
for col in interval_trials_df:
    print(col,':',intervals['trials'][col].description)


# ### Units
# 
# But wait, where's all of the neural data? The `units` group in our NWB file contains the neural activity of our individual neurons (**units**), including information about the spike sorting quality as well as the spike times -- when each of these cells fired an action potential. Much like the `intervals` group, `units` can also be assigned to a dataframe.

# In[10]:


units = nwb_file.units
units_df = units.to_dataframe()
units_df.head()


# If we'd like to know where these spikes are coming from, we can look at the `electrodes` attribute. The `electrodes` group contains metadata about the electrodes used in the experiment, including the location of the electrodes, the type of filtering done on that channel, and which electrode group the electrode belongs to. 

# In[11]:


# electrode positions 
electrodes = nwb_file.electrodes
electrodes_df = electrodes.to_dataframe()
electrodes_df.head()


# Wondering what something in this table is? We can once again dig out the descriptions:

# In[14]:


# return the description of each col in our dataframe
for col in electrodes_df:
    print(col,':',nwb_file.electrodes[col].description)


# Now that we have an idea of what this file contains, we can finally take a look at some of the data! We'll do that in the next chapter. 💃
# 
# 
# ## Additional Resources 
# For an in depth explanation of all groups contained within an NWB File object please visit the <a href = 'https://pynwb.readthedocs.io/en/stable/pynwb.file.html'> pynwb.file.NWBFile </a> section of the PyNWB documentation. 
