import numpy as np

def cosine_similarity(v1, v2):
    dot = 0
    A, B = 0, 0
    for i in range(len(v1)):
        dot += v1[i] * v2[i]
        A += v1[i] ** 2
        B += v2[i] ** 2
    return round(dot / np.sqrt(A*B), 3)