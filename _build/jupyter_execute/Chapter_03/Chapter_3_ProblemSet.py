#!/usr/bin/env python
# coding: utf-8

# # Chapter 3 Problem Set
# 
# 1. In 3.1, we created two functions. One of these functions plots binned firing rates over time. Modify this function to accept a NumPy array that is neurons x spike times, and to plot an average firing rate of all neurons over time. Bonus: add a shaded standard deviation around your average firing rate.
# 
# 2. In 3.1, we looked at the Economo & Svoboda (2018) extracellular data and produced a table of trial times. In 3.2, we showed how to plot a PSTH for single neurons. Use the `interval_trial` table we created in 2.2 to find trials where the mouse either had a "correct" or "incorrect" response. Take an average of firing rates across all neurons in the incorrect and correct trials, and plot. Is there a difference?
# 
# 3. Create a plot that compares the average firing rate for each brain area.
# 
# 4. Using the `spykes` package, create a plot that is a peristimulus histogram for all gabor stimuli at 90 degrees.
# 
# 5. Use the code provided in 3.3 to compare the waveforms of Sst+ cells with non-Sst+ cells and PV+ cells. Are they the same?
