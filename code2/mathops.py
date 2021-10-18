import datetime

class Calculator:
    def __init__(self):
        pass 

    def add(self, a,b):
        return a + b 

    def multiply(self, a,b):
        return a*b

    def divide(self, a, b):
        if b != 0:
            return a/b
        return "Undefined"

class Talker: 
    def __init__(self):
        pass 

    def sayHello(self):
        return "Hello, how are you!"

    def sayHelloName(self, name):
        if not name: 
            return "Provide a name seriously"
        else: 
            return "Hello, how are you {}".format(name) 
            
    def somedate(self):
        return datetime.date(2014,11,4)
