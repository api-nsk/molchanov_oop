from pprint import pprint
class Person:
    name = "Ivan"
    
    def hello():
        print("Hello")

Person.hello()
pprint(dir(Person))
pprint(Person.__dict__)