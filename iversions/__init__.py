"""A cell magic command for IPython/Jupyter to display name and version of the imported modules"""

__version__ = "0.0.1"
__all__ = ['iversions']

from .iversions import IVersions

def load_ipython_extension(ipython):
    ipython.register_magics(IVersions)
