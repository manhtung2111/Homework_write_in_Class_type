import random
class rand:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def ngaunhien(self):
        print(random.randint(self.a,self.b))
ran = rand(5,9)
ran.ngaunhien()
