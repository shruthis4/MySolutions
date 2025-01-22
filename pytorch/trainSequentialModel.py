from simpleSequential import simpleSequential
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
x_train = torch.randn(100,3).to(device)
y_train = torch.randint(0,5,(100,2),dtype=torch.float).to(device)
data = TensorDataset(x_train,y_train)
data_load =  DataLoader(data,batch_size=10,shuffle=True)
model = simpleSequential().to(device)
criteria = nn.MSELoss()
optimizer = optim.SGD(model.parameters(),lr=0.1)
num_epoch = 10
for i in range(num_epoch):
    total_loss = 0
    for x,y in data_load:
        optimizer.zero_grad()
        yhat=model(x)
        loss = criteria(yhat,y)
        loss.backward()
        optimizer.step()
        total_loss+=loss.item()
    print(f'Epoch: {i}, Loss :{total_loss/len(data_load):.4f} ')

torch.save(model.state_dict(),'sequentialModel.pth')






