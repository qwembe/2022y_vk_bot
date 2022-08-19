from math import sqrt


def my_sum(a, b):
    """
    Подсчет простой суммы
    :param a: первое слагаемое
    :param b: второе слагаемое
    :return: сумма a и b
    """
    return a + b


def pip_install_verification():
    """
    Проверка установки пакета
    :return: bool -> True если установка прошла успешно
    """
    import pip_install_test
    return True


def my_distant(point1: tuple = (1, 1), point2: tuple = (2, 2)):
    """
    Нужно написать функцию, которая будет получать 2 кортежа из 2-ух чисел и находить расстояние между ними
    :param point1: Точка в пространстве
    :param point2:
    :return: Евклидово расстояние между точками
    """
    return 0 + 0  # YOUR CODE


def main():
    print(f"sum of 2 and 3 is {my_sum(2, 3)}")
    pip_install_verification()
    print(my_distant())


if __name__ == "__main__":
    main()
