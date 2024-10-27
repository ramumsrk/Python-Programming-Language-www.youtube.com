#! /usr/bin/python3.12

import logging_configuration

import logging
from typing import List, NamedTuple

class PersonTuple(NamedTuple):
    """A class to represent a Person"""
    person_name: str
    person_age: int

# User-defined function
def main() -> None:
    """This is an entry-point function"""
    person_name: str = 'Tom'
    person_age: int = 30
    person_introduction_template: str = 'My name is "%s" and I am "%d" years old.' % (person_name, person_age)
    logging.debug(person_introduction_template)
    tom_person: PersonTuple = PersonTuple(person_name='Tom', person_age=30)
    bob_person: PersonTuple = PersonTuple(person_name='Bob', person_age=40)
    jerry_person: PersonTuple = PersonTuple(person_name='Jerry', person_age=50)
    list_of_person_tuples: List[PersonTuple, ...] = [
        tom_person,
        bob_person,
        jerry_person,
    ]
    for a_person in list_of_person_tuples:
        a_person_introduction_template: str = 'My name is "%s" and I am "%d" years old.' % (a_person.person_name, a_person.person_age)
        logging.debug(a_person_introduction_template)
    return None


if __name__ == '__main__':
    logging.debug(f'Module name is: {__name__}')
    logging.debug(f'File constituting module is: {__file__}')
    logging.debug(f'{main()=}')