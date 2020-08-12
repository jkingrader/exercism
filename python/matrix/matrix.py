class Matrix:
    def __init__(self, matrix_string):
 
        self.matrix = []
        for row in matrix_string.split("\n"):
            self.matrix.append([int(n) for n in row.split(" ")])

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        # return map(lambda row: row[index-1], self.matrix)
        return (row[index-1] for row in self.matrix)

