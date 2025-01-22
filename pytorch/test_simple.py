import torch
import pytest
from simpleModel import simpleModel  # Import your model 
@pytest.mark.parametrize("inputShape,OutputShape",[((100,10),(100,1)),
                                                     ((200,10),(200,1))])

def test_forward(inputShape: tuple[int, int],OutputShape: tuple[int, int]):
    model = simpleModel()
    input = torch.randn(inputShape)
    y = model(input)
    assert y.shape==OutputShape
