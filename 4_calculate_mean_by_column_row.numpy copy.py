def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    ans = []
    if mode == 'column':
        for j in range(len(matrix[0])):
            col_sum = 0
            for i in range(len(matrix)):
                col_sum += matrix[i][j]
            ans.append(col_sum / len(matrix))
    elif mode == 'row':
        for i in range(len(matrix)):
            row_sum = sum(matrix[i])
            ans.append(row_sum / len(matrix[0]))
    else:
        return []
    return ans

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
mode = 'row'
print(calculate_matrix_mean(matrix, mode))  # Output: [4.0, 5.0, 6.0]