class list_check:
    def __init__(self, my_list):
        self.my_list = list(my_list)
    def myfunc(self):
        result = list(filter(lambda x: (x % 13 == 0), self.my_list))
        print("Numbers divisible by 13 are", result)
kt = list_check([12, 65, 54, 39, 102, 339, 221])
kt.myfunc()


