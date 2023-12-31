#!/usr/bin/python3
"""In this module we would work operating with lists"""
def matrix_divided(matrix, div):
    """Divides all elements of a matrix.

    Parameters:
        matrix (list): list of integers or floats
        div (int or float): number to divide all elements of the matrix.

    Raises:
        TypeError: If matrix is not a list of list of integers or floats.
        TypeError: If each row of the matrix is not of the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.

    Returns:
        list: All elements of the matrix divided by div, rounded to 2 decimal.
        """
    if not isinstance(matrix, list) or not all(isinstance(row, list) and all(
            isinstance(i, (int, float)) for i in row) for row in matrix):
        raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    result_matrix = [
            [round(element / div, 2) for element in row]
            for row in matrix
    ]

    return result_matrix
