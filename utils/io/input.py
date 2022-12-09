def input_alph():
    alph = input('Введите алфавит: ')
    if alph.strip() == '':
        return None
    if len(alph) != len(set(alph)):
        raise ValueError('alph must not contain duplicate chars')
    return alph


def input_str():
    return input('Введите строку: ').lower()
