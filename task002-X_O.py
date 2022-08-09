# Создайте программу для игры в "Крестики-нолики".


def correct_value(player):
    # result = input(f'\n{player}, твоя очередь брать конфеты: ')
    result = input()
    while not result.isdigit() or not (10 > int(result) > 0):# or int(result) > value:
        result = input(f'{player}, можно вводить значения только от 1 до 9: ')
    return int(result)


def player_init():
    player_1 = input('\nВведите имя первого игрока: ')
    player_2 = input('Введите имя второго игрока: ')
    return player_1, player_2


def draw_field(field):  
    line='-------------'
    print(line)
    for i in range(3):
        print('|',field[0+i*3],'|',field[1+i*3],'|',field[2+i*3],'|')
    print(line)


def win_condition(field):
    if field[0] == field[1] == field[2]:
        return field[0]
    elif field[3] == field[4] == field[5]:
        return field[3]
    elif field[6] == field[7] == field[8]:
        return field[6]
    elif field[0] == field[3] == field[6]:
        return field[0]
    elif field[1] == field[4] == field[7]:
        return field[1]
    elif field[2] == field[5] == field[8]:
        return field[2]
    elif field[0] == field[4] == field[8]:
        return field[0]
    elif field[2] == field[4] == field[6]:
        return field[2]
    elif all(isinstance(x, str) for x in field):
        return 'X=O'
    else:
        return None

player_1, player_2 = player_init()

game_field=list(range(1,10))
turn = 1
while True:
    if turn == 1:
        draw_field(game_field)
        print('Ходит X: ', end='')
        move = correct_value(player_1)
        while move not in game_field:
            print('Это поле уже занято! Выберете свободное поле: ', end='')
            move = correct_value(player_1)
        game_field[game_field.index(move)] = 'X'
        win = win_condition(game_field)
        if win == 'X' or win == 'O':
            draw_field(game_field)
            print(f'Победили {win}!!!')
            break
        if win == 'X=O':
            draw_field(game_field)
            print('НИЧЬЯ!')
            break
        turn = 2
    if turn == 2:
        draw_field(game_field)
        print('Ходит O: ', end='')
        move = correct_value(player_2)
        while move not in game_field:
            print('Это поле уже занято! Выберете свободное поле: ', end='')
            move = correct_value(player_2)
        game_field[game_field.index(move)] = 'O'
        win = win_condition(game_field)
        if win == 'X' or win == 'O':
            draw_field(game_field)
            print(f'Победили {win}!!!')
            break
        if win == 'X=O':
            draw_field(game_field)
            print('НИЧЬЯ!')
            break
        turn = 1

