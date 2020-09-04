# fake snils
snils1 = '11909885393'
snils2 = 42696272110
snils3 = [snils1,
          snils2,
          '88864390792',
          '84770516655',  # Неверная контрольная сумма
          '51913281575',
          '95058457236',
          '37160918982',  # Неверная контрольная сумма
          '840-302-292 55',
          '615-412-616 59',
          223327916456,  # Лишний символ 12/11
          '247-261-79O 83',  # Буква вместо цифры
          '62935606919',
          ['40195442558', '70545709698', '58417911825']  # Список
          ]


def check_snils(data):
    snils = data
    # Проверяем тип данных
    if isinstance(snils, str):
        # Удаляем лишние символы
        snils = snils.replace('-', '').replace(' ', '')
    elif isinstance(snils, int):
        # Меняем тип данных на str
        snils = str(snils)
    else:
        # При любом другом типе данных делаем return
        return f'СНИЛС: {snils} - Неверный тип данных - {type(snils)}'
    control_sum = int(snils[9:11])
    valid = True

    # Проверяем является ли строка числом, если нет то return
    if not snils.isdigit():
        return f'СНИЛС: {snils} - В СНИЛС содержатся посторонние символы - <isdigit({snils.isdigit()})>'

    # Проверка контрольного числа проводится только для номеров больше номера 001001998
    if not int(snils) > int('001001998'):
        return f'СНИЛС: {snils} - Номер СНИЛС меньше <001001998>'

    # В номере XXX-XXX-XXX не может присутствовать одна и та же цифра три раза подряд. Дефисы при этой проверке
    # игнорируются, т.е. неверными будут все нижеследующие примеры СНИЛСов:

    # Проверяем количество символов
    if len(snils) == 11:
        snils = [x for x in snils[0:9]]
        summa = 0
        for i in range(len(snils), 0, -1):
            summa += i * int(snils[-i])

        # Если сумма меньше 100, то контрольное число равно самой сумме
        if summa < 100 and summa == control_sum:
            return valid
        # Если сумма меньше 100, то контрольное число равно самой сумме
        elif summa == 101 or summa == 100 and control_sum == 00:
            return valid
        # Если сумма больше 101, то его необходимо нацело разделить на 101. Если значение меньше 300, допустимо
        # находить его не делением, а вычитанием из него цифры 101, до тех пор, пока полученная цифра не будет меньше
        # 100. Полученное значение определяется по двум пунктам, указанным выше.
        elif summa > 101 and summa % 101 == control_sum:
            return valid
        else:
            # Если сумма меньше 100, то контрольное число равно самой сумме
            if summa % 101 < 100 and summa == control_sum:
                return valid
            # Если сумма меньше 100, то контрольное число равно самой сумме
            elif summa % 101 == 101 or summa % 101 == 100 and control_sum == 00:
                return valid
            else:
                return f'Неверный СНИЛС'
    else:
        # Если не равно 11 то return
        return f'Неверное количество символов в СНИЛС - <{len(snils)}/11>'


print(check_snils(snils1))
print(check_snils(snils2))

for i in snils3:
    if check_snils(i) != True:
        print(check_snils(i))