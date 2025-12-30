import torch

def matrixmul(a, b) -> torch.Tensor:
    """
    Multiply two matrices using PyTorch.
    Inputs can be Python lists, NumPy arrays, or torch Tensors.
    Returns a 2D tensor of shape (m, n) or a scalar tensor -1 if dimensions mismatch.
    """
    a_t = torch.as_tensor(a, dtype=torch.int)
    b_t = torch.as_tensor(b, dtype=torch.int)
    
    if a_t.shape[1] != b_t.shape[0]:
        return torch.tensor(-1)

    return torch.matmul(a_t, b_t)
	

A = [[1,2],[2,4]]
B = [[2,1],[3,4]]

print(matrixmul(A, B))  # Output: tensor([[ 8,  9], [16, 18]])