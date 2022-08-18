#!/usr/bin/env python
# coding: utf-8

# # Lesson #2 Problem Set
# 
# 1. In 4.1, we performed simple spike sorting using threshold detection and then feature extraction on one channel (index 99) in the Giocomo dataset. Use the same code to look at a different channel, index 89, and do the following:
# 
#     * Zoom in on this data to show about one second of the recording by changing the `xlim` on the plot. How does this change your interpretation of this signal?
#     * Run the spike detection & feature extraction code as is. How many units does this suggest there are?
#     * Take a closer look at the recommended threshold and lower it (make it closer to zero). How does this change your conclusions? Does the amplitude feature extraction capture the two different waveforms well?
# 
# 
# 2. In 4.2, we created two functions. One of these functions plots binned firing rates over time. Modify this function to accept a NumPy array that is neurons x spike times, and to plot an average firing rate of all neurons over time. Bonus: add a shaded standard deviation around your average firing rate.
# 
# 3. In 4.2, we looked at the Economo & Svoboda (2018) extracellular data and produced a table of trial times. In 4.2, we showed how to plot a PSTH for single neurons. Use the `interval_trial` table we created in 3.2 to find trials where the mouse either had a "correct" or "incorrect" response. Take an average of firing rates across all neurons in the incorrect and correct trials, and plot. Is there a difference?
# 
# 4. Create a plot that compares the average firing rate for each brain area.
