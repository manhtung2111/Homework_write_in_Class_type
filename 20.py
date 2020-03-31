class amstrong_list:
    def __init__(self,a , b):
        self.a = int(a)
        self.b = int(b)
    def find(self):
        for num in range(self.a, self.b + 1):
            order = len(str(num)) #tim do dai cua so tuong ung voi so mu
            sum = 0
            temp = num
            while temp > 0:
                digit = temp%10
                sum = sum + digit**order
                temp = temp//10
            if num == sum:
                print(num)
list = amstrong_list(100,2000)
list.find()