from .base import *

from .prod import *  # default for production
try:
    from .local import *  # default for development
except:
    pass
