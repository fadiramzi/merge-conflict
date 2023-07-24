import sys

try:
    x = int(input("x: "))
    y = int(input("y: "))
    result = x / y
    print(f"{x} / {y} = {result}")
except ZeroDivisionError:
    print('Y cannot be Zero')
except Exception:
    print('Invalid numbers')
    sys.exit(0)
