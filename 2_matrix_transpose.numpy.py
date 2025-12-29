def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    ans = []
    for i in range(len(a)):
        for j in range(len(a[0])):
            if i == 0:
                ans.append([a[i][j]])
            else:
                ans[j].append(a[i][j])
    return ans

a = [[1, 2, 3], [4, 5, 6]]
print(transpose_matrix(a))  # Output: [[1, 4], [2, 5], [3, 6]]