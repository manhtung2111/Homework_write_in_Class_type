class two_num:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def myfunc(self):
        sum = self.a + self.b
        minus = self.a - self.b
        multiply = self.a * self.b
        print("tong 2 so la: ",sum)
        print("hieu 2 so la: ", minus)
        print("tich 2 so la: ", multiply)
num = two_num(6.5,9.3)
num.myfunc()
