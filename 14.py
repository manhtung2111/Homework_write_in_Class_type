class prime:
    def __init__(self,n):
        self.n = int(n)
    def check(self):
        if self.n > 1:
            for i in range (2,self.n):
                if (self.n % i) == 0:
                    print(self.n,"is not a prime number")
                    break
            else:
                print(self.n,"is a prime number")
        else:
            print(self.n, "is not a prime number")
kt = prime(16)
kt.check()