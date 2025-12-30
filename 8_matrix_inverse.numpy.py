def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    a, b = matrix[0]
    c, d = matrix[1]
    determinant = a * d - b * c
    
    if determinant == 0:
        return None
    
    inverse_matrix = [[d / determinant, -b / determinant],
                      [-c / determinant, a / determinant]]
    
    return inverse_matrix

matrix = [[4, 7], [2, 6]]
print(inverse_2x2(matrix))  # Output: [[0.6, -0.7], [-0.2, 0.4]]