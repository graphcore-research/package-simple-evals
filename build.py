"""
Custom build command for setuptools to run our package setup script.
"""

import os
import subprocess
import sys
from setuptools.command.build_py import build_py as _build_py

class BuildCommand(_build_py):
    """Custom build command to run setup_package.py before building."""
    
    def run(self):
        """Run setup_package.py and then continue with the standard build process."""
        # Run the setup_package.py script to copy files
        setup_script = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'setup_package.py')
        
        try:
            print("Running setup_package.py to prepare the package structure...")
            subprocess.check_call([sys.executable, setup_script])
        except subprocess.CalledProcessError as e:
            sys.stderr.write(f"Error: Failed to run setup_package.py: {e}\n")
            sys.exit(1)
        
        # Continue with the standard build process
        _build_py.run(self) 