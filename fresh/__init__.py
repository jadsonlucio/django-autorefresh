import logging
from fresh.filter import filter_fresh_request
from fresh.version import __version__

server_logging = logging.getLogger("django.server")
server_logging.addFilter(filter_fresh_request)


