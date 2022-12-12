def greet():
    print('*****************')
    print(' Приветсвуем вас,')
    print(' дорогие игроки, ')
    print('    в игре       ')
    print(' Крестики-нолики ')
    print('*****************')
def show_field(f):
    num = ' 0 1 2'
    print(num)
    for row, i in zip(f,num.split()):
        print(f'{i} {"".join(str(j) for j in row)}')
def users_input(f,user):
    while True:
        place = input(f'Ход: {user}. Введите координаты:').split()
        if len(place)!=2:
            print('**********************')
            print('Введите две координаты')
            print('**********************')
            continue
        if not (place[0].isdigit() and place[1].isdigit()):
            print('Введите числа')
            continue
        x, y = map(int, place)
        if not (x>=0 and x<3 and y>=0 and y<3):
            print('***********************')
            print(' Вы вышли из диапозона ')
            print('Попробуйте ввести снова')
            print('***********************')
            continue
        if f[x][y] != '-':
            print('***************')
            print(' Клетка занята ')
            print('Выберите другую')
            print('***************')
        break
    return x, y
def win(f,user):
    def check_line(a1,a2,a3,user):
        if a1==user and a2==user and a3==user:
            return True
    for n in range(3):
        if check_line(f[n][0],f[n][1],f[n][2], user)or\
        check_line(f[0][n],f[1][n],f[2][n],user) or \
        check_line(f[0][0],f[1][1],f[2][2], user) or \
        check_line(f[2][0],f[1][1],f[0][2], user):
            return True
    return False
def start(field):
    count = 0
    while True:
        show_field(field)
        if count%2==0:
            user='x'
        else:
            user = 'o'
        if count < 9:
            x,y = users_input(field,user)
            field[x][y] = user
        elif count == 9:
            print('Ничья')
            break
        if win(field,user):
            print(f'Выиграл {user}!')
            win(field, user)
            break
        count+=1
field = [['-'] * 3 for _ in range(3)]
greet()
start(field)
