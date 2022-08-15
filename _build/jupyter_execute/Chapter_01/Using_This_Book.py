#!/usr/bin/env python
# coding: utf-8

# # How to Use this Book
# 
# This online resource contains many notebook files with executable code cells as well as descriptive Markdown cells. It is designed to be an active exploration of NWB data, but can be used in a few different ways.
# 
# ## Option 1: As a casual observer
# There's a lot of descriptive text in this book, as well as the code. If you're interested in seeing the overall flow of ideas without digging into the data yourself, feel free to peruse via the primary website: [nwb4edu.github.io](http://nwb4edu.github.io).
# 
# ## Option 2: Using cloud computing
# This, dear reader, is our preferred mode of interaction so that you really engage with the materials! And even here, you have two options:
# 
# ### DANDI Jupyter Hub
# [DANDI](https://www.dandiarchive.org/), a platform for publishing, sharing, and processing neurophysiology data funded by the BRAIN Initiative, has a platform called a [JupyterHub](https://jupyterhub.readthedocs.io/en/stable/). This JupyterHub (nicknamed the [Dandihub](http://hub.dandiarchive.org/)) allows you to run code on servers that they are supporting. There are instructions on the setup page for how to get the code in this book into the Dandihub.
# 
# **Note**: Regardless of whether or not you're using the code on the DANDI Jupyter Hub, we'll be using dandi to interact with NWB datasets.
# 
# ### Colab or Binder
# If you're viewing this page from nwb4edu.github.io, you'll see a little rocket icon on the top of your screen. The little rocket button will offer two options: Google Colab or Binder. Which you use is up to you, but we generally find Google Colab to be faster to load and to install packages. 
# 
# When you try to run your first cell in Colab, it will tell you that your notebook was not authored by Google -- that's okay! Click "Run Anyway." Saving notebooks in Colab is possible if you log into a Google account.
# 
# ## Option 3: Using your local Python environment
# As you would with other code bases, you can [clone the source code from Github](https://github.com/nwb4edu/nwb4edu-dandi) and go wild with your local Python install.
# 
# If you'd rather not clone the whole repository, you can use the good ol' copy and paste technique. Take caution, though: some, but not all, of the code snippets in this book will work on their own. Copy and paste into your own coding environment at your own risk.
# 
# <hr>
# 
# ## Additional tips
# 
# * If you're running the notebooks one after the other, keep in mind that **each notebook functions separately**. Any packages that are imported, variables that are created, etc. will need to be regenerated in each notebook.
# * Occassionally, a cell might produce a red warning message saying something is "**deprecated**." Don't fret! This is just a warning that something deep in the code *may not work soon*.  It usually does not mean it won't work for you now.
