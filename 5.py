class phuongtrinh:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def myfunc(self):
        d = (self.b**2) - (4  * self.a * self.c)
        x = (-self.b + d**0.5)/(2 * self.a)
        y = (-self.b - d**0.5)/(2 * self.a)
        print("Nghiem cua pt la ", x, y)
pt = phuongtrinh(1, -2, 1)
pt.myfunc()