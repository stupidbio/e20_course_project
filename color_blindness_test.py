import tkinter
import random

# random.seed(1)

WIDTH = 1200
HEIGHT = 900
H_COUNT = 7
W_COUNT = 7

history = {
    'test_params': [],
    'test_results': [],
}


def init_empty_mask(width, height):
    """
    Маска mask является массивом, состоящим из массивов и задаёт,
    в какой клетке должен быть основной цвет, а в какой - путающийся.
    Если mask[x][y] == 0, то прямоугольник с координатами x,y - одного цвета
    Если mask[x][y] == 1, то другого

    Эта функция генерирует пустую, т.е. состоящую только из нулей маску.

    # Аргументы функции
        width: количество прямоугольников в ширину (координата x)
        height: количество прямоугольников в высоту (координата y)

    # Возвращаемое значение
        mask: массив длины width, состоящий из массивов длины height, состоящих из нулей.

    # Авторы:
        Алисия и Ярослав
    """

    mask = [[0 for i in range(height)] for j in range(width)]
    return mask


def set_answer(mask, x, y):
    """
    Данная функция ставит в маске единицы крестиком вокруг позиции mask[x][y]
    . 1 .
    1 1 1
    . 1 .

    # Аргументы функции:
        mask: маска теста на дальтонизм
        x: индекс отмечаемой позиции (не с краю)
        y: индекс отмечаемой позиции (не с краю)

    # Возвращаемое значение
        mask: подправленная маска теста, в которой позиции x, y и соседние с ней равны 1

    # Авторы:
        Андрей З. и Софья Н.


    """
    mask[x][y] = 1
    mask[x - 1][y] = 1
    mask[x][y - 1] = 1
    mask[x + 1][y] = 1
    mask[x][y + 1] = 1
    return mask


def create_mask(test_params):
    width = test_params['field_width']
    height = test_params['field_height']
    mask = init_empty_mask(width, height)

    x = test_params['x']
    y = test_params['y']
    mask = set_answer(mask, x, y)
    return mask


def prepare_color_str(r, g, b):
    """
    Функция кодирует цвет, заданный тремя яркостями (зелёный, синий, красный)
    в стандартный формат вида #rrggbb, где - xx - цвет x, в 16-ой записи.

    # Аргументы функции
        r: интенсивность красного (целое число от 0 до 255)
        g: интенсивность зелёного (целое число от 0 до 255)
        b: интенсивность синего (целое число от 0 до 255)

    # Возвращаемое значение
        formatted_color: строка #xxxxxx, где x - цифра 16-го алфавита (0123456789abcdef)
    """

    # место для вашего кода
    raise NotImplementedError()

    return formatted_color


def calc_rect_color(is_foreground, test_params):
    """
    Функция выбирает цвет прямоугольника, в зависимости от того,
    является ли он прямоугольником фона или основного объекта.
    И в зависимости от параметров теста.

    # Аргументы функции
        is_foreground: 0 или 1 для заднего и переднего фона соответственно
        test_params: словарь, содержащий параметры теста

    # Возвращаемое значение
        r, g, b - значение интенсивностей по компонентам цвета
    """

    # место для вашего кода
    raise NotImplementedError()

    return r, g, b


def get_color_str(is_ok, test_params):
    return "#8899aa"  # stub answer

    r, g, b = calc_rect_color(is_ok, test_params)
    return prepare_color_str(r, g, b)


def color_mask(mask, test_params):
    for i in range(len(mask)):
        for j in range(len(mask[i])):
            is_ok = mask[i][j]
            mask[i][j] = get_color_str(is_ok, test_params)
    return mask


def select_random_answer(field_width, field_height):
    """
    Функция выбирает, в какой клетке будет загаданный прямоугольник.
    Выбор производится равновероятно случайным образом из всех некрайних клеток.

    # Аргументы функции:
        field_width: ширина поля в прямоугольниках, не меньше 3
        field_height: высота поля в прямоугольниках, не меньше 3

    # Возвращаемое значение
        rect_x, rect_y - координаты загаданного прямоугольника.
    """
    return 1, 1  # stub answer

    return rect_x, rect_y


def gen_test_params(history):
    tests_count = len(history['test_params'])
    answer = select_random_answer(W_COUNT, H_COUNT)

    if tests_count == 15:
        return None # test is finished

    x, y = answer
    params = {
        'field_width': W_COUNT,
        'field_height': H_COUNT,
        'difficulty': 1,
        'x': x,
        'y': y,
        'test_type': 'gb',
    }

    return params


def gen_colored_field(test_params):
    figure = create_mask(test_params)
    test = color_mask(figure, test_params['test_type'])
    return test


def remove_previous_test(canvas):
    canvas.delete(*canvas.find_all())


def get_x_coords(win_width, rects_count, index):
    """
    # Аргументы функции
        win_width: размер окна
        rects_count: количество подотрезков, на которые его нужно разделить
        index: индекс требуемого отрезка

    # Возвращаемое значение
        l, r: левый и правый конец искомого отрезка
    """

    # место для вашего кода

    return 0, win_width # stub answer

    return l, r

def get_y_coords(win_height, rects_count, index):
    """
    # Аргументы функции
        win_height: размер окна
        rects_count: количество подотрезков, на которые его нужно разделить
        index: индекс требуемого отрезка

    # Возвращаемое значение
        l, r: левый и правый конец искомого отрезка
    """

    # место для вашего кода

    return 0, win_height # stub answer

    return l, r


def draw_field(canvas, colored_field):
    field_width = len(colored_field)
    field_height = len(colored_field[0])
    for x in range(field_width):
        for y in range(field_height):
            color = colored_field[x][y]

            x1, x2 = get_x_coords(WIDTH, field_width, x)
            y1, y2 = get_y_coords(HEIGHT, field_height, y)
            canvas.create_rectangle(x1, y1, x2, y2, fill=color, width=0)


def get_rect_x(win_width, rects_count, x):
    """
    Окно приложения расчерчено прямоугольной сеткой. Пользователь кликает в некоторою точку в окне.
    Рассмотрим ось x (ось y немного отличается)
    Все окно целиком занимает по оси x координаты от 0 до win_width,
    оно разбито на прямоугольники одинаковой ширины.

    Функция помогает понять по координатам клика мыши,
    на какой прямоугольник кликнул пользователь

    # Аргументы функции
        win_width: размер окна
        rects_count: количество подотрезков, на которые оно разделено
        x: координата клика

    # Возвращаемое значение
        rect_x: индекс соответствующего прямоугольника (целое число)

    # Авторы
        Василиса и Мария
    """

    t = win_width / rects_count
    rect_x = int(x / t)
    return rect_x

def get_rect_y(win_height, rects_count, y):
    """
    Окно приложения расчерчено прямоугольной сеткой. Пользователь кликает в некоторою точку в окне.
    Рассмотрим ось y (ось x немного отличается)
    Все окно целиком занимает по оси y координаты от 0 до win_height,
    оно разбито на прямоугольники одинаковой ширины.
    В программировании ось y идёт сверху вниз. Но нумеровать мы будем снизу вверх.

    Функция помогает понять по координатам клика мыши,
    на какой прямоугольник кликнул пользователь

    # Аргументы функции
        win_height: размер окна
        rects_count: количество подотрезков, на которые оно разделено
        y: координата клика

    # Возвращаемое значение
        rect_y: индекс соответствующего прямоугольника (целое число)

    # Авторы
        Василиса и Мария
    """

    t = win_height/rects_count
    rect_y = int((win_height-y)/t)
    return rect_y

def get_rect_coords(test_params, x, y):
    rect_x = get_rect_x(WIDTH, test_params['field_width'], x)
    rect_y = get_rect_y(HEIGHT, test_params['field_height'], y)
    return rect_x, rect_y


def check_correct(params, rect_x, rect_y):
    return params['x'] == rect_x and params['y'] == rect_y


def process_answer(history, click_x, click_y):
    prev_params = history['test_params'][-1]
    rect_x, rect_y = get_rect_coords(prev_params, click_x, click_y)
    print("click coords:", rect_x, rect_y) # for debugging

    correct = check_correct(prev_params, rect_x, rect_y)
    history['test_results'].append(correct)


def draw_test_and_save_params(canvas, history, test_params):
    history['test_params'].append(test_params)
    colored_field = gen_colored_field(test_params)
    draw_field(canvas, colored_field)


def stop_application(app_root):
    app_root.destroy()


def print_statistics(results, test_params):
    """
    Функция выписывает статистику пользователя.
    Сколько раз он ответил правильно, а сколько раз - ошибся

    Аргументы:
        results - массив, состоящий из True и False.
            На i-ом месте в массиве стоит True, если пользователь корректно ответил на i-ый тест
        test_params - массив параметров теста. В данной реализации не используется

    Возвращаемые значения:
        Функция ничего не возвращает.

    """

    print("Your result: UNKNOWN/UNKNOWN.")  # stub answer

    # место для вашего кода


def process_click(click_event):
    global canvas, history, app_root  # it would be better without globals (with classes/lambdas)
    process_answer(history, click_event.x, click_event.y)
    remove_previous_test(canvas)

    next_test_params = gen_test_params(history)
    if next_test_params is None:
        print_statistics(history['test_results'], history['test_params'])
        stop_application(app_root) # all tests passed
    else:
        draw_test_and_save_params(canvas, history, next_test_params)


app_root = tkinter.Tk()
canvas = tkinter.Canvas(app_root, width=WIDTH, height=HEIGHT)
canvas.pack()
canvas.bind('<Button-1>', process_click)
first_test_params = gen_test_params(history)
draw_test_and_save_params(canvas, history, first_test_params)
canvas.mainloop()

