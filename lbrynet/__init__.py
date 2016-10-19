import logging
from conf import Config

__version__ = "0.6.7"
version = tuple(__version__.split('.'))
settings = Config()
logging.getLogger(__name__).addHandler(logging.NullHandler())