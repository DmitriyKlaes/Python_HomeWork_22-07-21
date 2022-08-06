# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) (доп) Подумайте как наделить бота ""интеллектом""


def is_number(value):  # Определяет является ли строка числом
    try:
        int(value)
        return True
    except:
        return False


def correct_value(value, players, turn):
    result = input(f'{players[turn]}, твоя очередь брать конфеты: ')
    while not is_number(result) or not (29 > int(result) > 0) or int(result) > value:
        if value >= 28:
            result = input(
                f'{players[turn]}, можно вводить значения только от 1 до 28: ')
        else:
            result = input(
                f'{players[turn]}, можно вводить значения только от 1 до {value}: ')
    return int(result)


def player_init():
    player_1 = input('\nВведите имя первого игрока: ')
    player_2 = input('\nВведите имя второго игрока: ')
    return player_1, player_2


def players_draw(player_1, player_2):
    from random import randint as r
    draw = r(1, 2)
    if draw == 1:
        print(f'\nПо результатам жеребьевки первым ходит {player_1}!')
        return {1: player_1, 2: player_2}
    else:
        print(f'\nПо результатам жеребьевки первым ходит {player_2}!')
        return {1: player_2, 2: player_1}


def game_candies(value, players):
    turn = 1
    while value > 0:
        if turn == 1:
            move = correct_value(value, players, turn)
            value -= move
            if value == 0:
                print(f'{players[turn]} ПОБЕДИЛ!!!')
                break
            print(f'Осталось конфет: {value}')
            turn = 2
        if turn == 2:
            move = correct_value(value, players, turn)
            value -= move
            if value == 0:
                print(f'{players[turn]} ПОБЕДИЛ!!!')
                break
            print(f'Осталось конфет: {value}')
            turn = 1


count_candies = 2021
print('___ИГРА В КОНФЕТЫ___')
print('Брать со стола можно от 1 до 28 конфет за раз')
print('Кто последний делает ход - тот победил!')
player_1, player_2 = player_init()
players = players_draw(player_1, player_2)
print(f'\nКолличество конфет на столе: {count_candies}\n')
game_candies(count_candies, players)
