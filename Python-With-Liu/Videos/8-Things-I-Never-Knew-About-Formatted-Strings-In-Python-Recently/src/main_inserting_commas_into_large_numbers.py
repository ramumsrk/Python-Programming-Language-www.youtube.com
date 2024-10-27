#! /usr/bin/python3.12

import logging_configuration

import logging

# User-defined function
def main() -> None:
    """This is an entry-point function"""
    one_hundred_million: int = 100_000_000
    logging.debug(F'One hundred million: {one_hundred_million:,}')
    ten_billion: int = 10_000_000_000
    logging.debug(F'Ten billion: {ten_billion:,}')
    return None

if __name__ == '__main__':
    logging.debug(f'Module name is: {__name__}')
    logging.debug(f'File constituting module is: {__file__}')
    logging.debug(f'{main()=}')