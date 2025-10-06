---
title: 'nwb4edu: an Online Textbook for Teaching and Learning with NWB Datasets'

tags:
  - Python
  - neuroscience
  - open data
  - Neurodata Without Borders
authors:
  - name: Ashley L. Juavinett
    orcid: 0000-0003-0872-7098
    affiliation: 1
  - name: Victor Magdaleno
    affiliation: 2
affiliations:
 - name: UC San Diego, Neurobiology
   index: 1
 - name: UC San Diego, Cognitive Science
   index: 2
date: 10 October 2024
bibliography: paper.bib

---

# Summary
The ``nwb4edu`` online textbook provides an interactive set of lessons for educators, students, and self-guided learners who would like to use open neuroscience datasets for research and/or teaching. Specifically, it introduces users to Neurodata Without Borders (NWB), a relatively new data format for neurophysiology data [@rubel_neurodata_2022; @teeters_neurodata_2015] which can be accessed via [DANDI (Distributed Archives for Neurophysiology Data Integration)](https://about.dandiarchive.org/). The ``nwb4edu`` textbook contains tutorials within an interactive JupyterBook [@executable_books_project_2021_4539666] that enable users to wrangle, analyze, and visualize NWB datasets. The datasets featured in this resource currently include rodent behavioral data, single-cell and extracellular electrophysiological recordings, and two-photon imaging experiments. Importantly, it also provides users with the necessary conceptual background to understand how the data was collected and how it can be analyzed. The broad understanding of how a dataset is structured and how to navigate a dataset can be applied to other data standards, while the in-depth understanding of NWB datasets can empower students and researchers to conduct their own research using these data. 

Each lesson contains learning objectives, tasks, and a problem set so that students can test and extend their skills. Executable notebooks can be launched on a pre-configured JupyterHub, making these easily accessible to anyone with an internet connection. All of the materials are covered by a CC-BY-SA-4.0 and are available at http://nwb4edu.github.io. 

In its current form, there are four complete lessons, which contain multiple notebooks. Each lesson contains specific learning objectives, such as:

* Identify and implement multiple ways to obtain a NWB dataset via DANDI
* Explore the metadata contained in a typical Dandiset and explain the three common features of datasets: metadata, raw data, and processed data
* Implement spike sorting on extracellular recording data
* Generate and interpret common visualizations of extracellular recording data
* Access and visualize single-cell and two-photon neural data from the Allen Institute

Furthermore, there are a growing set of single notebook lessons ("Greatest Hits in Neuroscience") in which users can re-create figures from published scientific papers using their NWB-formatted data. These lessons transform foundational papers in neuroscience into living lessons, breathing new life into old data and inviting all students in to conduct authentic research.


## Statement of Need
There is an ongoing and enthusiastic movement in neuroscience to standardize data formats as a means of improving reproducibility and encouraging data reuse. NWB is one of these formats, and has proved itself to be an effective data standard to share, store, and build analysis tools for neuroscience data. The next generation of neuroscience researchers needs skills to work with data standards like NWB to perform data analyses, visualize neural data, and ultimately address pressing scientific questions. A standardized and accessible data format like NWB also opens possibilities for more easily integrating these cutting-edge datasets into the undergraduate or graduate classroom and can empower student-guided exploration. 

While many researchers have acknowledged the expanding intersection of data science and neuroscience, there are very few educational resources to help students and educators grow these skill sets. There are a multitude of introductory programming resources and several notable modules for learning how to code alongside neural data, but fewer advanced resources for neural data science. To meet this need, the ``nwb4edu`` online workbook provides a set of exercises -- for anyone from an advanced undergraduate to an early career researcher -- who wishes to learn how to access, manipulate, and visualize NWB datasets.  If we want open science and data standardization to be the future, we need to train our students accordingly and provide researchers with open access tools so that they can easily adapt data into their pipelines.

These materials are designed to be adapted as individual modules, so that instructors or self-guided learners may choose what best suits their learning needs. The project is entirely open access and can be tailored for different experience levels or modified to address specific learning objectives.


## Instructional Design

The creation of this book was supported and motivated by a Kavli Foundation Seed Grant which supported the senior author (A.L.J.) to create a learner-facing resource for NWB datasets. Two of the lesson plans within, involving the Allen Institute data, were  created and tested with under students in various neurobiology courses at UC San Diego. These were the first lessons in the new ``nwb4edu`` book. We then built the two lessons focusing on native NWB format, with the goal of introducing students to the mechanics of a standardized data format as well as conducting very common neural data analyses and visualizations with the data. These native NWB lessons have been used in a Neural Data Science course for undergraduate and graduate students at UC San Diego. Finally, in collaboration with the NWB team, we integrated two additional "Greatest Hits" lessons. These lessons have not been used by any of the authors in a course setting.

## Acknowledgements
We would like to thank the Kavli Foundation, specifically program officer Stephanie Albin, for supporting this project. We would also like to thank Ben Dichter, Oliver Rübel, and Ryan Ly for feedback and technical support.


## References
