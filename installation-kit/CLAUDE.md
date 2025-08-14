# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a **Data Science Bootcamp Installation Kit** designed to help absolute beginners set up a complete data science environment. The repository contains comprehensive installation guides, troubleshooting documentation, verification scripts, and test materials for setting up a Python data science stack using conda/miniconda.

## Common Commands

### Environment Setup and Testing
```bash
# Create the data science environment
conda env create -f environments/ds-bootcamp-env.yml

# Activate the environment
conda activate ds-bootcamp

# Quick functionality test (30 seconds)
python scripts/quick_test.py

# Comprehensive installation verification (2 minutes)
python scripts/verify_setup.py

# Start Jupyter for interactive testing
jupyter notebook
# Then open: scripts/test_notebook.ipynb
```

### Environment Management
```bash
# List all conda environments
conda info --envs

# Remove and recreate environment if needed
conda env remove -n ds-bootcamp
conda env create -f environments/ds-bootcamp-env.yml

# Update all packages in environment
conda activate ds-bootcamp
conda update --all

# Export current environment for backup
conda env export > backup-environment.yml
```

### Widget and Jupyter Configuration
```bash
# Enable Jupyter widgets (if not working)
conda activate ds-bootcamp
jupyter nbextension enable --py widgetsnbextension --sys-prefix

# Reset Jupyter configuration
rm -rf ~/.jupyter
jupyter notebook --generate-config

# Start Jupyter on different port if needed
jupyter notebook --port=8889
```

## Repository Structure

### Core Files and Directories

- **`environments/ds-bootcamp-env.yml`**: Conda environment specification with all required data science packages (pandas, numpy, matplotlib, seaborn, plotly, scikit-learn, jupyter, ipywidgets)

- **`scripts/`**: Verification and testing utilities
  - `verify_setup.py`: Comprehensive installation verification script with colored output
  - `quick_test.py`: Minimal 30-second functionality test
  - `test_notebook.ipynb`: Interactive Jupyter notebook for testing all functionality

- **`guides/`**: Platform-specific installation guides
  - `INSTALL_MAC.md`: macOS installation (Intel and Apple Silicon)
  - `INSTALL_WINDOWS.md`: Windows installation guide
  - `INSTALL_LINUX.md`: Linux installation guide

- **`README.md`**: Main entry point with overview and quick start instructions

- **`TROUBLESHOOTING.md`**: Comprehensive troubleshooting guide covering common installation issues

- **`QUICK_REFERENCE.md`**: Essential commands for students and instructors

## Key Architecture Components

### Target Python Environment
- **Python 3.9** as the base
- **Primary data science stack**: pandas (1.5.3), numpy (1.26.4), matplotlib (>=3.5.0), seaborn (>=0.11.0)
- **Machine learning**: scikit-learn (>=1.1.0), scipy (>=1.8.0)
- **Interactive visualization**: plotly (>=5.10.0)
- **Jupyter ecosystem**: jupyter, notebook (>=7.0.0), jupyterlab (>=4.0.0), ipykernel
- **Interactive widgets**: ipywidgets (>=8.0.0), widgetsnbextension (>=4.0.0)

### Verification System
The repository includes a multi-layer testing approach:
1. **Quick test**: Basic import and functionality check
2. **Comprehensive verification**: Detailed package testing with version checking, widget testing, and data science capability validation
3. **Interactive notebook**: Full workflow testing in Jupyter environment

### Installation Flow
1. Install Miniconda/conda
2. Create environment from YAML file
3. Activate environment
4. Run verification scripts
5. Test interactive functionality
6. Enable Jupyter extensions

## Working with This Repository

### When Helping with Installation Issues
- Always check which operating system the user is on first
- Direct users to appropriate OS-specific guide in `guides/` directory
- Use the verification scripts to diagnose issues
- Reference `TROUBLESHOOTING.md` for common solutions
- Environment recreation is often the most effective solution for complex issues

### When Modifying Environment
- Edit `environments/ds-bootcamp-env.yml` for package changes
- Test changes across multiple platforms if possible
- Update version information in `README.md` (currently shows version 1.0, Python 3.9, tested on Windows 10/11, macOS 12+, Ubuntu 20.04+)
- Update verification scripts if adding new packages

### When Updating Documentation
- Keep beginner-friendly tone throughout
- Include exact commands with proper formatting
- Provide clear step-by-step instructions
- Update troubleshooting guide with any new common issues discovered

## Target Audience Considerations

This installation kit is specifically designed for:
- Complete programming beginners
- Students entering a data science bootcamp
- Non-technical users who need a working data science environment
- Instructors teaching data science basics

The documentation uses extensive emoji, friendly language, clear sections, and assumes no prior technical knowledge. All instructions are written to be accessible to users who may never have used a command line before.