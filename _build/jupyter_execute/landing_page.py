#!/usr/bin/env python
# coding: utf-8

# # Teaching and Learning with NWB Datasets

# For many, many years in neuroscience, the landscape of file formats has been the wild west. Everyone either uses a format either dictated by their lab or by the equipment they’re using. This poses a huge challenge to data sharing: if you want to collaborate with the lab next door and share data with them, one of the first questions is, "what format is your data in?" While static images taken from a microscope and standard biology lab procedures like western blots are fairly straightforward to share, physiology and behavior data types are much more diverse.
# 
# That's where [Neurodata Without Borders](https://www.nwb.org/) (NWB) comes in. NWB is a consortium of researchers who are aiming to *standardize neuroscience data on an international scale.* The use of this standard dataset format will make sharing and contributing to open source projects easier, ultimately accelerating discovery.
# 
# NWB has pioneered a data format called [Neurodata Without Borders: Neurophysiology (NWB:N)](https://www.nwb.org/nwb-neurophysiology/). NWB:N is a standard to share, store, and build analysis tools for neuroscience data. It is built on [HDF5 (hierarchical data format)](http://davis.lbl.gov/Manuals/HDF5-1.8.7/UG/10_Datasets.html), which was designed for large data storage and multi-language accessibility. In other words, it’s good at doing exactly what we need it to do.
# 
# 
# ## Standardized data for education
# 
# A standardized and accessible data format like NWB also opens possibilities for more easily integrating these cutting-edge datasets into the classroom. **This online textbook aims to provide interactive and self-guided resources for educators, students, and self-guided learners who would like to use open neuroscience datasets for research and/or teaching.** Within, you'll find tutorials in the form of interactive Python notebooks that will enable you to wrangle and analyze NWB datasets. At the end of each chapter, there are problem sets so that you can test and extend your skills.
# 
# Along the way, we'll point you towards the prolific and tremendous documentation that the NWB team has already put together for you, for whenever you're ready to learn more.
# 
# 
# ## Using this textbook
# 
# This textbook is designed for educators, students, and self-guided learners who would like to work with NWB datasets. It expects that you have some knowledge of Python, though Chapter 2 will give you a refresher on the most pertinent information, if you need it. Throughout the book, you'll also find many recommendations for places to learn more.
# 
# Using the rocket icon in the top right corner, you can launch any of these notebooks in either Google Colab or Binder. There's much more information in Chapter 1 about how to set up your coding environment and interact with this textbook.
# 
# 
# ## Chapter outline
# 
# **Chapter 1** will set you up for success with options for interacting with these materials and some technical environment setup.
# 
# **Chapter 2** reviews some of the packages, data structures, and coding skills that we'll use throughout the rest of the book. You are welcome to skip this chapter if you're very comfortable in Python.
# 
# **Chapter 3** will give you important information about how to access and explore NWB files. 
# 
# **Chapters 4, 5, and 6** are self-contained and can be completed out of order, depending on which type of data you're most interested in working with.

# ## Support
# <img src="https://github.com/nwb4edu/nwb4edu.github.io/blob/master/The_Kavli_Foundation_Logo_Blue_Red.png?raw=true"
#      alt="Kavli Logo"
#      style="float: left; margin-right: 10px;"
#      width="500"/>
# <br clear="left"/>
# 
# This work is supported by a [Kavli Foundation Seed Grant](https://www.nwb.org/projects/) meant to increase the access to Neurodata Without Borders datasets.
# 
# <br clear="left"/>
# <img src="https://www.braininitiative.org/wp-content/uploads/2017/02/nwb.png"
#      alt="Kavli Logo"
#      style="float: left; margin-right: 10px;" />
# <br clear="left"/>
# 
# Many thanks to the NWB team, especially Ben Dichter, for their feedback and input.

# <hr>
# 
# ## Additional resources 
# There are several great online resources for neural data science beyond NWB formats:
# 
# - [Data Science in Practice](https://datascienceinpractice.github.io/)
# - [Neural Data Science by Nylen & Wallisch](https://www.sciencedirect.com/book/9780128040430/neural-data-science)
# - [Foundations of Data Science](https://www.inferentialthinking.com/chapters/intro.html)
# - [Computational Neuroscience](https://mrgreene09.github.io/computational-neuroscience-textbook/index.html), open textbook written by students
# - [Neuromatch Academy](http://www.neuromatchacademy.org/syllabus), online computational neuroscience course
# 
# <hr>

# ## License
# 
# This work is distributed under a [CC-BY-SA-4.0 license](https://creativecommons.org/licenses/by-sa/4.0/). You are free to use and adapt these resources, but if you generate a derivative of these resources, they should be distributed with a similar license.
