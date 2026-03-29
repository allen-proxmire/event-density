"""
Allow running edsim as a module: python -m edsim
"""

import sys
from .cli import main

if __name__ == "__main__":
    sys.exit(main())
