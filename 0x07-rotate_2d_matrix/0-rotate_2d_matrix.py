#!/usr/bin/python3
"""rotate a matric 90 degrees
"""


def rotate_2d_matrix(matrix):
    """rotate matrix 90 degrees clockwise
    """
    # transpose the matrix 1st, make all col to become rows
    i = 0
    mat_length = len(matrix)
    row_length = len(matrix[0])
    while i < mat_length:
        j = i
        while j < row_length:
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
            j += 1
        # reverse row
        matrix[i].reverse()
        i += 1
