import torch, torch.nn as nn
from torchsummary import summary
def build_model() -> nn.Module:
    """
    Return a tiny nn.Module for MNIST classification (10 classes).
    IMPORTANT: If total trainable params > 2048, final accuracy will be set to 0.
    Tip: Consider very small convs, global average pooling, and tiny linear head.
    """
    class TinyNet(nn.Module):
         def __init__(self):
             super(TinyNet, self).__init__()
             self.features = nn.Sequential(
                 nn.Conv2d(1, 8, kernel_size=3, padding=1),
                 nn.ReLU(),
                 nn.MaxPool2d(2, 2),
                 nn.Conv2d(8, 16, kernel_size=3, padding=1),
                 nn.ReLU(),
                 nn.MaxPool2d(2, 2)
             )
             self.gap = nn.AdaptiveAvgPool2d(1)
             self.classifier = nn.Linear(16, 10)
         def forward(self, x):
             x = self.features(x)
             x = self.gap(x)
             x = x.view(x.size(0), -1)
             return self.classifier(x)
    return TinyNet()


model = build_model()
total_params = sum(p.numel() for p in model.parameters())
print("Total parameters:", total_params)