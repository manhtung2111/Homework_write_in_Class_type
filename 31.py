class fibo:
    def __init__(self, x, y,):
        self.x = x
        self.y = y


    def myfunc(self):
        result = [[0, 0, 0, 0],
                  [0, 0, 0, 0],
                  [0, 0, 0, 0]]
        for i in range(len(self.x)):
            for j in range(len(self.y[0])):
                for k in range(len(self.y)):
                    result[i][j] += self.x[i][k] * self.y[k][j]
        for r in result:
            print (r)
test = fibo([[12,7,3],[4 ,5,6],[7 ,8,9]], [[5,8,1,2], [6,7,3,0],[4,5,9,1]])
test.myfunc()

