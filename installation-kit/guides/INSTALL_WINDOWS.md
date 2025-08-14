# 🖥️ Data Science Bootcamp Installation Guide - Windows

**Welcome to your Data Science journey!** 🚀 This guide will help you set up everything you need on your Windows computer. Don't worry if you're new to programming - we'll walk through every single step together!

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

### Step 1: Find Out Your Windows Version
1. **Click** the Windows key + R
2. **Type** `winver` and press Enter
3. **Write down** your Windows version (e.g., Windows 10, Windows 11)

### Step 2: Check if You Have Enough Space
1. **Open** File Explorer (folder icon in taskbar)
2. **Click** "This PC" on the left
3. **Look** at your C: drive - you need at least **5GB free space**
4. If you don't have enough space, delete some files or ask for help!

---

## 📥 Step-by-Step Installation

### Phase 1: Download Miniconda

1. **Open your web browser** (Chrome, Firefox, Edge, etc.)

2. **Go to:** https://docs.conda.io/projects/miniconda/en/latest/

3. **Find the Windows section** and click on:
   - If you have a newer computer (2019+): `Miniconda3 Windows 64-bit`
   - If you have an older computer: `Miniconda3 Windows 32-bit`
   
   *💡 Not sure? Choose 64-bit - it works on most computers!*

4. **Wait for download** - the file will be about 80-100MB
   
   *📸 [Screenshot placeholder: Miniconda download page with Windows options highlighted]*

### Phase 2: Install Miniconda

5. **Find your downloaded file** (usually in Downloads folder)
   - The file name will look like `Miniconda3-latest-Windows-x86_64.exe`

6. **Right-click** the file and select "Run as administrator"
   - If Windows asks "Do you want to allow this app to make changes?" click **Yes**

7. **Follow the installation wizard:**

   **Welcome Screen:**
   - Click **Next**

   **License Agreement:**
   - Click **I Agree** (after reading if you want!)

   **Installation Type:**
   - Choose **"Just Me"** (recommended)
   - Click **Next**
   
   *📸 [Screenshot placeholder: Installation type selection]*

   **Choose Install Location:**
   - **DON'T CHANGE THIS** - use the default location
   - It should be something like `C:\Users\YourName\miniconda3`
   - Click **Next**

   **Advanced Installation Options:**
   - ⚠️ **IMPORTANT**: Check both boxes:
     - ✅ "Add Miniconda3 to my PATH environment variable"
     - ✅ "Register Miniconda3 as my default Python"
   - Click **Install**
   
   *📸 [Screenshot placeholder: Advanced options with both checkboxes checked]*

8. **Wait patiently** - installation takes 5-10 minutes
   - You'll see a progress bar - don't close it!

9. **When finished:**
   - Click **Next**
   - Click **Finish**

### Phase 3: Test That Miniconda Works

10. **Open Command Prompt:**
    - Press **Windows key + R**
    - Type `cmd` and press **Enter**
    - A black window should open

11. **Test the installation:**
    - In the black window, type: `conda --version`
    - Press **Enter**
    - You should see something like `conda 23.X.X`
    
    *📸 [Screenshot placeholder: Command prompt showing conda version]*

**❌ If you get an error like "'conda' is not recognized":**
- Close the command prompt
- Restart your computer
- Try again
- If it still doesn't work, see the Troubleshooting section below

### Phase 4: Create Your Data Science Environment

12. **Download the environment file:**
    - Go back to your bootcamp folder
    - Find the file called `ds-bootcamp-env.yml` in the `installation-kit/environments/` folder
    - **Remember where you saved it!**

13. **In Command Prompt, navigate to the folder:**
    - If you saved it in Downloads, type: `cd C:\Users\%USERNAME%\Downloads`
    - If you saved it elsewhere, type: `cd` followed by the path to your folder

14. **Create the environment:**
    - Type: `conda env create -f ds-bootcamp-env.yml`
    - Press **Enter**
    - **This will take 15-30 minutes** - go grab a coffee! ☕
    
    *📸 [Screenshot placeholder: Terminal showing environment creation progress]*

15. **Activate your environment:**
    - Type: `conda activate ds-bootcamp`
    - Press **Enter**
    - Your command prompt should now show `(ds-bootcamp)` at the beginning

### Phase 5: Set Up Jupyter Widgets

16. **Install additional extensions:**
    ```
    jupyter contrib nbextension install --user
    jupyter nbextensions_configurator enable --user
    jupyter nbextension enable --py widgetsnbextension --sys-prefix
    ```
    - Copy and paste these one at a time, pressing Enter after each

17. **Test Jupyter:**
    - Type: `jupyter notebook`
    - Press **Enter**
    - Your web browser should open with Jupyter running
    - You should see a page that says "Jupyter" at the top
    
    *📸 [Screenshot placeholder: Jupyter notebook home page]*

---

## 🎉 Success Check

### Verify Everything Works

1. **In Jupyter, create a new notebook:**
   - Click **New** → **Python 3**

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

### Issue 1: "conda is not recognized as an internal or external command"

**Solution A - Restart Computer:**
1. Close all windows
2. Restart your computer
3. Try again from Step 10

**Solution B - Manually Add to PATH:**
1. Press Windows key + X, select "System"
2. Click "Advanced system settings"
3. Click "Environment Variables"
4. Under "User variables", find "Path" and click "Edit"
5. Click "New" and add: `C:\Users\YourUsername\miniconda3\Scripts`
6. Click "New" again and add: `C:\Users\YourUsername\miniconda3`
7. Click OK on all windows
8. Restart Command Prompt

### Issue 2: Jupyter won't open in browser

**Solution:**
1. In Command Prompt, type: `jupyter notebook --generate-config`
2. Then type: `jupyter notebook --no-browser`
3. Copy the URL that appears (looks like `http://localhost:8888/...`)
4. Paste it into your web browser

### Issue 3: Widgets don't show up

**Solution:**
1. In Command Prompt with ds-bootcamp activated:
```
conda install -c conda-forge ipywidgets
jupyter nbextension enable --py widgetsnbextension --sys-prefix
```
2. Restart Jupyter

### Issue 4: Permission Errors

**Solution:**
- Always run Command Prompt as Administrator
- Right-click Command Prompt icon and select "Run as administrator"

---

## 📞 Getting Help

**If you're stuck:**
1. 📧 Email your instructor with a screenshot of the error
2. 💬 Ask in the class chat/forum
3. 👥 Ask a classmate to help via screen sharing

**When asking for help, please include:**
- Your Windows version
- The exact error message (copy and paste)
- A screenshot of your Command Prompt

---

## 🎯 Next Steps

Once everything is working:
1. **Download the bootcamp materials** from your instructor
2. **Put them in a folder** like `C:\Users\YourName\Documents\DataScienceBootcamp`
3. **Navigate to that folder** in Command Prompt using `cd`
4. **Start Jupyter** with `jupyter notebook`
5. **Open** the main bootcamp notebook: `intro-to-data-science.ipynb`

**You're all set! Welcome to your Data Science adventure!** 🚀📊

---

*💡 **Tip:** Bookmark this page - you might need to refer back to it during the bootcamp!*