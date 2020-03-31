class find:
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)
    def check(self):
        for num in range (self.a, self.b + 1):
            if num >= 1:
                for i in range (2, num):
                    if (num % i) == 0:
                        break
                else:
                    print(num)
kt = find(1,10)
kt.check()
