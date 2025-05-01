import numpy as np

def uniform_intervals(a, b, n):
    """1. создает numpy массив - равномерное разбиение интервала от a до b на n отрезков."""
    return np.linspace(a, b, n + 1)

def cyclic123_array(n):
    """2. Генерирует numpy массив длины  3𝑛 , заполненный циклически числами 1, 2, 3, 1, 2, 3, 1...."""
    return np.tile([1, 2, 3], n)

def first_n_odd_number(n):
    """3. Создает массив первых n нечетных целых чисел"""
    return np.arange(1, 2 * n, 2)

def zeros_array_with_border(n):
    """4. Создает массив нулей размера n x n с "рамкой" из единиц по краям."""
    array = np.zeros((n, n), dtype=int)
    array[0, :] = 1  # верхняя граница
    array[-1, :] = 1  # нижняя граница
    array[:, 0] = 1  # левый край
    array[:, -1] = 1  # правый край
    return array

def chess_board(n):
    """5. Создаёт массив n x n с шахматной доской из нулей и единиц"""
    board = np.zeros((n, n), dtype=int)
    board[1::2, ::2] = 1  # заполняем единицами на четных строках
    board[::2, 1::2] = 1  # заполняем единицами на нечетных строках
    return board

def matrix_with_sum_index(n):
    """6. Создаёт 𝑛 × 𝑛  матрицу с (𝑖,𝑗)-элементами равным 𝑖+𝑗."""
    indices = np.arange(n)
    matrix = indices[:, np.newaxis] + indices  # используем broadcasting для создания матрицы
    return matrix

def cos_sin_as_two_rows(a, b, dx):
    """7. Вычислите $cos(x)$ и $sin(x)$ на интервале [a, b) с шагом dx,
    а затем объедините оба массива чисел как строки в один массив. """
    x = np.arange(a, b, dx)
    cos_values = np.cos(x)
    sin_values = np.sin(x)
    result = np.vstack((cos_values, sin_values))
    return result

def compute_mean_rowssum_columnssum(A):
    """8. Для numpy массива A вычисляет среднее всех элементов, сумму строк и сумму столбцов."""
    mean_value = np.mean(A)
    row_sums = np.sum(A, axis=1)
    column_sums = np.sum(A, axis=0)
    return mean_value, row_sums, column_sums

def sort_array_by_column(A, j):
    """ 9. Сортирует строки numpy массива A по j-му столбцу в порядке возрастания."""
    if j < 0 or j >= A.shape[1]:
        raise ValueError("Индекс столбца j должен быть в пределах от 0 до количества столбцов - 1.")
    sorted_A = A[A[:, j].argsort()]
    return sorted_A

def compute_integral(a, b, f, dx, method):
    """10. Считает определённый интеграл функции f на отрезке [a, b] с шагом dx 3-мя методами:
    method == 'rectangular' - методом прямоугольника
    method == 'trapezoidal' - методом трапеций
    method == 'simpson' - методом Симпсона
    """
    if method not in ['rectangular', 'trapezoidal', 'simpson']:
        raise ValueError("Метод должен быть 'rectangular', 'trapezoidal' или 'simpson'.")
    x = np.arange(a, b, dx)  # Создаем массив значений x на интервале [a, b] с шагом dx

    if method == 'rectangular':  # Метод прямоугольников (левые прямоугольники)
        integral = np.sum(f(x)) * dx

    elif method == 'trapezoidal':  # Метод трапеций
        integral = (dx / 2) * (f(x[0]) + 2 * np.sum(f(x[1:-1])) + f(x[-1]))

    elif method == 'simpson':  # Метод Симпсона
        if len(x) < 3 or len(x) % 2 == 0:
            raise ValueError("Для метода Симпсона требуется нечетное количество точек.")
        integral = (dx / 3) * (f(x[0]) + 4 * np.sum(f(x[1:-1:2])) + 2 * np.sum(f(x[2:-2:2])) + f(x[-1]))
    return integral


