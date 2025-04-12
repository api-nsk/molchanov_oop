class Person:
    def hello():
        print("Hello")
        
print(Person.hello) # <function Person.hello> - "hello" обьект функции.

p = Person()
print(p.hello) # <bound method Person.hello of <__main__.Person object>> - уже связанный метод c указанием на экземпляр класса p

print(Person.hello()) # Hello
# print(p.hello()) # TypeError: Person.hello() takes 0 positional arguments but 1 was given - забыта связка (bound) в виде self

print(type(p.hello), type(Person.hello)) # Surprise mazafaka! <class 'method'> <class 'function'>