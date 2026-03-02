def add_number(first_number, second_number = 25):
    """
    first_number = Первое число
    second_number = Второе число (по усолчанию 25)

    Return:
    summ: Сумма чисел
    """
    result = first_number + second_number
    print(result)
    return result

add_number(55, 100)