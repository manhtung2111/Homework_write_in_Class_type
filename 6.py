class doi:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def swap(self):
        temp = self.a
        self.a = self.b
        self.b = temp
        print("The value of x after swapping:", self.a)
        print("The value of x after swapping:", self.b)
doicho = doi(10,5)
doicho.swap()