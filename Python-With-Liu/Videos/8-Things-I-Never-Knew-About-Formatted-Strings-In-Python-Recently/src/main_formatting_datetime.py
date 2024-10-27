#! /usr/bin/python3.12

import logging_configuration

import logging
from datetime import datetime as datetime

# User-defined function
def main() -> None:
    """This is an entry-point function"""
    today: datetime = datetime.now()
    logging.debug(f'Today is {today=}')
    logging.debug(F'Today is {today:%Y-%m-%d %H:%M:%S %Z %z}')
    return None

if __name__ == '__main__':
    logging.debug(f'Module name is: {__name__}')
    logging.debug(f'File constituting module is: {__file__}')
    logging.debug(f'{main()=}')