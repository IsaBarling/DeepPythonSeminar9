from typing import Callable
from random import randint
from functools import wraps


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


def binary_search_game_wrap(func: Callable[..., None]) -> Callable[..., None]:
    @wraps(func)
    def wrapper(num: int, count: int, *args, **kwargs):
        if not (1 <= num <= 100):
            num = randint(1, 100)
            print("Загаданное число не входит в допустимый диапазон. "
                  "Генерируется случайное число.")

        if not (1 <= count <= 10):
            count = randint(1, 10)
            print("Количество попыток не входит в допустимый диапазон. "
                  "Генерируется случайное количество попыток.")

        result = func(num, count, *args, **kwargs)
        return result

    return wrapper


@binary_search_game_wrap
@validate_input_ranges
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
