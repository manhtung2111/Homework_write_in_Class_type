import calendar
class print_cal:
    def __init__(self,y,m):
        self.y = int(y)
        self.m = int(m)
    def my_calendar(self):
        yy = self.y
        mm = self.m
        print(calendar.month(yy, mm))
lich = print_cal(2020,4)
lich.my_calendar()

