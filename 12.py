class leap_year:
    def __init__(self, n):
        self.n = int(n)
    def check(self):
        if (self.n % 4) == 0:
            if(self.n % 100) == 0:
                if (self.n % 400) == 0:
                    print(self.n,"is a leap year")
                else:
                    print(self.n,"is not a leap year")
            else:
                print(self.n,"is a leap year")
        else:
            print(self.n,"is not a leap year")
x = input("Enter your year here:")
kt = leap_year(x)
kt.check()