from mathops import Calculator

class ToyExample:
    def __init__(self):
        self.calc = Calculator()
    
    def useless_code_1(self):
        for i in range(100):
            res = self.calc.add(1,2)
        return None
    def useless_code_2(self):
        for i in range(1, 200, 2):
            res = self.calc.multiply(2,3)
        return None

if __name__ == "__main__":
    te = ToyExample()
    value1 = te.useless_code_1()
    value2 = te.useless_code_2()
