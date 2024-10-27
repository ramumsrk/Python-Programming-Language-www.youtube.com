#! /usr/bin/python3.12

import logging_configuration

import logging

# User-defined function
def main() -> None:
    """This is an entry-point function"""
    first_real_number: float = 3.141_592_653_589_793
    logging.debug(f'Rounding {first_real_number=} to 2 decimal places results in {first_real_number:.2f}')
    second_real_number: float = 0.0000_3141_592_653_589_793
    logging.debug(f'Rounding {second_real_number=} to 2 decimal places results in {second_real_number:.2f}')
    logging.debug(f'Rounding {second_real_number=} to 2 significant digits results in {second_real_number:.2g}')
    logging.debug(f'Rounding {second_real_number=} to 3 significant digits results in {second_real_number:.3g}')
    third_natural_number: int = 314_159
    logging.debug(f'Rounding {third_natural_number=} to 3 significant digits results in {third_natural_number:.3g}')
    return None

if __name__ == '__main__':
    logging.debug(f'Module name is: {__name__}')
    logging.debug(f'File constituting module is: {__file__}')
    logging.debug(f'{main()=}')