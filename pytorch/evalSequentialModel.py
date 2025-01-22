import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader
from simpleSequential import simpleSequential

model = simpleSequential()
model.load_state_dict(torch.load('sequentialModel.pth'))

model.eval()
criteria = nn.MSELoss()
with torch.no_grad():
    x=torch.randn(100,3)
    y=torch.randint(0,5,(100,2),dtype=torch.float)

    dataset = TensorDataset(x,y)
    dataloader = DataLoader(dataset, batch_size=10, shuffle=True)
    total_loss = 0
    for x_i, y_i  in dataloader:
        y_hat = model(x_i)
        loss = criteria(y_hat,y_i)
        total_loss+=loss.item()
    print(f'Loss :{total_loss/len(dataloader):.4f} ')
