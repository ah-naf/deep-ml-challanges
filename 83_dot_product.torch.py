import torch
import numpy as np

def calculate_dot_product(vec1, vec2) -> float:
    vec1_t = torch.as_tensor(vec1, dtype=torch.float)
    vec2_t = torch.as_tensor(vec2, dtype=torch.float)
    return torch.dot(vec1_t, vec2_t).item()

vec1 = np.array([1, 2, 3])
vec2 = np.array([4, 5, 6])

print(calculate_dot_product(vec1, vec2))