#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == []:
        return None
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                print("{}".format(matrix[i][j]), end=" ")
            print()


if __name__ == '__main__':
    print_matrix_integer(matrix=[[]])
