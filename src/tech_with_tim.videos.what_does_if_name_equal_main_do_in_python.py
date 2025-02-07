#! /usr/bin/python3.13

from tech_with_tim.videos.what_does_if_name_equal_main_do_in_python.calculator.calculator import addition as addition, subtraction as subtraction

# User-defined function
def main() -> None:
    first_number: int = int(input(f'Enter first number: '))
    second_number: int = int(input(F'Enter second number: '))
    print(f'Sum of {first_number=} and {second_number=} is {addition(first_number, second_number)=}')
    print(f'Difference of {first_number=} and {second_number=} is {subtraction(first_number, second_number)=}')    
    return None

if __name__ == '__main__':
    print(f'Module name is: {__name__}')
    print(F'File constituting module: is {__file__}')
    # Function call
    main()