import math
class root:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def myfunc(self):
        sqr_a = self.a ** 2
        sqr_b = self.b ** 2
        sqrt_a = math.sqrt(self.a)
        sqrt_b = math.sqrt (self.b)
        print("binh phuong cua a va b la:",sqr_a,sqr_b)
        print("can bac 2 cua a va b la:", sqrt_a,sqrt_b)
num = root(4,2)
num.myfunc()

