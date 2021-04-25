import logging
from fresh.filter import filter_fresh_request

server_logging = logging.getLogger("django.server")
server_logging.addFilter(filter_fresh_request)

__version__ = "1.0.7"  # noqa
