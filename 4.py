class triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        s = (self.a + self.b + self.c) / 2
        area_count = (s*(s - self.a)*(s - self.b)*(s - self.c)) ** 0.5
        print("dien tich hinh tam giac la:",area_count)
num = triangle(3, 4, 5)
num.area()