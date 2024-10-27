#! /usr/bin/python3.12

import logging_configuration

import logging

# User-defined function
def main() -> None:
    """This is an entry-point function"""
    one_hundred: int = 100
    two_hundred: int = 200
    a_string_literal: str = f"""
    Apple   {one_hundred=}
    Orange      {two_hundred=}
    
    Pear            {(one_hundred + two_hundred)=}
    
    Durian
    
    Pineapple
    """
    logging.debug(f'{a_string_literal=}')
    return None

if __name__ == '__main__':
    logging.debug(f'Module name is: {__name__}')
    logging.debug(f'File constituting module is: {__file__}')
    logging.debug(f'{main()=}')