import random
import final
def game(name_player):
    rounds = int(input("Сколько раз вы хотите играть?:"))
    for i in range(rounds):
        name, date = random.choice(list(final.FAMOUS_PEOPLE.items()))
        answer = input(f"когда родился {name}")
        if answer == date:
            print(f"Верно {name_player}")
        else:
            print("Неверно")
    print("Пока")