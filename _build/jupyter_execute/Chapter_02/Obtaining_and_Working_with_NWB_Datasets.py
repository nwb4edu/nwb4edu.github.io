#!/usr/bin/env python
# coding: utf-8

# # Obtaining and Working with NWB Datasets
# 
# NWB datasets can be found in a few different places. Throughout this online textbook, we'll introduce two primary ways to obtain NWB datasets: through DANDI and through the Allen Institute SDK (Chapter X). In this chapter, we'll show you how to download a sample dataset via DANDI.
# 
# **Objectives for this Chapter**
# - [Obtain a NWB dataset via DANDI](https://nwb4edu.github.io/Chapter_02/Obtaining_Datasets_with_DANDI.html)
# - [Explore the metadata contained in a typical Dandiset](https://nwb4edu.github.io/Chapter_02/Working_with_NWB_format_in_Python.html)
# - Use an interactive widget for a big picture view of a Dandiset
# 
# **About the Neurodata Without Borders: Neurophysiology File Format**
# All of the datasets that we'll work with here are in the [Neurodata Without Borders: Neurophysiology (NWB:N)](https://www.nwb.org/nwb-neurophysiology/) format. NWB:N is the common standard to share, store, and build analysis tools for neuroscience data. NWB:N contains software to stadardize data, APIs to read and write data, and important datasets in the neuroscience community that have been converted to NWB format. As we'll see in our first dataset, NWB:N also includes factors such as experimental design, experimental subjects, behavior, data aquisition, neural activity, and extensions.
# 
# Several of the available NWB:N datasets are highlighted on the [NWB website](https://www.nwb.org/example-datasets/). 
# 
# In this chapter, we'll dig into one of the datasets that uses a technology known as Neuropixels to simultaneously record from many neurons. First, let's get the dataset.
