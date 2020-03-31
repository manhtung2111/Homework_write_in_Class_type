class choice:
    def __init__(self,x,y):
        self.x = float(x)
        self.y = float(y)
    def caculate(self):
        print("Select operation.")
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Divide")
        choice = input("Enter choice(1/2/3/4): ")
        if choice == '1':
            print(self.x, "+", self.y, "=", self.x + self.y)
        elif choice == '2':
            print(self.x, "-", self.y, "=",self.x - self.y)
        elif choice == '3':
            print(self.x, "*", self.y, "=", self.x * self.y)
        elif choice == '4':
            print(self.x, "/", self.y, "=", self.x / self.y)
        else:
            print("Invalid input")
a,b = input("Enter 2 numbers:").split()
chon = choice(a,b)
chon.caculate()