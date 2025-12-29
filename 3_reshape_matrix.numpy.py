import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	full_array = []
	for row in a:
		full_array.extend(row)
	
	if len(full_array) != new_shape[0] * new_shape[1]:
		return []

	final_array = []  
	
	for i in range(new_shape[0]):
		start_index = i * new_shape[1]
		end_index = start_index + new_shape[1]
		final_array.append(full_array[start_index:end_index])
	return final_array

a = [[1,2,3,4],[5,6,7,8]]
new_shape = (4, 2)
print(reshape_matrix(a, new_shape))  # Output: [[1, 2], [3, 4], [5, 6], [7, 8]]