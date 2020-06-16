from typing import Union, Sequence


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Calculate min cost of getting to the top of stairway if agent can go on next or through one step.

    :param stairway: list of ints, where each int is a cost of appropriate step
    :return: minimal cost of getting to the top
    """
    # определяем начальный список стоимости перехода по ступенькам
    sum_cost = [0 for _ in range(len(stairway))]
    sum_cost[0] = stairway[0] # стоимость шага на 1 ступеньку
    sum_cost[1] = stairway[1] # стоимость шага на 2 ступеньку

    for i in range(2, len(stairway)): # цикл начиная со 2 ступеньки и до конца лестницы
        # соимость перехода = стоимость на i-ой ступ. + минимум стоимости(переход с i-2, переход с i-1)
        sum_cost[i] = stairway[i] + min(sum_cost[i-2], sum_cost[i-1])

    return sum_cost[-1] # возвращаем последний результат в списке


# обратное динамическое программирование
def stairway_path_from_end_to_start(stairway):
    sum_cost = [0 for _ in range(len(stairway)+2)]
    sum_cost[0] = 0
    sum_cost[1] = 0

    for i in range(len(stairway)):
        # стоимость перехода на i+2 ступень = стоимость i сутпени + минимум(переход на i, переход на i+1)
        sum_cost[i + 2] = stairway[i] + min(sum_cost[i], sum_cost[i+1])

    return sum_cost[-1]


# рекурсия
def lazy_stairway_path(stairway, len_stairway):
    if len_stairway == 0:
        return stairway[0]
    if len_stairway == 1:
        return stairway[1]

    current_cost = stairway[len_stairway] + \
                   min(lazy_stairway_path(stairway, len_stairway-2), lazy_stairway_path(stairway, len_stairway-1))

    return current_cost


if __name__ == "__main__":
    n1 = [3, 2, -4, 7, 1, -2, 8]
    print(stairway_path(n1))
    print(stairway_path_from_end_to_start(n1))
    print(lazy_stairway_path(n1, len(n1)-1)) # вызов конечно кривой...
    n2 = [-2, 5, 1, -3]
    print(stairway_path(n2))
    print(stairway_path_from_end_to_start(n2))
    print(lazy_stairway_path(n2, len(n2)-1))
    n3 = [1, 5, 3, -6, 7, -9, 0, 2, 5]
    print(stairway_path(n3))
    print(stairway_path_from_end_to_start(n3))
    print(lazy_stairway_path(n3, len(n3)-1))

