
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

def crack_code(code):
    prefix = code[:2]
    origin = code[-2:]
    first = code[2]
    check = code[-3]
    probable_codes = []
    for i in range(0, 9999999):
        try_code = str(i).zfill(7)
        asbld_code = prefix+first+try_code+check+origin
        if check_code(asbld_code):
            probable_codes.append(asbld_code)
    return probable_codes