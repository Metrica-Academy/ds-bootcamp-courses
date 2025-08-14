# 🔧 Data Science Bootcamp - Troubleshooting Guide

**Don't panic!** Installation issues are completely normal, especially for beginners. This guide contains solutions for the most common problems you might encounter.

---

## 🚨 Emergency Quick Fixes

### If Nothing Seems to Work:
1. **Restart your computer** - Seriously, this fixes many issues!
2. **Run as Administrator** (Windows) or use `sudo` (Mac/Linux)
3. **Disable antivirus temporarily** during installation
4. **Check your internet connection** - many steps require downloading
5. **Free up disk space** - you need at least 5GB available

---

## 🖥️ Windows-Specific Issues

### Issue 1: "conda is not recognized as an internal or external command"

**Cause:** Miniconda wasn't added to your system PATH during installation.

**Solution A - Reinstall with PATH:**
1. Uninstall Miniconda (Control Panel → Programs → Uninstall)
2. Download Miniconda installer again
3. **IMPORTANT:** During installation, check "Add Miniconda3 to my PATH environment variable"
4. Complete installation and restart computer

**Solution B - Manually Add to PATH:**
1. Press **Windows Key + R**
2. Type `sysdm.cpl` and press Enter
3. Click **"Environment Variables"**
4. Under "User variables", find **"Path"** and click **"Edit"**
5. Click **"New"** and add: `C:\Users\YourUsername\miniconda3\Scripts`
6. Click **"New"** again and add: `C:\Users\YourUsername\miniconda3`
7. Click **OK** on all windows
8. **Restart Command Prompt** (close and reopen)

### Issue 2: "Access is denied" or Permission Errors

**Solution:**
1. Right-click **Command Prompt** and select **"Run as administrator"**
2. Try the command again
3. If still failing, check if antivirus is blocking the installation

### Issue 3: Installation Fails with "Could not create conda environment"

**Solution:**
```bash
# Clean conda caches
conda clean --all

# Try creating environment with more verbose output
conda env create -f ds-bootcamp-env.yml --verbose

# If still failing, create minimal environment first
conda create -n ds-bootcamp python=3.9
conda activate ds-bootcamp
conda install pandas numpy matplotlib seaborn plotly scikit-learn jupyter ipywidgets
```

### Issue 4: Jupyter Opens But Widgets Don't Work

**Solution:**
```bash
conda activate ds-bootcamp
pip install ipywidgets
jupyter nbextension enable --py widgetsnbextension --sys-prefix
jupyter lab build  # If using JupyterLab
```

**If still not working:**
```bash
jupyter nbextension list  # Check what's installed
jupyter notebook --debug  # Run with debug info
```

---

## 🍎 macOS-Specific Issues

### Issue 1: "conda: command not found"

**Cause:** Shell configuration issue, common on newer Macs.

**Solution for zsh (default on macOS Catalina+):**
```bash
echo 'export PATH="$HOME/miniconda3/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

**Solution for bash (older Macs):**
```bash
echo 'export PATH="$HOME/miniconda3/bin:$PATH"' >> ~/.bash_profile
source ~/.bash_profile
```

**If unsure which shell:**
```bash
echo $SHELL
# If it shows /bin/zsh, use zsh commands
# If it shows /bin/bash, use bash commands
```

### Issue 2: "xcrun: error: invalid active developer path"

**Cause:** Missing Xcode command line tools.

**Solution:**
```bash
xcode-select --install
```
Click "Install" when prompted, wait for download to complete, then try conda installation again.

### Issue 3: Apple Silicon (M1/M2/M3) Architecture Issues

**Solution A - Force x86 compatibility:**
```bash
conda config --env --set subdir osx-64
conda env create -f ds-bootcamp-env.yml
```

**Solution B - Use native ARM packages:**
```bash
conda config --env --set subdir osx-arm64
conda env create -f ds-bootcamp-env.yml
```

### Issue 4: "Permission denied" when installing packages

**Solution:**
```bash
# Don't use sudo with conda! Instead:
conda config --set always_yes true
conda env create -f ds-bootcamp-env.yml

# Or create environment in user directory:
conda env create -f ds-bootcamp-env.yml -p ~/miniconda3/envs/ds-bootcamp
```

---

## 🐧 Linux-Specific Issues

### Issue 1: "wget: command not found" or "curl: command not found"

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install wget curl
```

**Fedora:**
```bash
sudo dnf install wget curl
```

**CentOS/RHEL:**
```bash
sudo yum install wget curl
```

### Issue 2: "Permission denied" during installation

**Solution:**
```bash
# Make installer executable
chmod +x Miniconda3-latest-Linux-*.sh

# Run installer
bash Miniconda3-latest-Linux-*.sh
```

### Issue 3: SSL Certificate Issues

**Solution:**
```bash
# Update certificates
sudo apt update && sudo apt install ca-certificates  # Ubuntu/Debian
sudo dnf update ca-certificates  # Fedora
sudo yum update ca-certificates  # CentOS

# Alternative download method
wget --no-check-certificate https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

### Issue 4: Display Issues with Jupyter (Headless Systems)

**Solution - SSH with X11 forwarding:**
```bash
ssh -X username@your-server
# Then run jupyter normally
```

**Solution - Remote access:**
```bash
jupyter notebook --no-browser --port=8888 --ip=0.0.0.0
# Access via http://your-server-ip:8888
```

---

## 🌐 Network and Download Issues

### Issue 1: Slow Downloads or Timeouts

**Solution:**
```bash
# Increase timeout
conda config --set remote_read_timeout_secs 120

# Use different mirrors
conda config --add channels conda-forge
conda config --set channel_priority strict
```

### Issue 2: Corporate Firewall/Proxy Issues

**Solution:**
```bash
# Configure conda for proxy
conda config --set proxy_servers.http http://proxy.company.com:8080
conda config --set proxy_servers.https https://proxy.company.com:8080

# Alternative: Use pip for packages
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org pandas numpy matplotlib
```

### Issue 3: "Package not found" Errors

**Solution:**
```bash
# Update conda
conda update conda

# Add additional channels
conda config --add channels conda-forge
conda config --add channels anaconda

# Try installing packages individually
conda install pandas=1.5.3
conda install numpy=1.26.4
# etc...
```

---

## 🎮 Jupyter and Widget Issues

### Issue 1: Widgets Not Displaying

**Symptoms:** You see `Widget(...)` text instead of interactive elements.

**Solution 1 - Enable extensions:**
```bash
conda activate ds-bootcamp
jupyter nbextension enable --py widgetsnbextension --sys-prefix
```

**Solution 2 - Reinstall widgets:**
```bash
conda uninstall ipywidgets
conda install -c conda-forge ipywidgets
jupyter nbextension enable --py widgetsnbextension --sys-prefix
```

**Solution 3 - Clear browser cache:**
- Close Jupyter
- Clear your browser cache and cookies
- Restart Jupyter

### Issue 2: Jupyter Won't Start

**Solution 1 - Check port availability:**
```bash
jupyter notebook --port=8889  # Try different port
```

**Solution 2 - Reset Jupyter config:**
```bash
jupyter --config-dir  # See where config is stored
rm -rf ~/.jupyter  # Delete config (will recreate defaults)
jupyter notebook --generate-config
```

**Solution 3 - Check for running instances:**
```bash
jupyter notebook stop 8888  # Stop any running notebooks
```

### Issue 3: Kernel Keeps Dying

**Solution:**
```bash
# Check if environment is properly activated
conda activate ds-bootcamp
python -c "import sys; print(sys.executable)"

# Reinstall ipykernel
pip install ipykernel
python -m ipykernel install --user --name ds-bootcamp
```

---

## 🔄 Environment and Package Issues

### Issue 1: "Environment Already Exists"

**Solution:**
```bash
# Remove existing environment
conda env remove -n ds-bootcamp

# Create fresh environment
conda env create -f ds-bootcamp-env.yml
```

### Issue 2: Package Version Conflicts

**Solution:**
```bash
# Create minimal environment first
conda create -n ds-bootcamp python=3.9
conda activate ds-bootcamp

# Install packages one by one
conda install pandas
conda install numpy
# etc...

# Or use pip for problematic packages
pip install pandas==1.5.3
```

### Issue 3: "Solving environment" Takes Forever

**Solution:**
```bash
# Use mamba (faster conda alternative)
conda install mamba -n base -c conda-forge
mamba env create -f ds-bootcamp-env.yml

# Or use libmamba solver
conda install -n base conda-libmamba-solver
conda config --set solver libmamba
```

---

## 💾 Disk Space and Performance Issues

### Issue 1: "No space left on device"

**Solution:**
```bash
# Clean conda caches
conda clean --all

# Remove unused environments
conda env list  # See all environments
conda env remove -n unused_environment_name

# Check disk space
df -h  # Linux/Mac
dir c:  # Windows
```

### Issue 2: Installation is Very Slow

**Solution:**
```bash
# Use faster channels
conda config --add channels conda-forge
conda config --set channel_priority flexible

# Install with mamba (faster)
conda install mamba -c conda-forge
mamba env create -f ds-bootcamp-env.yml
```

---

## 🆘 When All Else Fails

### Option 1: Fresh Start
1. **Completely uninstall** Miniconda
2. **Restart** your computer
3. **Download fresh installer** from official site
4. **Follow installation guide** from beginning

### Option 2: Alternative Installation Methods

**Google Colab (Web-based, no installation needed):**
- Go to https://colab.research.google.com
- Upload the bootcamp notebook
- Most packages pre-installed

**Anaconda Full Distribution:**
- Download full Anaconda instead of Miniconda
- Includes all packages pre-installed
- Larger download but fewer compatibility issues

### Option 3: Docker (Advanced Users)
```bash
# Pull data science Docker image
docker pull jupyter/datascience-notebook

# Run container
docker run -p 8888:8888 jupyter/datascience-notebook
```

---

## 📞 Getting Additional Help

### Before Asking for Help

**Gather this information:**
1. **Operating System:** Windows 10, macOS Big Sur, Ubuntu 20.04, etc.
2. **Error Message:** Copy and paste the complete error (not just the last line)
3. **What you were doing:** Which step in the installation guide
4. **Commands you tried:** Copy and paste the commands you ran
5. **Output of diagnostics:**
   ```bash
   conda --version
   python --version
   which python  # Mac/Linux
   where python   # Windows
   conda info
   conda env list
   ```

### Where to Ask for Help

1. **Class Forum/Chat:** Other students might have faced the same issue
2. **Instructor:** Email with all the information above
3. **Office Hours:** Schedule a screen-sharing session
4. **Study Groups:** Work together with classmates

### How to Get Help Faster

1. **Be specific:** "It doesn't work" is hard to help with
2. **Include screenshots:** A picture is worth a thousand words
3. **Show what you tried:** List the solutions you already attempted
4. **Be patient:** Complex issues might take time to resolve

---

## 🎯 Prevention Tips

### For Next Time:
1. **Save these instructions:** Bookmark this troubleshooting guide
2. **Document what worked:** Keep notes for future reference
3. **Regular backups:** Export your environment: `conda env export > my_environment.yml`
4. **Keep systems updated:** Regularly update your OS and conda
5. **Test early:** Don't wait until the last minute to install

### Environment Best Practices:
```bash
# Always activate environment before working
conda activate ds-bootcamp

# Keep environment updated
conda update --all

# Create backup of working environment
conda env export > working_environment_backup.yml
```

---

## ✅ Success Checklist

When everything is working, you should be able to:
- [ ] Run `conda --version` and see a version number
- [ ] Run `conda activate ds-bootcamp` without errors
- [ ] Run `python -c "import pandas as pd; print('Success!')`
- [ ] Start Jupyter with `jupyter notebook`
- [ ] Create a new notebook and run Python code
- [ ] See interactive widgets in notebooks
- [ ] Import all required packages without errors

**If you can check all these boxes, you're ready for the bootcamp!** 🎉

---

**Remember:** Every expert was once a beginner. Installation issues are frustrating, but they don't reflect on your ability to learn data science. Keep trying, ask for help when needed, and celebrate when you get it working! 💪

*You've got this!* 🚀