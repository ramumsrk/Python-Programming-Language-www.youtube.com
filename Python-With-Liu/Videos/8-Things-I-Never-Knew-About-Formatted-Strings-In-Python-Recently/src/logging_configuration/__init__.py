#! /usr/bin/python3.12

import logging
from pathlib import Path

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S %Z %z',
    filemode='+at',
    filename=f'{Path(__file__).parent.parent.parent}/logs/8_things_I_never_knew_about_formatted_strings_in_Python_recently.log',
)

logging.debug(f'Module name is: {__name__}')
logging.debug(f'Path to module is: {__path__}')
logging.debug(f'File constituting module is: {__file__}')