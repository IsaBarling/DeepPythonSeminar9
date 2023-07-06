from typing import Callable


def create_guessing_game(secret_number: int, max_attempts: int) -> Callable[[], None]:
    def game():
        attempts = 0
        while attempts < max_attempts:
            try:
                guess = int(input("Угадайте число: "))
                if guess == secret_number:
                    print("Вы угадали!")
                    return
                elif guess < secret_number:
                    print("Загаданное число больше")
                else:
                    print("Загаданное число меньше")
                attempts += 1
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите целое число.")
        print("Вы исчерпали все попытки. Загаданное число было", secret_number)

    return game


if __name__ == '__main__':
    while True:
        try:
            secret = int(input("Введите загаданное число от 1 до 100: "))
            if 1 <= secret <= 100:
                break
            else:
                print("Некорректный ввод. Пожалуйста, введите число от 1 до 100.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")

    while True:
        try:
            attempts = int(input("Введите количество попыток от 1 до 10: "))
            if 1 <= attempts <= 10:
                break
            else:
                print("Некорректный ввод. Пожалуйста, введите число от 1 до 10.")
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")

    game_function = create_guessing_game(secret, attempts)
    game_function()

    play_again = input("Хотите сыграть ещё раз? (да/нет): ")
    if play_again.lower() == "да":
        print("Начинаем новую игру!")
        print("------------------------------------")
        main()
    else:
        print("Спасибо за игру. До свидания!")
