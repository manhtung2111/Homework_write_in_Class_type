class factorial:
    def __init__(self, n):
        self.n = int(n)
    def check(self):
        giaithua = 1
        if self.n < 0:
            print("Sorry, factorial does not exist for negative numbers")
        elif self.n == 0:
            print("The factorial of 0 is 1")
        else:
            for i in range (1, self.n + 1):
                giaithua = giaithua*i
            print("giai thua cua",self.n,"la:",giaithua)
kt = factorial(5)
kt.check()