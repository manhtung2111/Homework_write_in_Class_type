class uoc:
    def __init__(self,n):
        self.n = int(n)
    def factor(self):
        print("The factors of", self.n, "are:")
        for i in range(1, self.n + 1):
            if self.n % i == 0:
                print(i)
kq = uoc(320)
kq.factor()
