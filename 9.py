class celcius:
    def __init__(self,c):
        self.c = c
    def convert(self):
        f = (self.c*1.8) + 32
        print(self.c,"degree Celcius is equal to",f,"degree Farenheit")
doi = celcius(37.5)
doi.convert()