from collections import namedtuple
class Product(namedtuple('Product', ['name','price'])):
    def list(self):
        return f'{self.name} -> {self.price}'
thing=Product('muzlatgich','230000')
print(thing.list())



class User(namedtuple('User',['name','age'])):
    def checking(self):
        if int(self.age) < 18:
            return 'you are too young'
        print(f'Mr {self.name} you are {self.age} years old , you can use our sites')
john=User(input('enter your name : '),input ('enter your age : '))
print(john.checking())

