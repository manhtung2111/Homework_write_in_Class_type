class Fibonaci:
    def __init__(self, n):
        self.n = int(n)
    def check(self):
        n1, n2 = 0, 1
        count = 0
        if self.n <= 0:
            print("Please enter a positive integer")
        elif self.n == 1:
            print("Fibonacci sequence upto", self.n, ":")
            print(n1)
        else:
            print("Chuoi Fibonacci:")
            while count < self.n:
                print(n1)
                nth = n1 + n2
                n1 = n2
                n2 = nth
                count += 1
x = input("Enter the Number:")
day = Fibonaci(x)
day.check()
