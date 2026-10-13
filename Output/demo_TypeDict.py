from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int
    alive: bool # the defined types arre merely suggestive but not validating

new_person: Person = {"name": "Ravinandan", "age": 21, "alive": True}

print(new_person)