import pytest
from divisionByZero import divide_numbers

def test_divide_numbers():
    with pytest.raises(ZeroDivisionError):
        divide_numbers(10, 0)
    with pytest.raises(Exception) as e:
        divide_numbers(4,0)

    assert e.type is ZeroDivisionError
    assert "division by zero" in e.value 
    assert divide_numbers(4,2)==pytest.approx(2.1,0.1)
#     TypeError: This is raised when an operation is performed on an object of incorrect type.

# ValueError: This is raised when a function receives an argument of the correct type but an incorrect value.

# FileNotFoundError: This is raised when a requested file or directory is not found.

# IndexError: This is raised when a sequence (such as a list or string) is accessed with an index that is out of range.

# KeyError: This is raised when a dictionary is accessed with a key that does not exist.

# ZeroDivisionError: This is raised when a division operation is performed with zero as the divisor.

# NameError: This is raised when trying to access a variable or function that has not been defined.