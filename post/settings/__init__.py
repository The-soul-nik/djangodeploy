

from .base import *
try:
    from .local import *
except ImportError:
    print("cant import local settings")