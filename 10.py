class number:
    def __init__(self,n):
        self.n = n
    def check(self):
        if float(self.n) > 0:
            print("Positive number")
        elif float(self.n) == 0:
            print("Zero")
        else:
            print("Negative number")
x = input("Enter your number here:")
kt = number(x)
kt.check()