print("Hello World")
print("Hello Git")
import math
11
def quadratic_equation(a, b, c):
    """Обчислює коріння квадратного рівняння ax^2 + bx + c = 0.

    Args:
        a: Коефіцієнт a.
        b: Коефіцієнт b.
        c: Коефіцієнт c.

    Returns:
        Tuple(x1, x2): Коріння квадратного рівняння.
    """

    D = b ** 2 - 4 * a * c
    if D >= 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return x1, x2
    else:
        return None, None


if __name__ == "__main__":
    a = int(input("Enter coefficient a: "))
    b = int(input("Enter coefficient b: "))
    c = int(input("Enter coefficient c: "))

    x1, x2 = quadratic_equation(a, b, c)
    if x1 is not None:
        print("Коріння квадратного рівняння: x1 = {}, x2 = {}".format(x1, x2))
    else:
        print("Квадратне рівняння не має коренів.")