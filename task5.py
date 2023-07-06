from typing import Callable
from random import randint
from functools import wraps
import json

def save_to_json(func: Callable[..., None]) -> Callable[..., None]:
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        func_name = func.__name__
        params = {
            'function': func_name,
            'args': args,
            'kwargs': kwargs,
            'result': result
        }
        with open(f"{func_name}.json", 'a') as file:
            json.dump(params, file)
            file.write('\n')
        return result
    return wrapper

def validate_input_ranges(func: Callable[..., None]) -> Callable[..., None]:
    @wraps(func)
    def wrapper(num: int, count: int, *args, **kwargs):
        if not (1 <= num <= 100) or not (1 <= count <= 10):
            num = randint(1, 100)
            count = randint(1, 10)
            print("Введенные числа не входят в допустимые диапазоны. "
                  "Генерируются случайные числа для игры.")

        result = func(num, count, *args, **kwargs)
        return result

    return wrapper

def run_multiple_times(n: int):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@run_multiple_times(3)
@validate_input_ranges
@save_to_json
def game(num: int, count: int):
    for i in range(1, count + 1):
        print(f"Попытка номер {i}")
        try:
            user_num = int(input("Введите число от 1 до 100: "))
        except ValueError:
            print("Ошибка: введено некорректное значение. Повторите попытку.")
            continue

        if user_num == num:
            print("Угадал!!!")
            break
        elif user_num < num:
            print("Ваше число меньше")
        else:
            print("Ваше число больше")

    play_again = input("Хотите сыграть еще раз? (да/нет): ")
    if play_again.lower() == "да":
        main()

def main():
    num = int(input("Загадайте число от 1 до 100: "))
    count = int(input("Укажите количество попыток от 1 до 10: "))
    game(num, count)

if __name__ == '__main__':
    main()
