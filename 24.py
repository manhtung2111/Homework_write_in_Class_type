class convert:
    def __init__(self, n):
        self.n = int(n)
    def doi(self):
        print("The decimal value of", self.n , "is :")
        print(bin(self.n), "in binary.")
        print(oct(self.n), "in octal.")
        print(hex(self.n), "in hexadecimal.")
num = convert(344)
num.doi()