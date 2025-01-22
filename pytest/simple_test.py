# install pytest--pip install pytest
import pytest
def test_addition():
    assert 1+1==2
def test_negative():
    assert (1+1==3) is False
def test_error():
    with pytest.raises(AssertionError):#used to verify the errors
        assert 1+1==3
if __name__=="__main__":#this is to manually call the method when run as python script
    test_addition()
