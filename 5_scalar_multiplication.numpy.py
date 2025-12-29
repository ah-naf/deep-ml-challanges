def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	result = []
	for i in range(len(matrix)):
		new_row = []
		for j in range(len(matrix[0])):
			new_row.append(matrix[i][j] * scalar)
		result.append(new_row)
	return result