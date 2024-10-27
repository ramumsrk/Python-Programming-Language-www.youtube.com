#! /usr/bin/python3.12

import logging_configuration

import logging
from dataclasses import dataclass
from typing import List

@dataclass(frozen=True)
class Person:
    person_name: str
    person_age: int

# User-defined function
def main() -> None:
    """This is an entry-point function"""
    person_tom: Person = Person(person_name="Tom", person_age=30)
    person_introduction_template: str = "My name is '{person_name}', and my age is '{person_age}'".format(person_name=person_tom.person_name,person_age=person_tom.person_age)
    logging.debug(person_introduction_template)
    tom_person: Person = Person(person_name="Tom", person_age=30)
    jerry_person: Person = Person(person_name="Jerry", person_age=40)
    spike_person: Person = Person(person_name="Spike", person_age=50)
    list_of_persons: List[Person] = [tom_person, jerry_person, spike_person]
    for a_person in list_of_persons:
        a_person_introduction_template: str = 'My name is "{person_name}", and my age is "{person_age}"'.format(person_name=a_person.person_name,person_age=a_person.person_age)
        logging.debug(a_person_introduction_template)
    return None

if __name__ == '__main__':
    logging.debug(f'Module name is: {__name__}')
    logging.debug(f'File constituting module is: {__file__}')
    logging.debug(f'{main()=}')