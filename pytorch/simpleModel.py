import torch
import torch.nn as nn
class simpleModel(nn.Module):
    def __init__(self):
        super().__init__() 
        self.linear = nn.Linear(10, 1)

    def forward(self, x):
        return self.linear(x)
    