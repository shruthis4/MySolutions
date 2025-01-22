import numpy
import pickle
import torch
from torch.utils.data import TensorDataset, DataLoader



def pickleModelLoader(pickleFile):
    model = pickleFile.load()
    return(model)
def computeMAPE(yTargets, yPreds):
    yTargets, yPreds = numpy.array(yTargets), numpy.array(yPreds)
    return numpy.mean(numpy.abs((yTargets-yPreds)/yTargets))*100
def runInference(model,inputs):
    model.eval()
    with torch.no_grad():
        return(model(inputs))

if __name__=="__main__":
    x = torch.randn(100,3)
    y = torch.randint(0,5,(100,2),dtype=torch.float)
    dataset = TensorDataset(x,y)
    dataLoader = DataLoader(dataset, batch_size=10, shuffle=True)
    yPred = []
    for inputs in dataLoader:
        yPred = yPred.extend(runInference(inputs))
    computeMAPE(y,yPred)
    