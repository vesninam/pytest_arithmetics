# arithmetics/adder.py

def add_numbers(a, b):
    if isinstance(a, str) or isinstance(b, str):
        raise ValueError
    return a + b