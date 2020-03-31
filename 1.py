class intro:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello World")
        print(" My name is " + self.name)
        print(" I am " + self.age)
hello = intro("Tung","20")
hello.myfunc()

