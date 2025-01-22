import pytest

@pytest.mark.xfail
def test_add():
    assert 1+3==5

@pytest.mark.skip
def test_sum():
    assert 1+2==3

@pytest.mark.skipif(1+1==2,reason="Skipping this test since 1 and 1 make 2")
def test_avg():
    assert 2+2==5

@pytest.mark.parametrize("test_input,expected_output", [("3+5", 8), ("2+4", 6), ("6*9", 54)])
def test_eval(test_input, expected_output):
    assert eval(test_input) == expected_output