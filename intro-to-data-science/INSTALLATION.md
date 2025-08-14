# Detailed Installation Guide

This guide provides troubleshooting and manual installation instructions. For quick setup, see the main [README.md](README.md).

## Manual Installation

If the automated setup script (`./setup.sh`) doesn't work for your environment:

### 1. Install Dependencies

```bash
pip install -r requirements.txt --user
```

### 2. Register Jupyter Kernel

```bash
python3 -m ipykernel install --user --name python3 --display-name "Python 3"
```

### 3. Start Jupyter

```bash
jupyter notebook intro-to-data-science.ipynb
```

## Important Version Requirements

To avoid compatibility issues, these minimum versions are recommended:

- **pandas**: 1.5.0+ (for DataFrame operations)
- **numpy**: 1.24.0+ (for array operations)
- **ipywidgets**: 8.0.0+ (required for interactive components)
- **matplotlib**: 3.5.0+ (for plotting)
- **seaborn**: 0.11.0+ (for statistical visualizations)
- **plotly**: 5.10.0+ (for interactive plots)

## Troubleshooting

### Widget Display Errors

If you see "Error displaying widget: model not found":

1. **Restart Jupyter kernel**: Kernel → Restart & Clear Output
2. **Re-run all cells**: Cell → Run All
3. **Hard refresh browser**: Cmd+Shift+R (Mac) or Ctrl+Shift+R (Windows/Linux)

### Import Errors

If seaborn or other packages fail to import:

1. Check you're using the correct kernel: Kernel → Change kernel → Python 3
2. Reinstall the specific package:
   ```bash
   pip uninstall seaborn -y
   pip install seaborn --user
   ```

### NumPy Version Compatibility Issues

If you get "numpy.dtype size changed" or other version compatibility errors:

```bash
pip uninstall numpy pandas matplotlib seaborn -y
pip install -r requirements.txt --user
```

## Verifying Installation

Test your installation:

```python
import pandas as pd
import numpy as np
import seaborn as sns
import ipywidgets as widgets

print(f"Pandas: {pd.__version__}")
print(f"NumPy: {np.__version__}")
print(f"Seaborn: {sns.__version__}")
print(f"Widgets: {widgets.__version__}")
```

All imports should work without errors.