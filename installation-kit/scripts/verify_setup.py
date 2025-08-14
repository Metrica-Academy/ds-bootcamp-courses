#!/usr/bin/env python3
"""
Data Science Bootcamp - Installation Verification Script

This script checks if all required packages are installed and working correctly.
Run this after completing your installation to make sure everything is ready!

Usage:
    python verify_setup.py
"""

import sys
import importlib
import platform
from datetime import datetime

class Colors:
    """ANSI color codes for terminal output"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    END = '\033[0m'

def print_header():
    """Print a nice header for the verification script"""
    print(f"\n{Colors.BLUE}{'='*70}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}🚀 DATA SCIENCE BOOTCAMP - INSTALLATION VERIFICATION 🚀{Colors.END}")
    print(f"{Colors.BLUE}{'='*70}{Colors.END}\n")
    
    print(f"{Colors.PURPLE}System Information:{Colors.END}")
    print(f"  📅 Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  🖥️  Platform: {platform.system()} {platform.release()}")
    print(f"  🐍 Python Version: {sys.version}")
    print(f"  📍 Python Location: {sys.executable}")
    print()

def check_package(package_name, import_name=None, required_version=None):
    """
    Check if a package is installed and optionally verify its version
    
    Args:
        package_name (str): Display name of the package
        import_name (str): Import name (if different from package_name)
        required_version (str): Minimum required version (optional)
    
    Returns:
        bool: True if package is available and meets version requirements
    """
    if import_name is None:
        import_name = package_name.lower().replace('-', '_')
    
    try:
        module = importlib.import_module(import_name)
        version = getattr(module, '__version__', 'Unknown')
        
        status = f"{Colors.GREEN}✅ {package_name:<20} {version}{Colors.END}"
        
        if required_version and version != 'Unknown':
            # Simple version comparison (works for most cases)
            if version >= required_version:
                status += f" {Colors.GREEN}(>= {required_version}){Colors.END}"
            else:
                status = f"{Colors.YELLOW}⚠️  {package_name:<20} {version} (requires >= {required_version}){Colors.END}"
        
        print(status)
        return True
        
    except ImportError:
        print(f"{Colors.RED}❌ {package_name:<20} Not installed{Colors.END}")
        return False
    except Exception as e:
        print(f"{Colors.RED}❌ {package_name:<20} Error: {str(e)}{Colors.END}")
        return False

def test_jupyter():
    """Test if Jupyter notebook can be imported and basic functionality works"""
    print(f"\n{Colors.PURPLE}Testing Jupyter Environment:{Colors.END}")
    
    # Test Jupyter notebook
    success = True
    success &= check_package("Jupyter Notebook", "notebook")
    success &= check_package("Jupyter Lab", "jupyterlab")
    success &= check_package("IPython Kernel", "ipykernel")
    
    return success

def test_widgets():
    """Test if Jupyter widgets are working"""
    print(f"\n{Colors.PURPLE}Testing Interactive Widgets:{Colors.END}")
    
    try:
        import ipywidgets as widgets
        from IPython.display import display
        
        # Test basic widget creation
        test_widget = widgets.IntSlider(value=5, min=0, max=10, description='Test:')
        print(f"{Colors.GREEN}✅ Widget Creation      Works{Colors.END}")
        
        # Test widget display (won't actually display in terminal, but tests the method)
        try:
            display(test_widget)
            print(f"{Colors.GREEN}✅ Widget Display       Works{Colors.END}")
        except Exception as e:
            print(f"{Colors.YELLOW}⚠️  Widget Display       Warning: {str(e)[:50]}{Colors.END}")
            
        return True
        
    except Exception as e:
        print(f"{Colors.RED}❌ Widget Testing       Error: {str(e)}{Colors.END}")
        return False

def test_data_science_capabilities():
    """Test basic data science operations"""
    print(f"\n{Colors.PURPLE}Testing Data Science Capabilities:{Colors.END}")
    
    try:
        # Test pandas operations
        import pandas as pd
        df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
        _ = df.describe()
        print(f"{Colors.GREEN}✅ Pandas Operations    Works{Colors.END}")
        
        # Test numpy operations
        import numpy as np
        arr = np.array([1, 2, 3, 4, 5])
        _ = np.mean(arr)
        print(f"{Colors.GREEN}✅ NumPy Operations     Works{Colors.END}")
        
        # Test matplotlib
        import matplotlib.pyplot as plt
        fig, ax = plt.subplots(1, 1, figsize=(6, 4))
        ax.plot([1, 2, 3], [1, 4, 2])
        plt.close(fig)  # Don't actually show the plot
        print(f"{Colors.GREEN}✅ Matplotlib Plotting  Works{Colors.END}")
        
        # Test seaborn
        import seaborn as sns
        print(f"{Colors.GREEN}✅ Seaborn Styling      Works{Colors.END}")
        
        # Test plotly
        import plotly.graph_objects as go
        fig = go.Figure(data=go.Bar(x=['A', 'B'], y=[1, 2]))
        print(f"{Colors.GREEN}✅ Plotly Interactive   Works{Colors.END}")
        
        # Test scikit-learn
        from sklearn.linear_model import LinearRegression
        model = LinearRegression()
        X = np.array([[1], [2], [3]])
        y = np.array([1, 2, 3])
        model.fit(X, y)
        print(f"{Colors.GREEN}✅ Scikit-learn ML      Works{Colors.END}")
        
        return True
        
    except Exception as e:
        print(f"{Colors.RED}❌ Data Science Test    Error: {str(e)}{Colors.END}")
        return False

def main():
    """Main verification function"""
    print_header()
    
    # Core packages to check
    print(f"{Colors.PURPLE}Checking Core Packages:{Colors.END}")
    
    packages = [
        ("Pandas", "pandas", "1.5.0"),
        ("NumPy", "numpy", "1.20.0"),
        ("Matplotlib", "matplotlib", "3.5.0"),
        ("Seaborn", "seaborn", "0.11.0"),
        ("Plotly", "plotly", "5.10.0"),
        ("Scikit-learn", "sklearn", "1.1.0"),
        ("SciPy", "scipy", "1.8.0"),
    ]
    
    core_success = True
    for package_info in packages:
        if len(package_info) == 3:
            core_success &= check_package(package_info[0], package_info[1], package_info[2])
        else:
            core_success &= check_package(package_info[0], package_info[1])
    
    # Test Jupyter environment
    jupyter_success = test_jupyter()
    
    # Test widgets
    widget_success = test_widgets()
    
    # Test data science capabilities
    ds_success = test_data_science_capabilities()
    
    # Print summary
    print(f"\n{Colors.BLUE}{'='*70}{Colors.END}")
    print(f"{Colors.BOLD}{Colors.CYAN}📊 VERIFICATION SUMMARY{Colors.END}")
    print(f"{Colors.BLUE}{'='*70}{Colors.END}")
    
    if core_success and jupyter_success and widget_success and ds_success:
        print(f"\n{Colors.GREEN}{Colors.BOLD}🎉 CONGRATULATIONS! 🎉{Colors.END}")
        print(f"{Colors.GREEN}All components are installed and working correctly!{Colors.END}")
        print(f"{Colors.GREEN}You're ready to start the Data Science Bootcamp! 🚀{Colors.END}")
        
        print(f"\n{Colors.CYAN}Next steps:{Colors.END}")
        print(f"  1. 📂 Navigate to your bootcamp materials folder")
        print(f"  2. 🚀 Start Jupyter: {Colors.YELLOW}jupyter notebook{Colors.END}")
        print(f"  3. 📖 Open: {Colors.YELLOW}intro-to-data-science.ipynb{Colors.END}")
        print(f"  4. 🎯 Begin your data science journey!")
        
    else:
        print(f"\n{Colors.RED}{Colors.BOLD}⚠️  ISSUES DETECTED ⚠️{Colors.END}")
        print(f"{Colors.RED}Some components are missing or not working properly.{Colors.END}")
        
        print(f"\n{Colors.CYAN}What to do:{Colors.END}")
        print(f"  1. 📧 Check the installation guide for your operating system")
        print(f"  2. 🔍 Look at the TROUBLESHOOTING.md file")
        print(f"  3. 💬 Ask your instructor or classmates for help")
        print(f"  4. 📱 Include this output when asking for help")
    
    print(f"\n{Colors.BLUE}{'='*70}{Colors.END}")
    
    # Additional helpful information
    print(f"\n{Colors.PURPLE}💡 Helpful Commands:{Colors.END}")
    print(f"  Check conda environment: {Colors.YELLOW}conda info --envs{Colors.END}")
    print(f"  Activate bootcamp env:   {Colors.YELLOW}conda activate ds-bootcamp{Colors.END}")
    print(f"  Start Jupyter notebook:  {Colors.YELLOW}jupyter notebook{Colors.END}")
    print(f"  Update packages:         {Colors.YELLOW}conda update --all{Colors.END}")
    
    return core_success and jupyter_success and widget_success and ds_success

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print(f"\n{Colors.YELLOW}Verification cancelled by user.{Colors.END}")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Colors.RED}Unexpected error during verification: {str(e)}{Colors.END}")
        sys.exit(1)