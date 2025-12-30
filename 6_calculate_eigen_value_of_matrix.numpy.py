def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	trace = sum(matrix[i][i] for i in range(len(matrix)))
	determinant = (matrix[0][0] * matrix[1][1]) - (matrix[0][1] * matrix[1][0])
	discriminant = trace**2 - 4 * determinant
	eigenvalue1 = (trace + discriminant**0.5) / 2
	eigenvalue2 = (trace - discriminant**0.5) / 2
	return [max(eigenvalue1, eigenvalue2), min(eigenvalue1, eigenvalue2)]

matrix = [[2, 1], [1, 2]]
print(calculate_eigenvalues(matrix))  # Output: [3.0, 1.0]