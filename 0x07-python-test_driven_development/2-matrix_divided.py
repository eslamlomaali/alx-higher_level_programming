#!/usr/bin/python3
"""matrix_divided method module."""


def matrix_divided(matrix, div):
    """Divides all elements of matrix.
    Args:
        matrix: List contain int or float
        div: number to divide matrix
    Returns:
        list: List of lists represen matrix that have been diveded.
    Raises:
        TypeError: If matrix is not list of lists containing int or float.
        TypeError: If sublists are not all same size.
        TypeError: If div is not int or float.
        ZeroDivisionError: If div is zero.
    """
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if not isinstance(matrix, list) or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) " +
                        "of integers/floats")
    for r in matrix:
        if not isinstance(r, list) or len(r) == 0:
            raise TypeError("matrix must be a matrix (list of lists) " +
                            "of integers/floats")
        if len(r) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        for c in r:
            if not isinstance(c, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) " +
                                "of integers/floats")
    return [[round(c / div, 2) for c in r] for r in matrix]

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
