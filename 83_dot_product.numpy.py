import numpy as np

def calculate_dot_product(vec1, vec2) -> float:
    n = len(vec1)
    ans = 0
    for i in range(n):
        ans += vec1[i]*vec2[i]
    return ans