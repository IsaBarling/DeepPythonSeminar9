import math

def solve_quadratic_equation(a, b, c):
    # Вычисляем дискриминант
    discriminant = b**2 - 4*a*c
    
    # Проверяем условия и находим корни
    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2
    elif discriminant == 0:
        x = -b / (2*a)
        return x
    else:
        return None


# Пример вызова функции
roots = solve_quadratic_equation(1, -3, 2)
print("Корни квадратного уравнения:", roots)