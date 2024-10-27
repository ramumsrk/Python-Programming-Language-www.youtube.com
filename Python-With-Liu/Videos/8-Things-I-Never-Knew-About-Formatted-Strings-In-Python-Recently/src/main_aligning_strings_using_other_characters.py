#! /usr/bin/python3.12

import logging_configuration

import logging

# User-defined function
def main() -> None:
    """This is an entry-point function"""
    a_string_literal: str = 'Apple'
    logging.debug(f'Left aligned string literal: [{a_string_literal:-<20}]')
    logging.debug(f'Left aligned string literal: [{a_string_literal:+<40}]')
    logging.debug(f'Left aligned string literal: [{a_string_literal:?<20}]')
    logging.debug(f'Center aligned string literal: [{a_string_literal:-^20}]')
    logging.debug(f'Right aligned string literal: [{a_string_literal:->20}]')
    logging.debug(f'Left aligned string literal: [{a_string_literal:-<30}]')
    logging.debug(f'Center aligned string literal: [{a_string_literal:-^30}]')
    logging.debug(f'Right aligned string literal: [{a_string_literal:->30}]')
    return None

if __name__ == '__main__':
    logging.debug(f'Module name is: {__name__}')
    logging.debug(f'File constituting module is: {__file__}')
    logging.debug(f'{main()=}')