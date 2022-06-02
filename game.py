"""
Цель функции: необходимо проверить корректность ввода и цели

1) Создать итерируемый обьект по ответу и таргету
2) Проверить является ли каждый элемент таргета эквивалетным в ответе
3) Вернуть выводом один из трех вариантов ответа
"""


def game(target: str, answer: str)-> None:
    target = list(target)
    answer = list(answer)

    for i in range(0, len(target)):
        if answer[i] == target[i]:
            print('correct')
            target[i] = '@'
        elif answer[i] in target:
            if answer[target.index(answer[i])] != target[target.index(answer[i])]:
                print('present')
                target[target.index(answer[i])] = '@'
            else:
                print('absent')
        elif answer[i] not in target:
            print('absent')
