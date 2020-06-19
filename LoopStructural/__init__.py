"""


LoopStructural API
=======================

.. autosummary::
    :toctree:


    interpolators
    modelling
    visualisation
    utils
"""
import logging
from logging.config import dictConfig
import tempfile
from pathlib import Path
from .modelling.core.geological_model import GeologicalModel
from .visualisation.model_visualisation import LavaVuModelViewer
from .visualisation.map_viewer import MapView
levels = {'info':logging.INFO,'warning':logging.WARNING,'error':logging.ERROR,'debug':logging.DEBUG}
def log_to_file(filename,level='info'):
    """Set the logging parameters for log file


    Parameters
    ----------
    filename : string
        name of file or path to file
    level : str, optional
        'info', 'warning', 'error', 'debug' mapped to logging levels, by default 'info'
    """
    level = levels.get(level,logging.WARNING)
    logging.basicConfig(level=level,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename=filename,
                    filemode='w')

def log_to_console(level='warning'):
    """Set the level of logging to the console


    Parameters
    ----------
    level : str, optional
        'info', 'warning', 'error', 'debug' mapped to logging levels, by default 'info'
    """
    level = levels.get(level,logging.WARNING)

    changed_level = False
    for h in logging.getLogger().handlers:
        if type(h) is logging.StreamHandler:
            h.setLevel(level)
            changed_level = True
    if not changed_level:
        console = logging.StreamHandler()
        console.setLevel(level)
        # add the handler to the root logger
        logging.getLogger().addHandler(console)

#set up logging
tempfile.mkdtemp()
if tempfile.tempdir:
    temp_file = tempfile.tempdir+Path('/default-loop-structural-logfile.log')
    log_to_file(temp_file)
log_to_console()