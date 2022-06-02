def almost_right(data: str) -> int:
    left_count = data.count('(')
    right_count = data.count(')')

    if left_count - right_count == 1:
        return data.index('(')+1
    elif left_count - right_count == -1:
        return data.index(')')+1
    else:
        return (-1)


print(almost_right('a + b = b + a'))
print('-------------')
print(almost_right('d + (a + (b + c) = (a + b) + c + d'))
print('--------------')
print(almost_right('(a((b + c) = ab + bc'))
