#!/usr/bin/env python
# coding: utf-8

# # Lesson #3: Single-Cell Electrophysiology

# While extracellular electrophysiology enables us to record from many neurons simultaneously, it cannot give us detailed information about single cells. Single-cell electrophysiology is conducted in two different ways: **intracellular**, where the electrode is inside of the cell, and **patch clamp**, where the electrode forms a continuous recording space with the inside of the cell.
#  
# The data in the Allen Cell Types Database was collected using whole-cell patch clamp. Patch clamp allows for very precise measurements of either whole-cell activity or specific ion channels. The video below shows what patch clamping looks like. 

# In[1]:


from IPython.display import YouTubeVideo
YouTubeVideo('mF7Vd5olw18')


# **About the Allen Brain Cell Types DataBase** 
# 
# The Allen Brain Cell Types dataset contains data recorded from cells using whole-cell patch clamp while injecting different current waveforms into to the cells. The dataset also includes many computed neuron metrics such as adaptivity, interspike interval, and spike rate, and interacelluar characteristics including like resting membrane potential, rheobase, and more. 
# 
# **Targeting different cell types**
# 
# How did the Allen Institute actually distinguish between different cell types? To do so, they capitalized on the fact that different cells in the brain often express different genes. With genetic engineering, we can express glowing proteins (such as green fluorescent protein) in cells that express a specific gene. This approach takes advantage of an enzyme called Cre recombinase, which is found in bacteriophages, but not mammals. When we artificially express Cre recombinase in a specific cell type and include LoxP sites around our glowing protein, the Cre recombinase comes and flips those LoxP sites around, leading to protein expression and a gorgeous glowing neuron. This system is called the [Cre-LoxP system](https://www.google.com/url?q=https%3A%2F%2Fwww.jax.org%2Fnews-and-insights%2F2006%2Fmay%2Fthe-cre-lox-and-flp-frt-systems&sa=D&sntz=1&usg=AOvVaw3Bd1-ytiLSqWA2QDto8bwT) and is one of the main tools that neuroscientists use to identify and target specific cells in the brain.
# 
# 
# **Learning objectives**
# 
# After completing this lesson, you'll be able to:
# * download single cell electophysiology data from the Allen Brain Cell Types Database
# * access and plot pre-computed features8
# * plot the morphology of single cells
# * compare different types of cells (i.e. spiny vs aspiny dendritic cells)

# **Additional Resources**
# 
# * The Allen Brain Cell Types Dataset uses hundreds of different Cre-driver lines. For a list of all the available lines, please visit the <a href = 'http://connectivity.brain-map.org/transgenic'> Transgenic Characterization</a> section of the Allen Mouse Connectivity site. 
