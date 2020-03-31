class raiseof:
    def __init__(self,n):
        self.n = n
    def myfunc(self):
        terms = 10
        result = list(map(lambda x: self.n ** x, range(terms+1)))
        #cach dung lambda: giong def, map dung de in ra kq, filter dung de so sanh voi đk
        print("ket qua la:", terms)
        for i in range (terms+1):
            print(self.n,"raised to power",i,"is",result[i])
kq = raiseof(2)
kq.myfunc()
