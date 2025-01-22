import sys
def divide_numbers(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
        raise
    except Exception as e:
        print(f"Exception type {type(e).__name__}")
    else:
        return result
    finally:
        print("ExecutionComplete")
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python divide.py <numerator> <denominator>")
    else:
        try:
            # Convert command-line arguments to floats
            numerator = float(sys.argv[1])
            denominator = float(sys.argv[2])
            result = divide_numbers(numerator, denominator)
            if result is not None:
                print(f"Result: {result}")
        except ValueError:
            print("Error: Please provide valid numbers.")