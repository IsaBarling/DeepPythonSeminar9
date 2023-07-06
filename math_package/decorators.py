import json

from math_package.quadratic_equation import solve_quadratic_equation

def quadratic_equation_decorator(func):
    def wrapper(filename):
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                a, b, c = map(int, row)
                result = func(a, b, c)
                print(f"Корни квадратного уравнения {a}x^2 + {b}x + {c}: {result}")
    return wrapper

def save_to_json_decorator(func):
    def wrapper(filename, *args):
        result = func(*args)
        data = {
            "filename": filename,
            "arguments": args,
            "result": result
        }
        with open("result.json", "w") as file:
            json.dump(data, file, indent=4)
    return wrapper


@save_to_json_decorator
def multiply(a, b):
    return a * b

solve_quadratic_equation("data.csv")
multiply(2, 3)