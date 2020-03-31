class multi:
    def __init__(self,n):

        self.n = int(n)
    def multi_table(self):
        for i in range (1, 11):
            print(self.n, "x", i , "=", self.n * i)
x = input("Display multiplication table of?")
kt = multi(x)
kt.multi_table()
