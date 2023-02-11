import random
from random import randint, choice
from random import randint

greeting = ('Здравствуйте уважаемые Игроки! Вас приветствует игра "Кофетное изобилие!" '
            'Основные правила игры: '
            'Нам будет дано некоторое количество конфет, '
            'за один ход мы можем взять не более определённого количества, '
            'о котором мы с вами договоримся.'
            'Итак, начнём!')
messages = ['Ваш ход']

start = int(input('Одиночна игра(1) Мультиплеер (0): '))

if start == 0:

    def play_game(n, m, players, messages):
        count = 0
        if n % 10 == 1 and 9 > n > 10:
            letter = 'а'
        elif 1 < n % 10 < 5 and 9 > n > 10:
            letter = 'ы'
        else:
            letter = ''
        while n > 0:
            print(f'{players[count % 2]}, {messages}')
            move = int(input())
            if move > n or move > m:
                print(f'Можно взять не более {m} конфет{letter}, у нас всего {n} конфет{letter}')
                attempt = 3
                while attempt > 0:
                    if n >= move <= m:
                        break
                    print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                    move = int(input())
                    attempt -= 1
                else:
                    return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
            n = n - move
            if n > 0:
                print(f'Осталось {n} конфет{letter}')
            else:
                print('Все конфеты разобраны.')
            count += 1
        return players[not count % 2]

    print(greeting)

    player1 = " Игрок 1"
    player2 = " Игрок 2"
    players = [player1, player2]

    n = int(input('Сколько конфет будем разыгрывать?\n '))
    m = int(input('Сколько максимально будем брать конфет за один ход?\n '))

    winer = play_game(n, m, players, messages)
    if not winer:
        print('У нас нет победителя.')
    else:
        print(f'Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!')

else:

    def introduce_players():
        player1 = " Игрок "
        player2 = "AI"
        return [player1, player2]

    def get_rules(players):
        n = int(input("Сколько конфет будем разыгрывать?\n "))
        m = int(input("Сколько максимально будем брать конфет за один ход?\n "))
        print("Определяем кто ходит первый")
        print("Ходит игрок:(1)")
        print("Ходит AI:(0)")
        first = randint(0, 1)
        if first != 1:
            first = 0
        return [n, m, int(first)]


    def play_game(rules, players, messages):
        count = rules[2]
        print(count)
        if rules[0] % 10 == 1 and 9 > rules[0] > 10:
            letter = "а"
        elif 1 < rules[0] % 10 < 5 and 9 > rules[0] > 10:
            letter = "ы"
        else:
            letter = ""
        while rules[0] > 0:
            if not count % 2:
                move = rules[0] % rules[1] + 1
                print(f"Ai забирает {move}")
            else:
                print(f"{players[0]}, {choice(messages)}")
                move = int(input())
                if move > rules[0] or move > rules[1]:
                    print(f"Это слишком много, можно взять не более {rules[1]} конфет{letter}, у нас всего {rules[0]} конфет{letter}")
                    attempt = 3
                    while attempt > 0:
                        if rules[0] >= move <= rules[1]:
                            break
                        print(f"Попробуйте ещё раз, у Вас {attempt} попытки")
                        move = int(input())
                        attempt -= 1
                    else:
                        return print(f"Очень жаль, у Вас не осталось попыток. Game over!")
            rules[0] = rules[0] - move
            if rules[0] > 0:
                print(f"Осталось {rules[0]} конфет{letter}")
            else:
                print("Все конфеты разобраны.")
            count += 1
        return players[not count % 2]


    print(greeting)

    players = introduce_players()
    rules = get_rules(players)

    winer = play_game(rules, players, messages)
    if not winer:
        print("У нас нет победителя.")
    else:
        print(f"Поздравляю! В этот раз победил {winer}! Ему достаются все конфеты!")

