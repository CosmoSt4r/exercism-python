class Matrix:
    def __init__(self, matrix_string):
        self.rows = []
        self.columns = []

        row_strings = matrix_string.split("\n")
        for row in row_strings:
            self.rows.append(list(map(int, row.split())))

        for i in range(len(self.rows[0])):
            current_column = []
            for j in range(len(self.rows)):
                current_column.append(self.rows[j][i])
            self.columns.append(current_column)

    def row(self, index):
        return self.rows[index - 1]

    def column(self, index):
        return self.columns[index - 1]
