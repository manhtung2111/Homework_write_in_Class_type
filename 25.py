class order:
    def __init__(self,c):
        self.c = c
    def find(self):
        print("The ASCII value of",self.c,"is",ord(self.c))
char = order("p")
char.find()