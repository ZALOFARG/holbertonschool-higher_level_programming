#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == []:
        return None
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if j == 2:
                    print("{:d}".format(matrix[i][j]))
                else:
                    print("{:d}".format(matrix[i][j]), end=" ")
            print()


if __name__ == '__main__':
    print_matrix_integer(matrix=[[]])
