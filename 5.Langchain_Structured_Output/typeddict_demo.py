from typing import TypedDict

class Person(TypedDict):

  name:str
  age:int

new_person: Person = {'name':'nitin', 'age':20}

print(new_person)