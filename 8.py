class convert:
    def __init__(self, km):
        self.km = km
    def myfunc(self):
        conv_fac = 0.621371
        miles = float(self.km) * conv_fac
        print(self.km," kilometers is equal to ", miles )
x = input("enter value in kilometers:")
doi = convert(x)
doi.myfunc()