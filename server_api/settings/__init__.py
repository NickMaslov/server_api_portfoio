from .settings import *

# keeping your secret key local
try:
    from .local_settings import *
except ImportError:
    pass
