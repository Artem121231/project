from random import randint
from data import player, enemies, items
from time import sleep


def fight(current_enemy):
    round = randint(1, 2)
    enemy = enemies[current_enemy]
    enemy_hp = enemies[current_enemy]['hp']
    print(f'Противник - {enemy["name"]}: {enemy["script"]}')
    input('Enter чтобы продолжить')
    print()
    while player['hp'] > 0 and enemy_hp > 0:
        if round % 2 == 1:
            print(f'{player["name"]} атакует {enemy["name"]}.')
            enemy_hp -= player['attack']
            sleep(1)
            print(f'''{player['name']} - {player['hp']}
    {enemy['name']} - {enemy_hp}''')
            print()
            sleep(1)
        else:
            print(f'{enemy["name"]} атакует {player["name"]}.')
            player['hp'] -= enemy['attack']
            sleep(1)
            print(f'''{player['name']} - {player['hp']}
    {enemy['name']} - {enemy_hp}''')
            print()
            sleep(1)
        round += 1

    if player['hp'] > 0:
        print(f'Противник - {enemy["name"]}: {enemy["win"]}')
    else:
        print(f'Противник - {enemy["name"]}: {enemy["loss"]}')
        
def displey_player():
    print("Имя:", player["name"])
    print("броня:", player["armor"])
    print("Жизни:", player["hp"])
    print("Урон:", player["attack"])
    print("Удача:", player["luck"])
    print("Деньги:", player["money"])

def displey_enemies():
    for i in range(0,3):
        enemy=enemies[i]
        print("Имя:", enemy["name"])
        print("Жизни:", enemy["hp"])
        print("Урон:", enemy["attack"])
        print("Фраза_Скрипт:", enemy["script"])
        print("Победная_Фраза:", enemy["win"])
        print("Проигрышная_Фраза:", enemy["loss"])

def displey_enemy(qrent_enemy):
    enemy=enemies[qrent_enemy]
    print("Имя:", enemy["name"])
    print("Жизни:", enemy["hp"])
    print("Урон:", enemy["attack"])
    print("Фраза_Скрипт:", enemy["script"])
    print("Победная_Фраза:", enemy["win"])
    print("Проигрышная_Фраза:", enemy["loss"])
 


def train(tip_train):
    if tip_train == "1":
        for i in range(0,101,20):
            sleep(2)
            print(f"Тренировка завершилась на {i} %")
        player["armor"] += 10
        print("Тренировка брони завершена")
    if tip_train == "2":
        for i in range(0,101,20):
            sleep(2)
            print(f"Тренировка завершилась на {i} %")
        player["hp"] += 5
        print("Тренировка здоровья заввершена")
    if tip_train == "3":
        for i in range(0,101,20):
            sleep(2)
            print(f"Тренировка завершилась на {i} %")
        player["attack"] += 5
        print("Тренировка атаки звершена")


def magazine():
    print("Привет, что бы ты хотел купить?")
    print(f'у тебя есть {player["money"]} ')
    item = input()
    if player ["money"] >= items[item]["prace"]:
        print(f'Ты успешно купил {items[item]["name"]} за {items[item]["prace"]} ')
    else: print("не хватает денег")




