# Contributing to nwb4edu

Thank you for your interest in contributing to nwb4edu! We welcome contributions from our community to help improve and build it.

## How to Contribute

There are many ways to contribute to this project:

### Reporting Issues

If you find a bug, typo, or have a suggestion for improvement:

1. Check if the issue already exists in our [issue tracker](https://github.com/nwb4edu/nwb4edu.github.io/issues)
2. If not, [open a new issue](https://github.com/nwb4edu/nwb4edu.github.io/issues/new)
3. Provide a clear description of the problem or suggestion
4. Include steps to reproduce (for bugs) or examples (for suggestions)

### Suggesting New Lessons

We're especially interested in expanding our "Greatest Hits" collection. If you have an idea for a lesson that recreates the analysis and figures from landmark neuroscience papers using NWB data:

1. Open an issue with the tag "new lesson"
2. Describe the paper and which figures you'd like to recreate
3. Identify the NWB dataset (from DANDI or elsewhere) that contains the relevant data
4. Outline the learning objectives

### Contributing Content

#### For Small Changes (typos, small fixes)

1. Fork the repository
2. Make your changes in a new branch
3. Submit a pull request with a clear description of the changes

#### For Larger Contributions (new lessons, major revisions)

1. Open an issue first to discuss your proposed changes
2. Wait for feedback from the maintainers
3. Once approved, fork the repository
4. Create a new branch for your work
5. Make your changes following our guidelines (see below)
6. Test your changes thoroughly
7. Submit a pull request

## Development Guidelines

### Setting Up Your Environment

1. Fork and clone the repository:
```bash
git clone https://github.com/YOUR-USERNAME/nwb4edu.github.io.git
cd nwb4edu.github.io
```

2. Install dependencies:
```bash
pip install -r requirements.txt
pip install -r requirements-docs.txt
```

3. Create a new branch for your work:
```bash
git checkout -b descriptive-branch-name
```

### Code Style Guidelines

#### Python Code
- Follow [PEP 8](https://pep8.org/) style guidelines
- Use snake_case for function and variable names (not CamelCase)
- Include docstrings for functions using numpy-style format:
```python
def process_data(data, threshold=0.5):
    """
    Process neural data by applying a threshold.

    Parameters
    ----------
    data : numpy.ndarray
        The input data array
    threshold : float, optional
        The threshold value (default: 0.5)

    Returns
    -------
    processed : numpy.ndarray
        The processed data
    """
    processed = data[data > threshold]
    return processed
```

- Use proper spacing around operators and after commas
- Keep lines under 100 characters when possible

#### Jupyter Notebooks
- Use markdown cells liberally to explain what you're doing
- Include comments in code cells for complex operations
- Test that all cells run in order without errors
- Include learning objectives at the beginning of each lesson
- End lessons with a summary or problem set

#### Markdown
- Use proper heading hierarchy (# for titles, ## for main sections, etc.)
- Include links to external resources where helpful

### Testing Your Changes

Before submitting a pull request:

1. Run all cells in any notebooks you've modified to ensure there are no errors
2. Build the book locally to check formatting:
```bash
jupyter-book build .
```
3. Open `_build/html/index.html` in a browser to review your changes

### Commit Messages

Write clear, descriptive commit messages:
- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests when relevant

Example:
```
Fix typo in Lesson 2 spike sorting tutorial

Corrected variable name from 'spiketimes' to 'spike_times'
for consistency with documentation.

Fixes #123
```

## Contributing New Lessons

If you're creating a new lesson, please include:

### Elements
1. **Learning objectives** - Clear, measurable goals for the lesson
2. **Introduction** - Context and motivation for the lesson
3. **Step-by-step tutorial** - Well-commented code with explanations and visualizations
4. **Problem set** - Exercises for students to practice (*optional*)
6. **References** - Citations for papers, datasets, and methods used

### Dataset Requirements
- Use openly available datasets (DANDI, Allen Institute, etc.)
- Include citation information for datasets
- Provide clear instructions for data access
- Consider data download size and accessibility
-     Is it small enough to sync on Github? Is it small enough to download? If neither of those are true, can it be streamed?

### Documentation
- Add your lesson to `_toc.yml`
- Include a `requirements.txt` file in your lesson folder if you use additional packages
- Update the main README.md if you're adding a major section

## Style Preferences
- **Code comments**: Be generous with comments, especially for complex analyses
- **Variable names**: Use descriptive names (e.g., `firing_rate` not `fr`)
- **Figures**: Include axis labels, titles, and legends where appropriate
- **Citations**: Use proper attribution for methods, datasets, and figures

## Getting Help

If you need help with your contribution:

- **Questions about content**: Open a discussion on GitHub
- **Technical issues**: Open an issue with the "help wanted" tag
- **Direct contact**: Email Ashley Juavinett at ajuavine(at)ucsd(dot)edu

## Recognition

Contributors will be acknowledged in:
- The project's README.md (for significant contributions)
- Individual lesson pages (for lesson authors)
