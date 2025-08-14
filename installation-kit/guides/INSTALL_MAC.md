# 🍎 Data Science Bootcamp Installation Guide - macOS

**Welcome to your Data Science journey on Mac!** 🚀 This guide will help you set up everything you need on your macOS computer. Whether you're on an older Intel Mac or a newer Apple Silicon Mac (M1/M2/M3), we've got you covered!

## 📋 What We'll Install

By the end of this guide, you'll have:
- ✅ Miniconda (a lightweight Python package manager)
- ✅ All the data science tools you need (pandas, matplotlib, etc.)
- ✅ Jupyter notebooks (where you'll write and run your code)
- ✅ Interactive widgets (for fun, clickable elements in your notebooks)

**Time needed:** 30-45 minutes  
**Don't panic if something goes wrong** - we have solutions for common issues at the end!

---

## 🔍 Before We Start: Check Your System

### Step 1: Find Out Your Mac Type
1. **Click** the Apple logo (🍎) in the top-left corner
2. **Select** "About This Mac"
3. **Look at "Processor" or "Chip":**
   - If it says **"Intel"** → You have an Intel Mac
   - If it says **"Apple M1"**, **"Apple M2"**, or **"Apple M3"** → You have an Apple Silicon Mac
4. **Write this down** - you'll need it!

*📸 [Screenshot placeholder: About This Mac window showing chip type]*

### Step 2: Check Your macOS Version
- In the same "About This Mac" window, note your macOS version
- You need **macOS 10.15 (Catalina) or newer**
- If older, please update your macOS first!

### Step 3: Check Available Space
- **Click** the Apple logo → "About This Mac" → "Storage"
- **Make sure** you have at least **5GB free space**

---

## 📥 Step-by-Step Installation

### Phase 1: Download Miniconda

1. **Open Safari** (or your preferred web browser)

2. **Go to:** https://docs.conda.io/projects/miniconda/en/latest/

3. **Choose the right version for your Mac:**
   
   **For Intel Macs:**
   - Click `Miniconda3 macOS Intel x86 64-bit pkg`
   
   **For Apple Silicon Macs (M1/M2/M3):**
   - Click `Miniconda3 macOS Apple M1 64-bit pkg`
   
   *💡 Not sure which you have? Go back to Step 1 above!*

4. **Wait for download** - the file will be about 80-100MB

*📸 [Screenshot placeholder: Miniconda download page with macOS options highlighted]*

### Phase 2: Install Miniconda

5. **Find your downloaded file** (usually in Downloads folder)
   - The file name will end with `.pkg`

6. **Double-click** the `.pkg` file to start installation

7. **Follow the installation wizard:**

   **Introduction:**
   - Click **Continue**

   **Read Me:**
   - Click **Continue** (you can read it if you want!)

   **License:**
   - Click **Continue**, then **Agree**

   **Destination Select:**
   - **Keep the default** (your main hard drive)
   - Click **Continue**

   **Installation Type:**
   - Click **Install**
   - **Enter your Mac password** when prompted

*📸 [Screenshot placeholder: Installation wizard showing destination selection]*

8. **Wait patiently** - installation takes 5-10 minutes

9. **When finished:**
   - Click **Close**
   - You can **Move to Trash** the installer file if asked

### Phase 3: Set Up Your Terminal

10. **Open Terminal:**
    - Press **Cmd + Space** to open Spotlight search
    - Type **"Terminal"**
    - Press **Enter**
    - A black or white window should open

*📸 [Screenshot placeholder: Spotlight search for Terminal]*

11. **Initialize conda for your shell:**
    - In Terminal, type: `~/miniconda3/bin/conda init`
    - Press **Enter**
    - You should see some text about "conda init"

12. **Restart Terminal:**
    - **Close** Terminal (Cmd + Q)
    - **Open** Terminal again
    - You should now see `(base)` at the beginning of your prompt

### Phase 4: Test That Miniconda Works

13. **Test the installation:**
    - In Terminal, type: `conda --version`
    - Press **Enter**
    - You should see something like `conda 23.X.X`

*📸 [Screenshot placeholder: Terminal showing conda version]*

**❌ If you get an error like "conda: command not found":**
- Try: `source ~/.zshrc` (press Enter)
- Or try: `source ~/.bash_profile` (press Enter)
- Then test `conda --version` again
- If still broken, see Troubleshooting section below

### Phase 5: Create Your Data Science Environment

14. **Download the environment file:**
    - Go back to your bootcamp materials
    - Find the file called `ds-bootcamp-env.yml` in the `installation-kit/environments/` folder
    - **Drag this file** to your Desktop (so it's easy to find)

15. **Navigate to your Desktop in Terminal:**
    - Type: `cd ~/Desktop`
    - Press **Enter**

16. **Create the environment:**
    - Type: `conda env create -f ds-bootcamp-env.yml`
    - Press **Enter**
    - **This will take 15-30 minutes** - go grab a coffee! ☕
    
    *💡 You'll see lots of text scrolling - this is normal!*

*📸 [Screenshot placeholder: Terminal showing environment creation progress]*

17. **Activate your environment:**
    - Type: `conda activate ds-bootcamp`
    - Press **Enter**
    - Your Terminal prompt should now show `(ds-bootcamp)` instead of `(base)`

### Phase 6: Set Up Jupyter Widgets

18. **Install additional extensions:**
    ```
    jupyter contrib nbextension install --user
    jupyter nbextensions_configurator enable --user
    jupyter nbextension enable --py widgetsnbextension --sys-prefix
    ```
    - **Copy and paste these one at a time**, pressing Enter after each
    - (In Terminal: Cmd+C to copy, Cmd+V to paste)

19. **Test Jupyter:**
    - Type: `jupyter notebook`
    - Press **Enter**
    - Your web browser should automatically open with Jupyter running
    - You should see a page that says "Jupyter" at the top

*📸 [Screenshot placeholder: Jupyter notebook home page]*

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

## 🔧 Common Issues and Solutions

### Issue 1: "conda: command not found"

**Solution A - Shell Configuration:**
```bash
echo 'export PATH="~/miniconda3/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

**Solution B - Manual Initialization:**
```bash
~/miniconda3/bin/conda init zsh
```
Then restart Terminal.

### Issue 2: "Permission denied" during installation

**Solution:**
1. Try running with `sudo`:
   ```
   sudo conda env create -f ds-bootcamp-env.yml
   ```
2. Enter your Mac password when prompted

### Issue 3: Jupyter won't open in browser

**Solution:**
1. In Terminal, type: `jupyter notebook --no-browser`
2. Copy the URL that appears (looks like `http://localhost:8888/...`)
3. Paste it into your web browser manually

### Issue 4: Widgets don't show up

**Solution:**
1. In Terminal with ds-bootcamp activated:
```bash
conda install -c conda-forge ipywidgets
jupyter nbextension enable --py widgetsnbextension --sys-prefix
```
2. Restart Jupyter

### Issue 5: Apple Silicon (M1/M2/M3) Compatibility Issues

**Solution:**
1. If you get architecture errors, try:
```bash
conda config --env --set subdir osx-64
conda env create -f ds-bootcamp-env.yml
```

### Issue 6: "Package not found" Errors

**Solution:**
1. Update conda first:
```bash
conda update conda
```
2. Try creating environment again

---

## 🍎 Mac-Specific Tips

### Useful Keyboard Shortcuts:
- **Cmd + Space**: Open Spotlight search (to find apps)
- **Cmd + T**: New Terminal tab
- **Cmd + C / Cmd + V**: Copy and paste in Terminal
- **Cmd + Q**: Quit an application completely

### Finding Files:
- **Downloads** are usually in `/Users/YourName/Downloads/`
- **Desktop** items are in `/Users/YourName/Desktop/`
- Use **Finder** (folder icon in dock) to navigate visually

---

## 📞 Getting Help

**If you're stuck:**
1. 📧 Email your instructor with a screenshot of the error
2. 💬 Ask in the class chat/forum
3. 👥 Ask a classmate to help via screen sharing

**When asking for help, please include:**
- Your Mac model (Intel vs Apple Silicon)
- Your macOS version
- The exact error message (copy and paste from Terminal)
- A screenshot of your Terminal

---

## 🎯 Next Steps

Once everything is working:
1. **Create a bootcamp folder:**
   ```bash
   mkdir ~/Documents/DataScienceBootcamp
   cd ~/Documents/DataScienceBootcamp
   ```

2. **Download the bootcamp materials** from your instructor and put them in this folder

3. **Start Jupyter from your bootcamp folder:**
   ```bash
   cd ~/Documents/DataScienceBootcamp
   conda activate ds-bootcamp
   jupyter notebook
   ```

4. **Open** the main bootcamp notebook: `intro-to-data-science.ipynb`

**You're all set! Welcome to your Data Science adventure!** 🚀📊

---

*💡 **Pro Tip:** Save this Terminal command for future use:*
```bash
cd ~/Documents/DataScienceBootcamp && conda activate ds-bootcamp && jupyter notebook
```
*This will navigate to your folder, activate the environment, and start Jupyter all in one go!*