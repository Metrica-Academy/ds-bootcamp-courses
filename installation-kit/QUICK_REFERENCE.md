# 📋 Quick Reference - Installation Commands

**For students and instructors who need quick access to key commands.**

---

## 🚀 Essential Commands

### After Installation - Every Time You Start:
```bash
# 1. Activate environment
conda activate ds-bootcamp

# 2. Navigate to bootcamp folder
cd /path/to/your/bootcamp/materials

# 3. Start Jupyter
jupyter notebook
```

### Verification Commands:
```bash
# Quick 30-second test
python scripts/quick_test.py

# Comprehensive verification
python scripts/verify_setup.py

# Check environment is active
conda info --envs
# Should show (ds-bootcamp) in your prompt
```

---

## 🔧 Troubleshooting Quick Fixes

### Environment Issues:
```bash
# Recreate environment
conda env remove -n ds-bootcamp
conda env create -f environments/ds-bootcamp-env.yml

# Update all packages
conda activate ds-bootcamp
conda update --all
```

### Widget Issues:
```bash
conda activate ds-bootcamp
jupyter nbextension enable --py widgetsnbextension --sys-prefix
```

### Jupyter Issues:
```bash
# Try different port
jupyter notebook --port=8889

# Reset configuration
rm -rf ~/.jupyter
jupyter notebook --generate-config
```

---

## 📱 Student Checklist

**Before class:**
- [ ] Follow OS-specific installation guide
- [ ] Run verification scripts successfully
- [ ] Test opening a Jupyter notebook
- [ ] Download bootcamp materials to known location

**First day of class:**
- [ ] Activate environment: `conda activate ds-bootcamp`
- [ ] Navigate to bootcamp folder
- [ ] Start Jupyter: `jupyter notebook`
- [ ] Open: `intro-to-data-science.ipynb`

---

## 👨‍🏫 Instructor Quick Setup

### Before Class:
```bash
# Test environment creation on your system
conda env create -f installation-kit/environments/ds-bootcamp-env.yml
conda activate ds-bootcamp
python installation-kit/scripts/verify_setup.py
```

### During Class:
```bash
# Have students run this
python installation-kit/scripts/quick_test.py

# For detailed troubleshooting
python installation-kit/scripts/verify_setup.py
```

### Common Student Commands:
```bash
# Windows
conda activate ds-bootcamp
jupyter notebook

# Mac/Linux  
conda activate ds-bootcamp
jupyter notebook
```

---

## 🔗 File Locations

- **Main Guide:** `installation-kit/README.md`
- **OS Guides:** `installation-kit/guides/INSTALL_[OS].md`
- **Environment:** `installation-kit/environments/ds-bootcamp-env.yml`
- **Verification:** `installation-kit/scripts/verify_setup.py`
- **Quick Test:** `installation-kit/scripts/quick_test.py`
- **Test Notebook:** `installation-kit/scripts/test_notebook.ipynb`
- **Troubleshooting:** `installation-kit/TROUBLESHOOTING.md`