class find:
    def __init__(self,a,b,c):
        self.a = int(a)
        self.b = int(b)
        self.c = int(c)
    def sapxep(self):
        if (self.a >= self.b) and (self.a >= self.c):
            largest = self.a
        elif (self.b >= self.a) and (self.b >= self.c):
            largest = self.b
        else:
            largest = self.c
        print("The largest number is",largest)
kt=find(5,9,8)
kt.sapxep()