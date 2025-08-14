# 🤝 Contributing to Metrica Academy Data Science Bootcamp Curriculum

We're thrilled that you want to contribute to improving our Data Science Bootcamp curriculum! This document provides guidelines and procedures for contributing to ensure a smooth and collaborative process.

## 📋 Table of Contents

- [Types of Contributions](#types-of-contributions)
- [Getting Started](#getting-started)
- [Development Workflow](#development-workflow)
- [Content Guidelines](#content-guidelines)
- [Review Process](#review-process)
- [Community Guidelines](#community-guidelines)

---

## 🎯 Types of Contributions

We welcome various types of contributions from our community:

### 📚 Content Contributions
- **New notebooks** or course modules
- **Exercise improvements** and additional practice problems  
- **Dataset updates** or new synthetic datasets
- **Documentation enhancements**
- **Slide deck updates** and presentation materials

### 🐛 Bug Fixes & Issues
- **Typos and grammatical errors**
- **Code errors** in notebooks or scripts
- **Broken links** or outdated references
- **Environment setup issues**
- **Package compatibility problems**

### 💡 Feature Enhancements
- **Interactive widgets** and tools
- **Assessment improvements** (quizzes, assignments)
- **Visualization enhancements**
- **Automation scripts** for common tasks
- **New learning resources**

### 🎨 Design & UX
- **Notebook formatting** and readability
- **Visual design** of slides and materials
- **User experience** improvements
- **Accessibility enhancements**

---

## 🚀 Getting Started

### Prerequisites

Before contributing, ensure you have:
- **Git** installed and configured
- **Python 3.8+** with required packages
- **Jupyter Lab/Notebook** for testing content
- **GitHub account** with SSH keys configured

### Initial Setup

1. **Fork the Repository**
   ```bash
   # Go to https://github.com/Metrica-Academy/ds-bootcamp-curriculum
   # Click the "Fork" button
   ```

2. **Clone Your Fork**
   ```bash
   git clone git@github.com:YOUR_USERNAME/ds-bootcamp-curriculum.git
   cd ds-bootcamp-curriculum
   ```

3. **Add Upstream Remote**
   ```bash
   git remote add upstream git@github.com:Metrica-Academy/ds-bootcamp-curriculum.git
   ```

4. **Create Development Environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   pip install -r requirements.txt
   pip install -r requirements-dev.txt  # Development dependencies
   ```

5. **Verify Setup**
   ```bash
   python verify_setup.py
   jupyter lab  # Test that everything works
   ```

---

## 🔄 Development Workflow

### Branch Strategy

We use a **feature branch** workflow:

```
main (protected)
├── feature/update-week-3-exercises
├── bugfix/pandas-version-compatibility  
├── content/add-nlp-module
└── docs/improve-setup-instructions
```

### Step-by-Step Process

#### 1. Sync with Upstream
```bash
git checkout main
git pull upstream main
git push origin main  # Update your fork
```

#### 2. Create Feature Branch
```bash
# Use descriptive branch names
git checkout -b feature/add-time-series-module
# or
git checkout -b bugfix/fix-visualization-error
# or  
git checkout -b docs/update-installation-guide
```

#### 3. Make Your Changes
- Follow our [Content Guidelines](#content-guidelines)
- Test your changes thoroughly
- Ensure notebooks run without errors
- Update documentation as needed

#### 4. Test Your Changes
```bash
# Run all notebooks to ensure they work
python test_notebooks.py

# Check for common issues
python lint_content.py

# Verify environment compatibility
python test_requirements.py
```

#### 5. Commit Your Changes
```bash
# Stage your changes
git add .

# Write descriptive commit messages
git commit -m "Add time series analysis module with ARIMA examples

- Create new notebook with time series fundamentals
- Include 3 practice datasets (stock prices, weather, sales)
- Add interactive widgets for parameter tuning
- Update main README with new module link"
```

#### 6. Push and Create Pull Request
```bash
# Push to your fork
git push origin feature/add-time-series-module

# Go to GitHub and create Pull Request
# Use our PR template and provide detailed description
```

---

## 📝 Content Guidelines

### Notebook Standards

#### Structure
Every educational notebook should follow this structure:
```markdown
# Module Title

## Learning Objectives
- Clear, measurable objectives
- 3-5 bullet points maximum

## Prerequisites  
- Required knowledge/modules
- Estimated time to complete

## Table of Contents
1. Introduction
2. Concept Explanation  
3. Code Examples
4. Practice Exercises
5. Summary & Next Steps
```

#### Code Quality
- **Clear variable names**: `student_scores` not `ss`
- **Comprehensive comments**: Explain the "why", not just "what"
- **Error handling**: Include try/except for common issues
- **Consistent formatting**: Use black formatter
- **Cell organization**: One concept per cell maximum

#### Content Requirements
- **Real-world examples**: Avoid toy datasets when possible
- **Interactive elements**: Include widgets, quizzes, or exercises
- **Visualizations**: Every analysis should include relevant plots
- **Checkpoint questions**: Test understanding throughout
- **Summary sections**: Reinforce key concepts

### Dataset Standards

#### Synthetic Data Requirements
- **Realistic**: Mirror real-world data distributions
- **Appropriate size**: 1K-10K rows for exercises, 100K+ for projects
- **Multiple variables**: Mix of categorical, numerical, datetime
- **Built-in challenges**: Missing values, outliers, inconsistencies
- **Documentation**: Clear data dictionary and context

#### Dataset Files
```
datasets/
├── README.md                    # Overview of all datasets
├── customer_data.csv           # Main dataset file
├── customer_data_metadata.json # Schema and descriptions
└── customer_data_generator.py  # Script to recreate data
```

### Documentation Standards

#### README Files
Every module should have a README.md with:
- **Module overview** and learning objectives
- **Prerequisites** and estimated time
- **File descriptions** and navigation
- **Setup instructions** specific to the module
- **Learning resources** and external links

#### Code Documentation  
- **Docstrings** for all functions using Google style
- **Type hints** for function parameters and returns
- **Inline comments** for complex logic
- **Markdown cells** explaining concepts before code

---

## 🔍 Review Process

### Pull Request Requirements

Before submitting, ensure your PR includes:

#### ✅ Checklist
- [ ] **Descriptive title** following our naming conventions
- [ ] **Detailed description** using our PR template
- [ ] **Screenshots/GIFs** for visual changes
- [ ] **Testing proof** - notebooks run without errors
- [ ] **Documentation updates** for new features
- [ ] **Breaking change** notification if applicable

#### PR Template
```markdown
## Description
Brief description of changes and motivation.

## Type of Change
- [ ] Bug fix
- [ ] New feature  
- [ ] Documentation update
- [ ] Performance improvement
- [ ] Other (please describe)

## Testing
- [ ] All notebooks run successfully
- [ ] New content tested with fresh environment
- [ ] Links and references verified
- [ ] Interactive elements work as expected

## Screenshots/Evidence
Include screenshots or output demonstrating your changes.

## Additional Context
Any additional information reviewers should know.
```

### Review Criteria

#### Technical Review
- **Code quality**: Clean, readable, well-commented
- **Functionality**: All code executes without errors
- **Performance**: Efficient algorithms and data operations
- **Compatibility**: Works with specified package versions

#### Educational Review  
- **Clarity**: Concepts explained clearly for target audience
- **Progression**: Logical flow from simple to complex
- **Engagement**: Interactive and interesting content
- **Assessment**: Adequate practice and feedback opportunities

#### Content Review
- **Accuracy**: Technically correct information
- **Relevance**: Aligned with learning objectives
- **Currency**: Up-to-date tools and best practices
- **Completeness**: No missing steps or explanations

### Review Timeline

| Review Stage | Timeline | Reviewer |
|--------------|----------|----------|
| **Initial Check** | 24 hours | Automated tools + Maintainer |
| **Technical Review** | 48 hours | Senior Instructor |
| **Educational Review** | 72 hours | Curriculum Committee |
| **Final Approval** | 96 hours | Lead Instructor |

---

## 👥 Community Guidelines

### Code of Conduct

We are committed to providing a welcoming and inclusive environment for all contributors:

#### Our Standards
- **Be respectful** and considerate in all interactions
- **Be collaborative** and help others learn and grow
- **Be constructive** when providing feedback
- **Be patient** with new contributors
- **Be open** to different perspectives and approaches

#### Unacceptable Behavior
- Harassment or discrimination of any kind
- Trolling, insulting, or derogatory comments
- Publishing private information without permission
- Disrupting discussions or community spaces
- Any behavior that violates our values

### Communication Channels

#### For Contributors
- **GitHub Issues**: Bug reports, feature requests
- **GitHub Discussions**: General questions, ideas
- **Slack #curriculum**: Real-time collaboration
- **Email**: curriculum@metrica-academy.com

#### For Questions & Support
- **Setup Issues**: Use GitHub Issues with `setup` label
- **Content Questions**: GitHub Discussions or Slack
- **Process Questions**: Contact maintainers directly
- **Urgent Issues**: Email with `[URGENT]` in subject

### Recognition

We believe in recognizing our contributors:

#### Contributor Levels
- **First-time Contributors**: Welcome badge on first merged PR
- **Regular Contributors**: Listed in monthly newsletter
- **Major Contributors**: Featured on website and course materials
- **Maintainers**: Direct collaboration privileges

#### Recognition Methods
- **Contributors file** maintained in repository
- **Release notes** highlighting contributions
- **Social media** shout-outs for major contributions
- **Conference opportunities** to present your work

---

## 🎯 Contribution Examples

### Small Contributions (1-2 hours)
- Fix typos in notebooks or documentation
- Update broken links or outdated references
- Improve code comments or add docstrings
- Add missing package imports

### Medium Contributions (1-2 days)
- Create new exercise problems with solutions
- Add interactive widgets to existing notebooks
- Update datasets with more realistic data
- Improve visualization examples

### Large Contributions (1+ weeks)  
- Design entirely new course modules
- Create comprehensive project assignments
- Develop automated testing infrastructure
- Build interactive learning tools

---

## 📞 Getting Help

### Contributor Support
- **Stuck on something?** Ask in GitHub Discussions
- **Need a review?** Tag `@maintainers` in your PR
- **Want to chat?** Join our Slack `#curriculum` channel
- **Have ideas?** Open a GitHub Issue with your proposal

### Maintainer Contact
- **@john-doe** - Lead Curriculum Developer
- **@jane-smith** - Technical Review Coordinator  
- **@alex-johnson** - Community Manager

---

## 🙏 Thank You!

Your contributions make our bootcamp better for every student. Whether you're fixing a small typo or adding an entire module, every contribution matters and is deeply appreciated.

### Recent Contributors
<!-- This section is automatically updated -->
Thanks to these amazing contributors who have helped improve our curriculum:
- @contributor1 - Added machine learning project templates
- @contributor2 - Fixed pandas compatibility issues
- @contributor3 - Created interactive visualization examples

---

<div align="center">
  <strong>Ready to contribute? 🚀</strong>
  <br>
  <p>Start by exploring our <a href="https://github.com/Metrica-Academy/ds-bootcamp-curriculum/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22">good first issues</a>!</p>
</div>