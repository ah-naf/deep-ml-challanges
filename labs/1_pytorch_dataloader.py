import torch
import torch.nn.functional as F

class MyTransform:
    def __call__(self, x: torch.Tensor) -> torch.Tensor:
        """
        x: (1, 28, 28) float tensor in [0,1]
        Return: transformed tensor, same shape/dtype.
        Must be non-identity and deterministic.
        """
        brightness_factor = 0.2
        contrast_factor = 1.5

        mean, std = x.mean(), torch.clamp(x.std(), min=1e-5)

        x = (x - mean) / std

        x = x + brightness_factor
        x = x * contrast_factor

        x = x.clamp(-3.0, 3.0)

        return x

import torch
x = torch.rand(1,28,28)
T = MyTransform()
y = T(x)
print(y.shape == x.shape)