class Matrix:
    def __init__(self, matrix_string):
        matrix_rows = matrix_string.split("\n")
        num_rows = len(matrix_rows)
        
        self.matrix = []
        row_idx = 0
        while row_idx < num_rows:
            row_strs = matrix_rows[row_idx].split(" ")
            row_vals = [int(n) for n in row_strs]
            self.matrix.append(row_vals)
            row_idx += 1
        self.num_rows = num_rows
        self.num_cols = len(self.matrix[0])

    def row(self, index):
        return self.matrix[index-1]

    def column(self, index):
        # return map(lambda row: row[index-1], self.matrix)
        return (row[index-1] for row in self.matrix)

