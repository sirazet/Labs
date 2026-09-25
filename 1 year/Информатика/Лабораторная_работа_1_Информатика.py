from string import ascii_uppercase
from math import factorial

alph = '0123456789' + ascii_uppercase


def tenth_for_dots(x, c):
    s = 0
    for i in range(len(str(x))):
        s += float(alph.index(x[i])) * int(c) ** -(i + 1)
    return s


def tenth(x, c):
    if ',' not in str(x):
        x = str(x)[::-1]
        s = 0
        for i in range(len(str(x))):
            s += int(alph.index(x[i])) * int(c) ** i
        return s
    else:
        x1, x2 = x[:str(x).index(',')], x[str(x).index(',') + 1:]
        s1 = tenth(x1, c)
        s2 = tenth_for_dots(x2, c)
        rounded = int((s1 + s2) * 100000 + 0.5) / 100000
        return rounded


def lab0(a, b, c):
    t = tenth(a, b)
    if '.' not in str(t):
        s = ''
        while t > 0:
            s = alph[t % int(c)] + s
            t //= c
        return s
    else:
        parts = str(t).split('.')
        inp = parts[0]
        dop = float('0.' + parts[1])
        s = ''
        for _ in range(5):
            dop *= 2
            if dop > 1:
                s += '1'
                dop -= 1
            else:
                s += '0'
        return lab0(inp, b, c) + '.' + s


def ten_to_thirteen(a, n):
    if n == 10:
        s = ''
        i = 2
        while a:
            s = str(a % i) + s
            a //= i
            i += 1
        return s
    elif n == 11:
        m = str(a)[::-1]
        s = 0
        for i in range(len(m)):
            s += int(m[i]) * factorial(i+1)
        return s
    elif n == 12:
        m = str(a)[::-1]
        s = 0
        for i in range(len(m)):
            s += int(m[i]) * (-10)**i
        return s
    elif n == 13:
        neg = False
        if a < 0:
            a = -a
            neg = True
        digits = []
        while a:
            digits.append(a % 9)
            a //= 9
        for i in range(len(digits)):
            q = digits[i]
            if q > 9 / 2:
                digits[i] = q - 9
                if i + 1 + 1 <= len(digits):
                    digits[i+1] += 1
                else:
                    digits.append(1)
        if neg:
            digits = [-q for q in digits]
        digits.reverse()
        return ''.join(map(str, digits))


print(f'Пример 1: {lab0(83860, 10, 9)}')
print(f'Пример 2: {lab0(11565, 7, 10)}')
print(f'Пример 3: {lab0('56A98', 7, 10)}')
print(f'Пример 4: {lab0('39,82', 10, 2)}')
print(f'Пример 10: {ten_to_thirteen(395, 10)}')
print(f'Пример 11: {ten_to_thirteen(313110, 11)}')
print(f'Пример 12: {ten_to_thirteen(581, 12)}')
print(f'Пример 13: {ten_to_thirteen(22940, 13)}')