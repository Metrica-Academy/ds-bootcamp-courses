# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a comprehensive **Data Science Bootcamp Course Collection** containing three integrated educational modules designed to take students from complete beginners to job-ready data scientists. The repository includes installation materials, Python fundamentals, data science concepts, and a complete 6-month bootcamp curriculum.

## Repository Architecture

### Main Course Modules

1. **`installation-kit/`** - Complete setup and installation materials for absolute beginners
   - Cross-platform installation guides (Windows, Mac, Linux)
   - Conda environment specifications and verification scripts
   - Interactive troubleshooting documentation

2. **`python-fundamentals/`** - 3-week intensive Python course for complete beginners
   - Progressive lesson structure with live coding approach
   - Real-world analogies and hands-on projects
   - Comprehensive exercises and homework assignments

3. **`intro-to-data-science/`** - Interactive data science fundamentals with real datasets
   - Jupyter notebook-based learning with gamification
   - 10 synthetic datasets across multiple domains
   - Professional visualization and analysis tools

4. **`ds-bootcamp-curriculum/`** - Complete 6-month virtual bootcamp curriculum
   - 8 modules covering full data science pipeline
   - Project-based learning with portfolio development
   - Industry-standard tools and career preparation

## Common Development Commands

### Environment Setup and Management
```bash
# Install complete data science environment
conda env create -f installation-kit/environments/ds-bootcamp-env.yml
conda activate ds-bootcamp

# Alternative manual setup for intro-to-data-science
cd intro-to-data-science
pip install -r requirements.txt

# Automated setup (intro-to-data-science only)
chmod +x setup.sh
./setup.sh
```

### Testing and Verification
```bash
# Quick functionality test
python installation-kit/scripts/quick_test.py

# Comprehensive verification
python installation-kit/scripts/verify_setup.py

# Test notebook environment
jupyter notebook installation-kit/scripts/test_notebook.ipynb
```

### Starting Course Materials
```bash
# Main data science course
jupyter notebook intro-to-data-science/intro-to-data-science.ipynb

# Python fundamentals (instructor-led)
jupyter lab python-fundamentals/lessons/week1/lesson01_intro.ipynb

# Practice exercises
jupyter notebook intro-to-data-science/data-science-exercises.ipynb
```

### Dataset Management
```bash
# Regenerate synthetic datasets (intro-to-data-science)
cd intro-to-data-science
python generate_datasets.py
```

### Development Tools
```bash
# Code formatting (where available)
black --line-length 88 .
isort .
flake8 .

# Testing (where available)
pytest
pytest --cov
```

## High-Level Architecture

### Educational Philosophy
- **Progressive Learning**: Each module builds on the previous
- **Hands-on Practice**: All concepts immediately applied
- **Real-world Applications**: Industry-relevant projects and datasets
- **Interactive Engagement**: Gamification, widgets, and immediate feedback
- **Beginner-Friendly**: Designed for absolute programming beginners

### Course Flow Integration
```
Installation Kit → Python Fundamentals → Intro to Data Science → Full Bootcamp Curriculum
     (Setup)      →    (Programming)    →     (Analysis)     →    (Professional Skills)
```

### Key Technologies Stack
- **Python 3.8+** with comprehensive data science libraries
- **Jupyter Ecosystem**: Notebooks, Lab, and interactive widgets
- **Data Science Core**: pandas, numpy, matplotlib, seaborn, plotly, scikit-learn
- **Development Tools**: black, flake8, isort, pytest
- **Optional Advanced**: tensorflow, transformers, deep learning libraries

### Learning Outcomes Alignment
1. **Technical Skills**: Python programming, data analysis, machine learning
2. **Professional Tools**: Git, Jupyter, cloud platforms, production deployment
3. **Soft Skills**: Communication, presentation, project management
4. **Industry Readiness**: Portfolio development, interview preparation, career guidance

## Working with This Repository

### For Course Development
- Each module has its own CLAUDE.md with specific guidance
- Follow established patterns for interactive components and styling
- Maintain beginner-friendly documentation and error handling
- Test all code on multiple platforms (Windows, Mac, Linux)

### For Student Support
- Direct students to appropriate module based on their current level
- Use installation-kit verification scripts to diagnose environment issues
- Reference troubleshooting guides before escalating technical issues
- Maintain consistent styling and terminology across modules

### For Content Updates
- Update requirements.txt files when adding new dependencies
- Regenerate datasets when modifying generate_datasets.py
- Test installation scripts on clean environments
- Keep documentation synchronized with code changes

### Key Patterns to Follow

#### Environment Management
- Always use conda environments for reproducible setups
- Provide both automated and manual installation options
- Include comprehensive verification and testing scripts
- Support multiple Python versions (3.8-3.11)

#### Educational Content
- Start with real-world analogies before showing code
- Include interactive widgets for engagement
- Provide immediate feedback and progress tracking
- Structure content with clear learning objectives

#### Code Quality
- Follow PEP 8 style guidelines
- Use descriptive variable names and comments
- Include error handling and user-friendly messages
- Maintain consistent styling across modules

#### Assessment and Projects
- Design projects that build real portfolio pieces
- Include rubrics and clear evaluation criteria
- Provide templates and starter code for complex projects
- Connect learning to industry applications

## Module-Specific Notes

### Installation Kit
- Designed for absolute beginners with no technical experience
- Comprehensive troubleshooting for common setup issues
- Cross-platform compatibility with specific OS instructions
- Verification scripts test all critical functionality

### Python Fundamentals  
- Live coding approach with instructor and student typing together
- Heavy use of real-world analogies (chef/recipe, LEGO blocks, etc.)
- Progressive project complexity from simple tracking to complete applications
- Assessment focuses on application rather than memorization

### Intro to Data Science
- Interactive notebook with gamification elements
- 10 synthetic datasets covering diverse industry applications
- Professional-grade visualization templates and utilities
- Complete workflow from data exploration to presentation

### Bootcamp Curriculum
- 6-month structured program with weekly schedules
- Virtual delivery format with specific timing and engagement strategies
- Industry partnerships and guest speaker integration
- Career preparation and job placement support

This repository represents a complete educational ecosystem designed to transform beginners into job-ready data scientists through progressive, hands-on learning experiences.