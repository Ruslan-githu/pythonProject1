n = int(input('Введите количество элементов:'))

def rec4(i, num, n):
    if i == n:
        return num
    elif i <= n:
        return rec4(i + 1, num / (-2), n)


print(rec4(0, 1, n))

