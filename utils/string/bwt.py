import functools


"""
Не рабочий модуль для Барроуза-Уилера
"""


# s - input string
# alph - alphabet
# return - BWT of s


def comp(array_of_permutations, alph, length):
    # i.	Проходим циклом по индексам до length
    # ii.	На каждой итерации ищем индексы i-х символов каждой из строк символов в массиве Alph
    # iii.	Если они не равны, прерываем цикл и считаем, что та строка, в которой i-й символ имеет больший индекс в алфавите, должна идти после другой

    for i in range(length):
        if alph.index(array_of_permutations[0][i]) != alph.index(array_of_permutations[1][i]):
            return alph.index(array_of_permutations[0][i]) - alph.index(array_of_permutations[1][i])


def bwt(s, alph):
    if not isinstance(s, str):
        raise ValueError('s must be str')
    if not isinstance(alph, str):
        raise ValueError('alph must be str')
    if not alph:
        raise ValueError('alph must not be empty')
    if not all([c in alph for c in s]):
        raise ValueError('s must contain only chars from alph')

    s = s + '$'
    s_len = len(s)
    array_of_permutations = [''] * s_len
    array_of_permutations[0] = s

    for i in range(2, s_len):
        s = s[-1] + s[:-1]
        array_of_permutations[i] = s

    # Сортируем array_of_permutations компаратором comp
    array_of_permutations.sort(key=functools.cmp_to_key(comp))
    # 3.	Создаем строку из последних символов всех строк массива array_of_permutations
    s_bwt = ''.join([array_of_permutations[i][-1] for i in range(s_len)])
    return s_bwt
