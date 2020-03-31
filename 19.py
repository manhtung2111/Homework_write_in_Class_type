class amstrong:
    def __init__(self,n):
        self.n = int(n)
    def check(self):
        sum = 0
        temp = self.n
        while temp > 0:
            digit = temp%10
            sum = sum + digit ** 3
            temp //= 10 #chia lay phan nguyen (temp = temp // 10)
        if self.n == sum:
            print(self.n,"is an Amstrong number")
        else:
            print(self.n,"is not an Amstrong number")
kt = amstrong(663)
kt.check()