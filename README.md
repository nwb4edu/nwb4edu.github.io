# nwb4edu: Teaching and Learning with NWB Datasets

[![License: CC BY-SA 4.0](https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-sa/4.0/)

An interactive online textbook for teaching and learning neuroscience using Neurodata Without Borders (NWB) datasets.

**Live Website:** [https://nwb4edu.github.io](https://nwb4edu.github.io)

## About This Project

The `nwb4edu` online textbook provides interactive and self-guided resources for educators, students, and self-guided learners who would like to use open neuroscience datasets for research and/or teaching. The textbook introduces users to [Neurodata Without Borders (NWB)](https://www.nwb.org/), a data standard for neurophysiology data, and teaches how to access, analyze, and visualize NWB datasets using Python.

### Key Features

- **Interactive Jupyter notebooks** with executable code
- **Comprehensive tutorials** covering data access, analysis, and visualization
- **Problem sets** for hands-on practice
- **Real datasets** from [DANDI Archive](https://dandiarchive.org/) and the [Allen Institute for Brain Science](https://alleninstitute.org/)
- **Greatest Hits lessons** that recreate figures from landmark neuroscience papers
- **Launch on JupyterHub** - no local installation required

## Content Overview

The textbook is organized into several sections:

### Introduction
- Using this book
- Environment setup
- Resources for educators

### Data Science in Python (Refresher)
- NumPy
- Pandas
- Matplotlib
- SciPy

### PyNWB Lessons
**Lesson 1:** Introduction to NWB format
- Obtaining datasets with DANDI
- Working with NWB format in Python
- Interactive NWB data exploration

**Lesson 2:** Large-scale electrophysiology
- Spike sorting
- Visualizing extracellular recordings

### AllenSDK Lessons
**Lesson 3:** Single-cell electrophysiology
- Obtaining data for single cells
- Analyzing computed features

**Lesson 4:** Two-photon calcium imaging
- Retrieving Brain Observatory data
- Analyzing two-photon data
- Correlations in neural activity

### Greatest Hits in Neuroscience
Recreate figures from foundational papers:
- Place fields (O'Keefe & Dostrovsky, 1971; Grosmark & Buzsáki, 2016)
- Rotational dynamics in motor cortex (Churchland et al., 2012)

## Using This Textbook

### For Students

The easiest way to use this textbook is through the live website at [https://nwb4edu.github.io](https://nwb4edu.github.io). You can launch any notebook directly on JupyterHub using the rocket icon in the top right corner of each page. No installation on your computer is required when using JupyterHub!

### For Local Development

If you want to run the notebooks locally:

1. Clone this repository:
```bash
git clone https://github.com/nwb4edu/nwb4edu.github.io.git
cd nwb4edu.github.io
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Launch Jupyter:
```bash
jupyter notebook
```

### For Educators

This textbook is designed to be modular - you can use individual lessons or entire sections in your courses. All materials are licensed under CC-BY-SA-4.0, so you're free to adapt and modify them for your teaching needs.

See our [For Educators](https://nwb4edu.github.io/Introduction/For_Educators.html) guide for more information on integrating these materials into your curriculum.

## Building the Book

This textbook is built using [Jupyter Book](https://jupyterbook.org/).

### Requirements

**Important**: Building the book requires **Python 3.11** due to AllenSDK compatibility requirements (AllenSDK requires numpy<1.24, which is incompatible with Python 3.12+).

1. Create a Python 3.11 environment:
```bash
conda create --name nwb4edu python=3.11 -y
conda activate nwb4edu
```

2. Install dependencies:
```bash
pip install -r requirements.txt
pip install -r requirements-docs.txt
```

### Build Process

To build the book locally:

```bash
jupyter-book build .
```

Or use the provided Makefile:

```bash
make build
```

To clean the build directory:

```bash
make clean
```

The built HTML files will be in `_build/html/`.

### Deploying to GitHub Pages

The book is automatically deployed to GitHub Pages when changes are pushed to the `master` branch. To manually deploy:

```bash
make deploy
```

This will build the book and push the HTML to the `gh-pages` branch.

## Repository Structure

```
nwb4edu.github.io/
├── _config.yml              # Jupyter Book configuration
├── _toc.yml                 # Table of contents
├── landing_page.ipynb       # Home page
├── Introduction/            # Getting started materials
├── Data_Science_In_Python/  # Python refresher lessons
├── Lesson_1/               # NWB format basics
├── Lesson_2/               # Electrophysiology analysis
├── Lesson_3/               # Single-cell data
├── Lesson_4/               # Two-photon imaging
├── Lesson_5/               # Greatest Hits recreations
├── requirements.txt         # Python package dependencies
└── requirements-docs.txt    # Documentation build dependencies
```

## Contributing

We welcome contributions from the community! Regardless of whether you want to report a bug, typo, or issue, suggest improvements to existing lessons, contribute new lesson content, or improve documentation, please see our [Contributing Guidelines](CONTRIBUTING.md) for more information.

### Getting Help

- **General questions:** Open a [discussion](https://github.com/nwb4edu/nwb4edu.github.io/discussions)
- **Bug reports:** Open an [issue](https://github.com/nwb4edu/nwb4edu.github.io/issues)
- **Direct contact:** Email Ashley Juavinett at ajuavine(at)ucsd(dot)edu

## Authors

- **Ashley L. Juavinett** - UC San Diego, Neurobiology (current project maintainer)
- **Victor Magdaleno-Garcia** - UC San Diego Alum, Cognitive Science

With thanks to Tommy Lee, Ariel Rokem, and Tom Donoghue for copyediting.

## Acknowledgements

This work is supported by a [Kavli Foundation Seed Grant](https://www.nwb.org/projects/) to increase access to Neurodata Without Borders datasets. We thank the Kavli Foundation, specifically program officer Stephanie Albin, for their support.

We also thank Ben Dichter, Oliver Rübel, and Ryan Ly for valuable feedback and technical support.

## License

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-sa/4.0/).

You are free to use and adapt these resources, but if you create derivative works, they should be distributed under the same license.

## Citation

If you use these materials in your teaching or research, please cite:

```
Juavinett, A.L., & Magdaleno-Garcia, V. (2024). nwb4edu: an Online Textbook for Teaching
and Learning with NWB Datasets. *Journal of Open Source Education: TENTATIVE*.
https://nwb4edu.github.io
```
