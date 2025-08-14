# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an educational **Data Science Bootcamp** repository containing interactive course materials for teaching data science fundamentals with Python. The project is designed as a comprehensive Jupyter notebook-based learning experience with supporting utility files and synthetic datasets for hands-on practice.

## Core Architecture

### Main Components

1. **`intro-to-data-science.ipynb`** - Primary interactive notebook (~29k tokens) containing the complete bootcamp curriculum with modules covering:
   - Welcome and interactive magic show demo
   - Data science fundamentals and career exploration
   - Python programming for data analysis
   - Data manipulation with Pandas and NumPy
   - Data visualization techniques (Matplotlib, Seaborn, Plotly)
   - Statistical analysis and pattern recognition
   - Real-world challenge projects:
     - COVID-19 Healthcare Detective Analysis
     - Fraud Detection Investigation
     - Mystery Shopper Customer Analytics
   - Interactive completion certificate generation

2. **`data-science-exercises.ipynb`** - Additional exercises notebook for independent practice

3. **`data_science_utils.py`** - Core utility library with educational classes:
   - `DataScienceKit`: Student progress tracking system
   - Various utility functions for data analysis and visualization
   - Educational components and progress tracking

4. **`interactive_components.py`** - Advanced interactive widgets for Jupyter:
   - `InteractiveQuiz`: Multiple choice quiz system with immediate feedback
   - Interactive data exploration components
   - Educational engagement tools

5. **`generate_datasets.py`** - Synthetic dataset generator creating 10 educational datasets:
   - Healthcare (COVID-19 patient data) - 2,000 rows
   - Financial (fraud detection transactions) - 10,000 rows
   - Retail (mystery shopper analytics) - 100 rows
   - Entertainment (Netflix viewing, Spotify music, movie ratings) - 5,000, 1,000, 5,000 rows
   - E-commerce (retail transactions) - 10,000 rows
   - Weather patterns - 3,650 rows
   - Social media data - 2,000 rows
   - Housing data - 545 rows

### Dataset Structure

- **`datasets/`** - Contains 10 CSV files (~39k total rows) with accompanying `metadata.json`
- **`figs/`** - 50+ educational images, logos, and visualizations for enhanced learning

### Supporting Files

- **`requirements.txt`** - Complete dependency specification for easy environment setup
- **`README.md`** - Project overview and setup instructions
- **`setup.sh`** - Automated environment setup script
- **`INSTALLATION.md`** - Detailed installation instructions

## Dependencies

The project uses standard data science Python libraries:

```python
# Core Data Science Stack
pandas, numpy, matplotlib, seaborn, plotly
sklearn, scipy

# Interactive Components
ipywidgets, IPython

# Utilities
datetime, random, json, os, warnings
```

## Educational Design

### Learning Architecture
- **Interactive-First Approach**: Every concept includes hands-on widgets and exercises
- **Gamification**: Point system, badges, and achievement tracking throughout
- **Real-World Applications**: Three comprehensive challenge projects using realistic datasets
- **Professional Workflows**: Students learn industry-standard tools and practices
- **Self-Contained**: No external APIs or services required

### Pedagogical Features
- Progress tracking with visual indicators
- Immediate feedback on quizzes and exercises
- Professional-grade visualizations with consistent styling
- Achievement system with completion certificates
- Career path exploration and tool ecosystem overview

## Common Development Tasks

### Running the Notebooks
```bash
# Main course notebook
jupyter notebook intro-to-data-science.ipynb

# Practice exercises
jupyter notebook data-science-exercises.ipynb
```

### Regenerating Datasets
```bash
python generate_datasets.py
```
This creates all 10 synthetic datasets in the `datasets/` directory with metadata.

### Automated Setup
```bash
chmod +x setup.sh
./setup.sh
```
This runs the complete environment setup including dependencies and Jupyter configuration.

### Environment Verification
```python
from data_science_utils import create_environment_checker
print(create_environment_checker())
```

## Code Patterns

### Class-Based Architecture
- Educational components organized into logical classes
- Interactive widgets follow consistent `create_*()` method patterns
- Data generators use static methods with standardized naming
- Utility functions grouped by functionality (plotting, analysis, engagement)

### Styling and UX
- Consistent color palette across all visualizations (`PlottingUtils.COLORS`)
- Professional bootcamp branding with engaging visual elements
- Responsive widget layouts optimized for Jupyter environment
- Achievement celebrations and progress indicators

### Data Generation
- All synthetic data uses `np.random.seed(42)` for reproducibility
- Realistic data distributions using appropriate statistical models
- Built-in validation and educational constraints
- Metadata documentation for all generated datasets

## Working with This Repository

When modifying educational content:
- Test all interactive components in Jupyter environment
- Maintain consistent progress tracking integration
- Follow established widget and visualization patterns
- Ensure synthetic data remains realistic and educational
- Verify all cells execute without errors
- Test completion certificate generation workflow

### Key Usage Patterns

```python
# Professional plotting with bootcamp styling
from data_science_utils import PlottingUtils
fig, ax = PlottingUtils.create_bar_chart(data, title="Analysis", xlabel="X", ylabel="Y")

# Interactive engagement tools
from data_science_utils import BootcampEngagement
BootcampEngagement.create_section_header("New Topic", "🚀", "Learning objectives...")

# Data analysis utilities
from data_science_utils import DataAnalysisUtils
outliers = DataAnalysisUtils.detect_outliers(df, 'column_name', method='iqr')
data_dict = DataAnalysisUtils.create_data_dictionary(df)

# Interactive components
from interactive_components import InteractiveQuiz, GamificationEngine
quiz = InteractiveQuiz("Topic Quiz")
game_engine = GamificationEngine("Student Name")
game_engine.award_points(50, "Completed analysis challenge!")
```

This is a self-contained educational package requiring no external services or APIs, designed to provide a comprehensive introduction to data science through hands-on, interactive learning experiences.