import math
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
num1 = 3
num2 = 6
sum = num1 +num2
print("tong 2 so la: ", sum)
print(math.sqr(2))