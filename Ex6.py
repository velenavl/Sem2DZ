# Напишите программу банкомат.
# ✔	Начальная сумма равна нулю
# ✔	Допустимые действия: пополнить, снять, выйти
# ✔	Сумма пополнения и снятия кратны 50 у.е.
# ✔	Процент за снятие — 1.5% от суммы снятия, но не менее 30
# и не более 600 у.е.
# ✔	После каждой третей операции пополнения
# или снятия начисляются проценты - 3 %
# ✔	Нельзя снять больше, чем на счёте
# ✔	При превышении суммы в 5 млн, вычитать налог на богатство 10%
# перед каждой операцией, даже ошибочной
# ✔	Любое действие выводит сумму денег


def invoice(money):
    print(f'На вашем счете {round(money, 2)} y.e.')


def menuAtm():
    print('--'*20)
    print(f'Показать остаток на счете, нажмите : 1')
    print(f'Снять, нажмите : 2')
    print(f'Внести, нажмите : 3')
    print('--' * 20)
    print(f'Для выхода нажмите 0')
    print('--' * 20)


def invoiceOut(money):
    invoice(money)
    while True:
        print(f'Сколько хотите снять со счета? ')
        outMoney = float(input(' ->> '))
        if outMoney > money:
            print(f'{invoice(money)}, введите сумму корректно')
            continue
        if bankTaxMax > outMoney - outMoney/bankTax > bankTaxMin:
            outMoney = outMoney - outMoney/bankTax
        elif bankTaxMin > outMoney - outMoney/bankTax:
            outMoney = outMoney - bankTaxMin  # Снимаем минимальную таксу, не со счета, потому что на счете может не быть суммы для банка
        else:
            outMoney = outMoney - bankTaxMax
        if money > rich:
            money = money - money/tax - outMoney
            break
        else:
            money = money - outMoney
            break
    return money


def invoiceIn(money):
    while True:
        print(f'Сколько хотите положить? (кратно 50)')
        moneyIn = int(input(' ->> '))
        if moneyIn % 50 != 0:
            print(f'Введите сумму кратную 50 ')
            continue
        elif moneyIn % 50 == 0:
            money = money + moneyIn
            break
    return money


# constants
money = 0
bankTax = 1.015
bankTaxMin = 30
bankTaxMax = 600
bankPercent = 1.03
rich = 5000000
tax = 1.1
# программа
opCount = 1  # первая операция
while True:
    menuAtm()
    if opCount % 3 == 0:
        money = money * bankPercent
    button = input(' ->> ')
    if button == '1':
        invoice(money)
    elif button == '2':
        money = invoiceOut(money)
    elif button == '3':
        money = invoiceIn(money)
    elif button == '0':
        break
    else:
        print(f'Ошибка, повторите ')
    opCount += 1

# constant.py

zero = 0
one = 1
two = 2
three = 3
four = 4
five = 5
six = 6
seven = 7
eight = 8
nine = 9

licevoi_chet_10001 = 0
count_10001 = 0
operation_counter = 3
percent_count = 0.03
perсent_min = 30
perсent_avg = 0.015
perсent_max = 600
perсent_luxury_tax = 0.1
line_luxury = 5_000_000

from os import system


def find_Index(id_client):              # Поиск индекса по ID
    index = 0
    index2 = 0
    for i in base_of_clients.id_clients:
        try:
            index2 = i.index(id_client)
        except ValueError:
            index2 = -1
        if index2 != -1:
            break
        index += 1
    if index2 == -1:
        print("Нет такого ID")
        time.sleep(2)
        system("cls")
        Main()
    else:
        return index


def choice_Method(index):            # Выбор метода
    balance(index)
    print('1. Пополнить \n 2. Снять \n 3. Выйти')
    method = int(input('Выберите пункт: '))
    if method == 1:
        luxury_Tax(index)
        top_Up(index)
    elif method == 2:
        check_Balance(index)
        luxury_Tax(index)
        take_Off(index)
    elif method == 3:
        print('Досвидания!')
        exit()
    else:
        choice_Method(index)


def count_Client(money, index):        # Счетчик на операции
    if base_of_clients.id_clients[index][2] < operation_counter:
        base_of_clients.id_clients[index][2] = base_of_clients.id_clients[index][2] + 1
        return
    elif base_of_clients.id_clients[index][2] == operation_counter:
        base_of_clients.id_clients[index][2] = 0
        base_of_clients.id_clients[index][1] = base_of_clients.id_clients[index][1] + \
                                               money * percent_count
        print(f'Начислен кэшбэк в размере {100 * percent_count} %')
        balance(index)
        return


def luxury_Tax(index):               # Налог на роскошь
    if base_of_clients.id_clients[index][1] <= line_luxury:
        return
    elif base_of_clients.id_clients[index][1] > line_luxury:
        base_of_clients.id_clients[index][1] = base_of_clients.id_clients[index][1] - \
                                               base_of_clients.id_clients[index][1] * perсent_luxury_tax
        print(f'Изъят налог на роскошь в размере - {100 * perсent_luxury_tax} %')
        balance(index)
        return


def check_Balance(index):            # Проверка баланса
    if base_of_clients.id_clients[index][1] <= 0:
        print("На вашем счет недостаточно средств для снятия наличных")
        time.sleep(2)
        system("cls")
        choice_Method(index)
    else:
        return


def balance(index):                  # Вывод баланса
    print(f'Ваш баланс: {base_of_clients.id_clients[index][1]} у.е. \n')
    time.sleep(2)
    system("cls")
    return


def top_Up(index):                   # Внесение наличных
    money = int(input('Внесите купюры кратные 50 у.е.: '))
    if money % 50 == 0 and money > 0:
        base_of_clients.id_clients[index][1] = base_of_clients.id_clients[index][1] + money
        count_Client(money, index)
        choice_Method(index)
    else:
        balance(index)
        top_Up(index)


def take_Off(index):                 # Снятие наличных
    money = int(input('Укажите сумму, которую хотите снять: '))
    if (money > 0):
        if ((money + money * perсent_min) <= perсent_min) \
                and ((money + perсent_min) <= base_of_clients.id_clients[index][1]):
            base_of_clients.id_clients[index][1] = base_of_clients.id_clients[index][1] - \
                                                   (money + perсent_min)
            count_Client(money, index)
            choice_Method(index)
        elif ((money + money * perсent_min) >= perсent_max) \
                and ((money + perсent_max) <= base_of_clients.id_clients[index][1]):
            base_of_clients.id_clients[index][1] = base_of_clients.id_clients[index][1] - \
                                                   (money + perсent_max)
            count_Client(money, index)
            choice_Method(index)
        elif ((money * perсent_min) < perсent_max) \
                and ((money + money * perсent_min) <= base_of_clients.id_clients[index][1]):
            base_of_clients.id_clients[index][1] = base_of_clients.id_clients[index][1] - \
                                                   (money + money * perсent_min)
            count_Client(money, index)
            choice_Method(index)
        else:
            print('Данная сумма не доступна для снятия')
            balance(index)
            take_Off(index)
    else:
        print('Вы указали некорректную сумму')
        balance(index)
        choice_Method(index)


def Main():                     # Приветствие
    print("Добро пожаловать в банкомат!")
    id_client = int(input('Укажите свой ID: '))
    index = find_Index(id_client)
    choice_Method(index)


Main()
