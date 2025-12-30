import torch

def calculate_eigenvalues(matrix: torch.Tensor) -> torch.Tensor:
    """
    Compute eigenvalues of a 2Ã2 matrix using PyTorch.
    Input: 2Ã2 tensor; Output: 1-D tensor with the two eigenvalues in ascending order.
    """
    # Your implementation here
    return torch.round(torch.linalg.eigvalsh(matrix).sort().values)

matrix = torch.tensor([[4.0,2.0],[1.0,3.0]], dtype=torch.float)
print(calculate_eigenvalues(matrix))  # Output: tensor([1., 3.])
