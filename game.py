import vicotri
def ig():
    a = input("Привет как тебя зовут?\n")
    b = input(f"{a},ты готов?(yes/no)")
    if b == "yes":
        vicotri.game(a)
    elif b == "no":
        print('Тогда готовься')
    else:
        print("Ты что араб?")
        ig()