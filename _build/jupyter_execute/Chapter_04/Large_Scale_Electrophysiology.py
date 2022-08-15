#!/usr/bin/env python
# coding: utf-8

# # Large-Scale Electrophysiology
# 
# A single neuron cannot carry out complex tasks by itself -- it requires the surrounding, interconnected neurons to send and receive signals and accomplish the simplest of tasks. In modern large-scale electrophysiology, the activity of hundreds of neurons are recorded in an attempt to determine where neuron activity occurs and how these cells communicate with each other when presented with certain tasks.  
# 
# Many NWB datasets feature extracellular electrophysiology, with technology ranging from tetrodes to cutting-edge silicon recording probes. Regardless of the technology, the principles of dealing with extracellular electrophysiology data are very similar.
# 
# In this chapter, we'll explore an extracellular electrophysiology dataset.
# 
# ### Learning Objectives
# * Identify the processing steps in extracellular experiments
# * Implement spike sorting on extracellular recording data
# * Generate and interpret common visualizations of extracellular recording data
# 
# <hr>
# 
# 
# ## Background information
# 
# ### Introduction to Electrophysiology
# 
# **Electrophysiology** is the study of the electrical activity created by neurons. There are three main ways of collecting electrophysiology data: 
#  1. Extracellular Recordings: electrode outside of the cell
#  2. Intracellular Recordings: electrode inside of the cell 
#  3. Patch Clamp Recordings: electrode continuous with cell membrane
#  
# ![](https://www.researchgate.net/publication/349446871/figure/fig1/AS:993163909025795@1613800136978/Overview-of-the-patch-clamp-method-a-Comparison-between-extracellular-and.ppm)
# *From [Noguchi et al. 2021](https://www.researchgate.net/publication/349446871_In_Vivo_Whole-Cell_Patch-Clamp_Methods_Recent_Technical_Progress_and_Future_Perspectives) under a [Creative Commons 4.0 License](https://creativecommons.org/licenses/by/4.0/)
# 
# ### Processing Extracellular Recordings
# 
# Extracellular recordings are taken from outside of the cell, and are therefore a bit messier than intracellular recordings. In addition to filtering the data to remove any slow, non-biological shifts in the recorded potential, raw extracellular recordings also need to be spike sorted. Because these recordings are taken from outside of the cell, it's possible that each electrode may be listening to multiple cells nearby. **Spike sorting** allows us to identify action potentials ("spikes") and assign them to **units**, or *putative* neurons. In other words, we can't say with utmost certainty that we've correctly identified the source of our spikes, but we can use spatial and temporal information to say with some confidence that we *likely* have.
# 
# Thankfully, most of the data in NWB files have already been sorted for us. Most often, the authors of these files will provide a list of spike times for each unit, and we can use these spike times along with the behavioral and environmental context of the experiment to try to make some sense of what neurons are doing.
# 
# In addition to spike times, researchers are often interested in studying the **local field potential** (LFP), or the collective sum of all of the neurons in a given area. We can filter this LFP for particular brain waves, and even use it to distinguish between layers of cortex. 
# 
# <hr>
# 
# <img src="https://brainmapportal-live-4cc80a57cd6e400d854-f7fdcae.divio-media.net/filer_public/88/00/8800429b-8811-471f-9f04-82d19b3851b0/neuropixels_visual_coding_cms_images-04.png"
#      alt="Neuropixels Logo"
#      align="right"
#      float="left"
#      width="250"/>
# 
# ### Neuropixels Probes
# 
# In one section of this chapter, you'll encounter Neuropixels data from the Allen Institute for Brain Science. The technological advancement of the Neuropixels probe (seen at right) has significantly propelled systems neuroscience research in recent years ([Jun et al., 2017](https://www.nature.com/articles/nature24636)). Each probe is approximately the size of a strand of hair and has 960 recording sites allowing for hundreds of neurons to be recorded simultaneously. The reduced size of these recording devices allows for several probes to be inserted into the same brain, providing real time recordings of multiple brain areas.
# <br clear="left"/>
# 
# <hr>
# 
# ### Additional Resources
# * For a thorough overview of electrophysiology, see the [Guide to Research Techniques](https://www.sciencedirect.com/science/article/pii/B9780128005118000046).
# * To read more about the potential of Neuropixels probes, read this [Simons Foundation article](https://www.simonsfoundation.org/2018/01/04/neuropixels-offer-new-ways-to-map-cells/).
# * For technical information about the Neuropixel probes or to learn how to obtain them, please visit <a href = 'https://www.neuropixels.org/'> neuropixels.org</a>.

# 
