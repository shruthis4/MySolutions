import torch
import torch.nn as nn

class simpleSequential(nn.Module):
    def __init__(self):
        super(simpleSequential,self).__init__()
        self.layer = nn.Sequential(nn.Linear(3,2),nn.ReLU(),nn.Linear(2,2))
    def forward(self,x):
        return self.layer(x)


