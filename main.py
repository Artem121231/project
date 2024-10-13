
from data import player, enemies
import helpers


name = input('Введи своё имя, путник: ')
player['name'] = name
current_enemy = 0

choise = input("Что ты выберешь?")
while choise != "stop":
    if choise == "1":
        helpers.fight(current_enemy)
    elif choise =="2":
        helpers.displey_player()
    elif choise == "3":
        helpers.displey_enemies()
    elif choise == "4":
        current_enemy +=  1 
        if current_enemy == len(enemies):
            current_enemy = 0
        print("Вы выбрали", enemies[current_enemy]["name"])
    elif choise == "5":
        helpers.displey_enemy(current_enemy)
    elif choise == "6":
        print("Выберите тип тренировки")
        tip_train = input()
        helpers.train(tip_train)
    elif choise == "7":
        helpers.magazine()
    choise = input("Что ты выберешь?")
    


    