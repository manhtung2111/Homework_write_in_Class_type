class matrix:
    def __init__(self, x, y, ):
        self.x = x
    def count(self):
        result = [[0, 0, 0],
                  [0, 0, 0]]
        for i in range(len(self.x)):
            for j in range(len(self.x[0])):
                result[j][i] = self.x[i][j]
        for r in result:
            print(r)
tinh = matrix([[12,7,],[4 ,5,],[8,6]],[[5,8], [6,7],[2,1]] )
tinh.count()
