import torch

def matrix_dot_vector(a, b) -> torch.Tensor:
    """
    Compute the product of matrix `a` and vector `b` using PyTorch.
    Inputs can be Python lists, NumPy arrays, or torch Tensors.
    Returns a 1-D tensor of length m, or tensor(-1) if dimensions mismatch.
    """
    a_t = torch.as_tensor(a, dtype=torch.float)
    b_t = torch.as_tensor(b, dtype=torch.float)
    ans = torch.tensor([])

    # Dimension mismatch check
    if a_t.size(1) != b_t.size(0):
        return torch.tensor(-1)
    # Your implementation here
    for i in range(a_t.size(0)):
        row = a_t[i]
        dot_product = torch.dot(row, b_t).unsqueeze(0)
        ans = torch.cat((ans, dot_product), dim=0)
    return ans


a = [[1, 2], [2, 4]]
b = [1, 2]
result = matrix_dot_vector(a, b)
print(result)  # Expected output: tensor([ 5., 10.])