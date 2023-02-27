import random
import sys  
from os.path import exists
from urllib import urlopen
from cowsay import cowsay


def bullscows(guess, secret):
    return (len([i for i in range(len(guess)) if guess[i] == secret[i]]), len([x for x in guess if x in secret]))


def inform(format_string, bulls, cows):
    print(cowsay(format_string.format(bulls, cows)))


def ask(prompt, valid = None):
    guess = input(cowsay(prompt))

    if valid is None:
        return guess

    while True:
        if guess in valid:
            return guess
        print('Неизвестное слово')
        guess = input(cowsay(prompt))


def gameplay(ask, inform, words):
    playing = True
    secret = random.choice(words)
    score = 0

    while playing:
        guess = ask("Введите слово: ", words)
        inform("Быки: {}, Коровы: {}", *bullscows(guess, secret))
        score += 1

        if (guess == secret):
            playing = False
    
    return score

        
while True:
    if len(sys.argv) < 2:
        print("Необходимо верно ввести словарь")
        exit()

    if exists(sys.argv[1]):
        with open(sys.argv[1], "r") as f:
            dict_words = f.read().split()
    else:
        try:
            dict_words = urlopen(sys.argv[1]).read().decode().split()
        except Exception:
            raise ValueError("Словарь не найден")

    if len(sys.argv) > 2:
        try:
            length = int(sys.argv[2])
        except Exception:
            raise ValueError("Длина слова - число")

    dict_words = [x for x in dict_words if len(x) == length]

    print("You are win! Score: ", gameplay(ask, inform, dict_words))