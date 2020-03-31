class even_odd:
    def __init__(self, n):
        self.n = int(n)
    def check(self):
        if self.n % 2 == 0:
            print(self.n,"is Even")
        else:
            print(self.n,"is Odd")
x = input("Enter your number here:")
kt = even_odd(x)
kt.check()