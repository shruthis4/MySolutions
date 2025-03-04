def example(times):

   def decorator(func):

       @functools.wraps(func)

       def wrapper(*args, **kwargs):

           for _ in range(times):

               result = func(*args, **kwargs)

           return result

       return wrapper

   return decorator

@example(times=3)

def greet(name):
    print(f"Hello, {name}!")
