from random import shuffle

NUM_DIGIT = 3
MAX_GUESSES = 10


def main():
    print(
        f"""
        Bagels, логическая игра.

        Я загадал число из {NUM_DIGIT} уникальных цифр.
        Попробуйте угадать его. Вот несколько подсказок:
        Когда я говорю:   Это значит:
            Pico        Одна цифра верна, но не на своем месте.
            Fermi       Одна цифра верна и на своем месте.
            Bagels      Ни одна цифра не верна.

            Например, если секретное число - 248, а ваша догадка - 843, подсказки будут Fermi Pico
        """
    )
    gameover = 0
    esc = 1

    while not gameover:
        secret_num = get_secret_num()
        print("Я загадал число.")
        print(f"У вас есть {MAX_GUESSES} попыток, чтобы угадать.\nДля завершения игры напешите 2")

        num_guesses = 1
        while num_guesses <= MAX_GUESSES and not gameover:
            guess = ""

            while not gameover:
                print(f"Попытка {num_guesses}")
                guess = input("> ")

                if guess == "2":
                    gameover = 1
                    esc = 0
                    break

                if len(guess) != NUM_DIGIT or not guess.isdecimal():
                    print(f"Надо написать {NUM_DIGIT} значное число или 2 для выхода!")
                    continue

                clues = get_clues(guess, secret_num)
                print(clues)
                num_guesses += 1

                if guess == secret_num:
                    gameover = 1
                    break

                if num_guesses > MAX_GUESSES:
                    print("У вас закончились попытки.😞")
                    print(f"Правильный ответ: {secret_num}")
                    break
        
        if esc:
            print("Хотите сыграть еще раз? (1-да, 2-нет)")
            inp = input("> ")
            while inp not in ("1", "2"):
                print("Напишите 1 или 2")
                inp = input("> ")
            if int(inp) == 1: main()
            elif int(inp) == 2: break; gameover = 1
    print("Спасибо за игру")


def get_secret_num():
    numbers = list("0123456789")
    shuffle(numbers)

    secret_num = ""
    for i in range(NUM_DIGIT):
        secret_num += str(numbers[i])
    return secret_num


def get_clues(guess, secret_num):
    clues = []
    if guess == secret_num:
        return "Вы угадали!!!"

    for i in range(len(guess)):
        if guess[i] == secret_num[i]:
            clues.append("Fermi") # правильная цифра на правильном месте
        elif guess[i] in secret_num:
            clues.append("Pico") # правильная цифра, но на неправильном месте

    if len(clues) == 0:
        return "Bagels"  # нет правильных цифр
    else: 
        clues.sort()
        return " ".join(clues)


if __name__ == "__main__":
    main()
