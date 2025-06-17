

import random


def get_secret_word() -> str: #Esto indica el tipo de dato que va a devolver, asegurando que sea un string
    palabras = ['palabra','python','laravel','spring','testing','frondend','backend','developer']
    return random.choice(palabras)

def show_progress(secret_word, guessed_letters):
    guessed = ""

    for letter in secret_word:
        if letter in guessed_letters:
            guessed += letter
        else:
            guessed += "_"

    return guessed


def hangman_game():
    secret_word = get_secret_word()
    guessed_letters = []
    max_try = 7
    ended_game = False

    print("Bienvenid@ al juego del ahorcado")
    print(f"Tienes {max_try} intentos para adivinar la palabra secreta")
    print("Todas las palabras están en minúscula, sin caracteres especiales")
    print(show_progress(secret_word, guessed_letters))

    while not ended_game and max_try > 0:
        get_word = input("Introduce una letra: ").lower()

        if len(get_word) !=1 or not get_word.isalpha():
            print("Introduzca una letra válida (Sólo una letra)")
        elif get_word in guessed_letters:
            print("Ya has utilizado esa letra, prueba con otra")
        else:
            guessed_letters.append(get_word)

            if get_word in secret_word:
                print(f"Has acertado, la letra {get_word} está en la palabra")
            else:
                max_try -=1
                print(f"F, la letra {get_word} no está en la palabra secreta, pierdes un intento")
                print(f"Te quedan {max_try} intentos")

        current_progress =show_progress(secret_word, guessed_letters)
        print(current_progress)

        if "_" not in current_progress:
            ended_game = True
            print(f"Ganaste, adivinaste la palabra secreta era {secret_word}")

    if max_try == 0:
        print(f"Se acabaron los intentos, la palabra secreta era {secret_word}")

hangman_game()





