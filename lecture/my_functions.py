import numpy as np


def quad(a, b, c):
    root1 = (-b + np.sqrt(b**2 - 4 * a * c)) / (2 * a)
    root2 = (-b - np.sqrt(b**2 - 4 * a * c)) / (2 * a)

    return root1, root2
