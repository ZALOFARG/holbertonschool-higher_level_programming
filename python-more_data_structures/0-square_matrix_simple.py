#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    b = []
    for i in range(len(matrix)):
        b_row = []
        for j in range(len(matrix[i])):
            b_row.append(matrix[i][j] ** 2)
        b.append(b_row)
    return b


if __name__ == '__main__':
    square_matrix_simple(matrix=[])
