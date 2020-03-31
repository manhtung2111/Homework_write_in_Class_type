class GCD:
    def __init__(self, a,b):
        self.a = int(a)
        self.b = int(b)
    def compute_gnd(self):
        global hcf
        if self.a > self.b:
            smaller = self.b
        else:
            smaller = self.a
        for i in range(1, smaller + 1):
            if ((self.a % i == 0) and (self.b % i == 0)):
                hcf = i
        return hcf

check = GCD(8,6)
print("Uoc chung lon nhat cua 2 so la:", check.compute_gnd())
