import pytest
import numpy as np

@pytest.fixture
def defineData():
    yield  {"x":np.array([1,2,3]),"y":np.array([2,4,6])}
    print(f"Test Complete")
def test_times2(defineData):
    assert (defineData["x"]*2==defineData["y"]).all()
    # assert np.array_equal(defineData["x"]*2,defineData["y"])