#!/bin/bash

# Data Science Bootcamp - Setup Script
# This script installs all required dependencies and configures Jupyter

echo "=========================================="
echo "Data Science Bootcamp - Environment Setup"
echo "=========================================="

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8+ first."
    exit 1
fi

echo "✅ Python version: $(python3 --version)"

# Upgrade pip
echo "📦 Upgrading pip..."
python3 -m pip install --upgrade pip --user

# Install requirements
echo "📦 Installing requirements..."
python3 -m pip install -r requirements.txt --user

# Register Python kernel for Jupyter
echo "🔧 Registering Jupyter kernel..."
python3 -m ipykernel install --user --name python3 --display-name "Python 3 (Data Science)"

# Enable widget extensions
echo "🔧 Enabling Jupyter widget extensions..."
# Add common Python user bin paths
export PATH="$PATH:$HOME/.local/bin:$HOME/Library/Python/3.*/bin"

# Test imports
echo "🧪 Testing imports..."
python3 -c "
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import ipywidgets as widgets
print('✅ All core imports successful!')
print(f'  Pandas: {pd.__version__}')
print(f'  NumPy: {np.__version__}')
print(f'  Seaborn: {sns.__version__}')
print(f'  IPyWidgets: {widgets.__version__}')
"

if [ $? -eq 0 ]; then
    echo ""
    echo "=========================================="
    echo "🎉 Setup Complete!"
    echo "=========================================="
    echo ""
    echo "To start the main notebook:"
    echo "  jupyter notebook intro-to-data-science.ipynb"
    echo ""
    echo "To start the exercises notebook:"
    echo "  jupyter notebook data-science-exercises.ipynb"
    echo ""
    echo "Or with JupyterLab:"
    echo "  jupyter lab intro-to-data-science.ipynb"
    echo ""
    echo "If you encounter widget issues:"
    echo "  1. Restart the kernel (Kernel > Restart)"
    echo "  2. Clear outputs (Cell > All Output > Clear)"
    echo "  3. Re-run all cells"
else
    echo ""
    echo "❌ Setup encountered errors. Please check the output above."
    exit 1
fi