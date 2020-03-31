class sum:
    def __init__(self,n):
        self.n = int(n)
    def tong(self):
        sum = 0
        for i in range (self.n + 1) :
            sum = sum+i
            i=i+1
        print("tong cua n so la:",sum)
sumlist = sum(16)
sumlist.tong()