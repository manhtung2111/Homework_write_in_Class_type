class matrix:
    def __init__(self, x, y, ):
        self.x = x
        self.y = y
    def count(self):
        result = [[0, 0, 0],
                  [0, 0, 0],
                  [0, 0, 0]]
        for i in range(len(self.x)):
            for j in range(len(self.x[0])):
                result[i][j] = self.x[i][j] + self.y[i][j]
        for r in result:
            print(r)
tinh = matrix([[12,7,3],[4 ,5,6],[7 ,8,9]],[[5,8,1], [6,7,3],[4,5,9]] )
tinh.count()
