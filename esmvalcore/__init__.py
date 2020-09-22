"""ESMValTool core package."""
import logging
import os

from ._config_object import config, drs_config
from ._session import session
from ._version import __version__

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())

__all__ = [
    '__version__',
    'cmor',
    'config',
    'drs_config',
    'session',
    'preprocessor',
]


def get_script_root():
    """Return the location of the ESMValTool installation."""
    return os.path.abspath(os.path.dirname(__file__))
