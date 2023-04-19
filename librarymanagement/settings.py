import socket
if socket.gethostname()=="DESKTOP-G87VIM5":
    from .local_settings import *
else:
    from .production_settings import *

