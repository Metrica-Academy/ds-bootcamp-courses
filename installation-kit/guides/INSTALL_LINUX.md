# 🐧 Data Science Bootcamp Installation Guide - Linux

**Welcome to your Data Science journey on Linux!** 🚀 This guide will help you set up everything you need on your Linux system. We'll cover the most popular distributions (Ubuntu, Fedora, CentOS, etc.).

## 📋 What We'll Install

By the end of this guide, you'll have:
- ✅ Miniconda (a lightweight Python package manager)
- ✅ All the data science tools you need (pandas, matplotlib, etc.)
- ✅ Jupyter notebooks (where you'll write and run your code)
- ✅ Interactive widgets (for fun, clickable elements in your notebooks)

**Time needed:** 20-30 minutes  
**Don't panic if something goes wrong** - we have solutions for common issues at the end!

---

## 🔍 Before We Start: Check Your System

### Step 1: Find Out Your Linux Distribution
```bash
cat /etc/os-release
```
This will show you information like:
- Ubuntu 20.04, 22.04, etc.
- Fedora 38, 39, etc.
- CentOS, RHEL, etc.

### Step 2: Check Your Architecture
```bash
uname -m
```
You'll see either:
- `x86_64` (64-bit Intel/AMD) - **Most common**
- `aarch64` (ARM 64-bit)

### Step 3: Check Available Space
```bash
df -h ~
```
Make sure you have at least **5GB free space** in your home directory.

### Step 4: Update Your System
**Ubuntu/Debian:**
```bash
sudo apt update && sudo apt upgrade -y
```

**Fedora:**
```bash
sudo dnf update -y
```

**CentOS/RHEL:**
```bash
sudo yum update -y
```

---

## 📥 Step-by-Step Installation

### Phase 1: Install Prerequisites

**Ubuntu/Debian:**
```bash
sudo apt install -y wget curl bzip2 ca-certificates
```

**Fedora:**
```bash
sudo dnf install -y wget curl bzip2 ca-certificates
```

**CentOS/RHEL:**
```bash
sudo yum install -y wget curl bzip2 ca-certificates
```

### Phase 2: Download Miniconda

1. **Create a downloads directory:**
```bash
mkdir -p ~/downloads
cd ~/downloads
```

2. **Download Miniconda (choose based on your architecture):**

**For x86_64 (most common):**
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

**For ARM64/aarch64:**
```bash
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-aarch64.sh
```

3. **Verify the download completed:**
```bash
ls -la Miniconda3-latest-Linux-*.sh
```
You should see a file that's about 80-100MB.

### Phase 3: Install Miniconda

4. **Make the installer executable:**
```bash
chmod +x Miniconda3-latest-Linux-*.sh
```

5. **Run the installer:**
```bash
bash Miniconda3-latest-Linux-*.sh
```

6. **Follow the interactive installation:**

   - **License Agreement:** Press `Enter` to scroll through, then type `yes`
   
   - **Installation Location:** Press `Enter` to accept default (`/home/yourusername/miniconda3`)
   
   - **Initialize conda:** Type `yes` when asked "Do you wish the installer to initialize Miniconda3?"

*💡 The installer will show lots of text - this is normal!*

7. **Reload your shell configuration:**
```bash
source ~/.bashrc
```
(or `source ~/.zshrc` if you use zsh)

### Phase 4: Test That Miniconda Works

8. **Test the installation:**
```bash
conda --version
```
You should see something like `conda 23.X.X`

**❌ If you get "conda: command not found":**
```bash
export PATH="$HOME/miniconda3/bin:$PATH"
source ~/.bashrc
```

9. **Update conda to the latest version:**
```bash
conda update conda -y
```

### Phase 5: Create Your Data Science Environment

10. **Navigate to your bootcamp materials directory:**
    - If you have the environment file, navigate to where you saved it
    - Example: `cd ~/Downloads` or wherever you put the `ds-bootcamp-env.yml` file

11. **Create the environment:**
```bash
conda env create -f ds-bootcamp-env.yml
```
**This will take 15-30 minutes** - perfect time for a coffee break! ☕

*You'll see lots of text about downloading and installing packages - this is normal!*

12. **Activate your environment:**
```bash
conda activate ds-bootcamp
```
Your prompt should now show `(ds-bootcamp)` at the beginning.

### Phase 6: Set Up Jupyter Widgets

13. **Install Jupyter extensions:**
```bash
jupyter contrib nbextension install --user
jupyter nbextensions_configurator enable --user
jupyter nbextension enable --py widgetsnbextension --sys-prefix
```

14. **Test Jupyter:**
```bash
jupyter notebook
```
- If you're using Linux with a desktop, your browser should open automatically
- If you're on a server or headless system, see "Headless/Server Installation" below

---

## 🎉 Success Check

### Verify Everything Works

1. **In Jupyter, create a new notebook:**
   - Click **New** → **Python 3 (ipykernel)**

2. **Test basic functionality:**
   - In the first cell, type: `import pandas as pd`
   - Press **Shift + Enter**
   - If no error appears, you're good!

3. **Test widgets:**
   - In a new cell, type:
   ```python
   import ipywidgets as widgets
   slider = widgets.IntSlider(value=5, min=0, max=10)
   slider
   ```
   - Press **Shift + Enter**
   - You should see a slider you can move!

**🎊 Congratulations! You're ready for the bootcamp!**

---

## 🖥️ Headless/Server Installation

If you're installing on a server without a desktop environment:

### Option 1: Remote Access with SSH Tunneling

1. **On your server, start Jupyter without browser:**
```bash
conda activate ds-bootcamp
jupyter notebook --no-browser --port=8888 --ip=0.0.0.0
```

2. **From your local machine, create SSH tunnel:**
```bash
ssh -L 8888:localhost:8888 username@your-server-ip
```

3. **Open browser on local machine** and go to: `http://localhost:8888`

### Option 2: JupyterLab (Better for Remote)

```bash
conda activate ds-bootcamp
pip install jupyterlab
jupyter lab --no-browser --port=8888 --ip=0.0.0.0 --allow-root
```

---

## 🔧 Common Issues and Solutions

### Issue 1: "conda: command not found"

**Solution A - Add to PATH manually:**
```bash
echo 'export PATH="$HOME/miniconda3/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
```

**Solution B - Reinitialize:**
```bash
~/miniconda3/bin/conda init bash
source ~/.bashrc
```

### Issue 2: Permission Denied Errors

**Solution - Fix permissions:**
```bash
chmod -R u+w ~/miniconda3/
```

### Issue 3: "Package not found" or "Channel not available"

**Solution - Add conda-forge channel:**
```bash
conda config --add channels conda-forge
conda config --set channel_priority flexible
```

### Issue 4: SSL Certificate Errors

**Solution:**
```bash
conda config --set ssl_verify false
pip config set global.trusted-host pypi.org
pip config set global.trusted-host pypi.python.org
pip config set global.trusted-host files.pythonhosted.org
```

### Issue 5: Low Disk Space During Installation

**Solution - Use different location:**
```bash
conda config --add pkgs_dirs ~/conda-pkgs
```

### Issue 6: Jupyter Won't Start

**Solution A - Check if port is in use:**
```bash
netstat -tlnp | grep :8888
jupyter notebook --port=8889
```

**Solution B - Reset Jupyter config:**
```bash
jupyter --paths
rm -rf ~/.jupyter
jupyter notebook --generate-config
```

---

## 🐧 Linux Distribution Specific Notes

### Ubuntu/Debian Specifics:
- Make sure `python3-dev` is installed: `sudo apt install python3-dev`
- For older versions, you might need: `sudo apt install python3-pip`

### Fedora Specifics:
- Install development tools: `sudo dnf groupinstall "Development Tools"`
- Python headers: `sudo dnf install python3-devel`

### CentOS/RHEL Specifics:
- Enable EPEL repository: `sudo yum install epel-release`
- Development tools: `sudo yum groupinstall "Development Tools"`

### Arch Linux:
```bash
sudo pacman -S wget curl bzip2 ca-certificates
# Then follow the standard installation steps
```

---

## 📞 Getting Help

**If you're stuck:**
1. 📧 Email your instructor with the error output
2. 💬 Ask in the class chat/forum
3. 👥 Ask a classmate to help via screen sharing

**When asking for help, please include:**
- Your Linux distribution and version (`cat /etc/os-release`)
- Your architecture (`uname -m`)
- The exact error message (copy from terminal)
- Output of `conda --version` and `python --version`

---

## 🎯 Next Steps

Once everything is working:

1. **Create a dedicated workspace:**
```bash
mkdir -p ~/DataScienceBootcamp
cd ~/DataScienceBootcamp
```

2. **Download the bootcamp materials** from your instructor and put them here

3. **Create a launch script** for convenience:
```bash
cat > ~/start_bootcamp.sh << 'EOF'
#!/bin/bash
cd ~/DataScienceBootcamp
conda activate ds-bootcamp
jupyter notebook
EOF

chmod +x ~/start_bootcamp.sh
```

4. **Launch your bootcamp environment:**
```bash
~/start_bootcamp.sh
```

5. **Open** the main bootcamp notebook: `intro-to-data-science.ipynb`

**You're all set! Welcome to your Data Science adventure!** 🚀📊

---

## ⚡ Advanced Tips

### Make conda activation automatic:
```bash
echo "conda activate ds-bootcamp" >> ~/.bashrc
```

### Create desktop shortcut (Ubuntu):
```bash
cat > ~/Desktop/DataScienceBootcamp.desktop << 'EOF'
[Desktop Entry]
Version=1.0
Type=Application
Name=Data Science Bootcamp
Comment=Launch Jupyter for Data Science Bootcamp
Exec=bash -c "cd ~/DataScienceBootcamp && conda activate ds-bootcamp && jupyter notebook"
Icon=applications-science
Terminal=true
StartupNotify=false
EOF

chmod +x ~/Desktop/DataScienceBootcamp.desktop
```

**You're now ready to dive into data science on Linux!** 💪