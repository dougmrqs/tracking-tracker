
# S10 UPU Standard
# https://en.wikipedia.org/wiki/S10_(UPU_standard)

# def gera_rastreio():
#     from numpy.random import randint
#     rnd_track = randint(10000000, 99999999)
#     code = calc_check_digit(rnd_track)
#     rastreio = 'OJ'+str(code)+'BR'
#     return rastreio

def calc_check_digit(numbers):
    weights = [8, 6, 4, 2, 3, 5, 9, 7]
    splitted_numbers = []
    for n in str(numbers):
        splitted_numbers.append(int(n))
    s = []
    for n in range(len(weights)):
        s.append((splitted_numbers[n]*weights[n]))
        S = sum(s)
        c = 11 - (S%11)
        if c == 11:
            c = 5
        if c == 10:
            c = 0
    splitted_numbers.append(c)
    code = ''
    for n in splitted_numbers:
        code += str(n)
    return code

def check_code(code):
    weights = [8, 6, 4, 2, 3, 5, 9, 7]
    splitted_numbers = []
    numbers = code[2:-3]
    check_digit = code[-3]
    for n in str(numbers):
        splitted_numbers.append(int(n))
    s = []
    for n in range(len(weights)):
        s.append((splitted_numbers[n]*weights[n]))
        S = sum(s)
        c = 11 - (S%11)
        if c == 11:
            c = 5
        if c == 10:
            c = 0
    return int(check_digit) == int(c)