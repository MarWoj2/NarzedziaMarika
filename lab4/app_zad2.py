def add_numbers(a, b):
    """Dodawanie dwóch liczb."""
    return a + b

def subtract_numbers(a, b):
    """Odejmowanie drugiej liczby od pierwszej."""
    return a - b

def multiply_numbers(a, b):
    """Mnożenie dwóch liczb."""
    return a * b

def divide_numbers(a, b):
    """Dzielenie pierwszej liczby przez drugą."""
    if b == 0:
        raise ValueError("Dzielenie przez zero jest niedozwolone.")
    return a / b

def main():
    num1 = 10
    num2 = 5
    print(f"Dodawanie: {add_numbers(num1, num2)}")
    print(f"Odejmowanie: {subtract_numbers(num1, num2)}")
    print(f"Mnożenie: {multiply_numbers(num1, num2)}")
    print(f"Dzielenie: {divide_numbers(num1, num2)}")

if __name__ == "__main__":
    main()

