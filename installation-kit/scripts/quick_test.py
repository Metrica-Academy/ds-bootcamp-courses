#!/usr/bin/env python3
"""
Quick Test Script for Data Science Bootcamp Installation

This is a minimal test that can be run from the command line to verify
basic functionality. Perfect for a quick check!

Usage:
    python quick_test.py

or simply:
    python -c "import pandas as pd, numpy as np, matplotlib.pyplot as plt; print('✅ Quick test passed! Ready for bootcamp!')"
"""

def quick_test():
    """Run a minimal test of core functionality"""
    try:
        # Test core imports
        import pandas as pd
        import numpy as np
        import matplotlib.pyplot as plt
        import seaborn as sns
        import sklearn
        
        # Test basic operations
        data = np.array([1, 2, 3, 4, 5])
        df = pd.DataFrame({'numbers': data, 'doubled': data * 2})
        
        # Test matplotlib (create but don't show)
        fig, ax = plt.subplots()
        ax.plot(data)
        plt.close(fig)
        
        print("🎉 QUICK TEST PASSED!")
        print("✅ All core libraries are working")
        print("✅ Basic operations successful")  
        print("✅ You're ready for the Data Science Bootcamp!")
        print("\nNext step: Run 'jupyter notebook' and open the bootcamp materials!")
        
        return True
        
    except ImportError as e:
        print(f"❌ IMPORT ERROR: {e}")
        print("⚠️  Some required packages are missing.")
        print("📋 Please run the full verification script: python verify_setup.py")
        return False
        
    except Exception as e:
        print(f"❌ ERROR: {e}")
        print("📋 Please run the full verification script: python verify_setup.py")
        return False

if __name__ == "__main__":
    import sys
    success = quick_test()
    sys.exit(0 if success else 1)