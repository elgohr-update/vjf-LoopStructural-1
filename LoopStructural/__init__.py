"""


LoopStructural API
=======================

"""

import logging
from logging.config import dictConfig
import tempfile
from pathlib import Path
from .version import __version__
ch = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s ~ %(name)-12s ~ %(levelname)-10s ~ %(message)s')
ch.setFormatter(formatter)
ch.setLevel(logging.WARNING)
loggers = {}
from .modelling.core.geological_model import GeologicalModel
from .utils import log_to_console, log_to_file, getLogger
logger = getLogger(__name__)
logger.info("Imported LoopStructural")
