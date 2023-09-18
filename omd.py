def step2_umbrella():
    print(
        'Утка-маляр взяла зонтик и пошла в бар. '
        'В баре было много людей. '
        'Она заказала коктейль и начала разговор с барменом.'
    )
    return step3()


def step2_no_umbrella():
    print(
        'Утка-маляр пошла в бар без зонтика. '
        'Начался дождь, и она промокла. '
        'В баре она заказала горячий шоколад, чтобы согреться.'
    )
    return step3()


def step3():
    print(
        'После того как утка-маляр закончила свой напиток, '
        'она решила пойти домой. '
        'Она была очень рада своему вечеру в баре!'
    )


def step1():
    print(
        'Утка-маляр решила выпить зайти в бар. '
        'Взять ей зонтик?'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()
    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()
