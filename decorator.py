import datetime
from contextlib import contextmanager
from datetime import datetime
import os.path

param_for_decorator = 'output_dir'

def logger_decor(param):
    def my_decorator(old_function):
        output_file = 'log.txt'
        path = param + '/' + output_file

        def new_foonction(*args, **kwargs):
            with open(path, 'a', encoding='utf-8') as file:

                file.write(f'{datetime.now()}\n')
                print(datetime.now())
                file.write(f'Имя функции: {old_function.__name__}\n')
                print(f'Имя функции: {old_function.__name__}')
                file.write(f'Аргументы: {args}\n')
                print(f'Аргументы: {args}')
                file.write(f'Результат: {old_function(*args, **kwargs)}\n\n')
                file.write(f'Путь к логам: {os.path.abspath(path)}\n\n')

            return old_function(*args, **kwargs)

        return new_foonction

    return my_decorator


#######################################################################

@logger_decor(param_for_decorator)
def func(num):
    lst = [i for i in range(20000000)]
    low = 0
    high = len(lst) - 1
    count = 0
    while low <= high:
        count += 1
        mid = int((low + high) / 2)
        ges = lst[mid]
        if ges == num:
            return f'\nчисло {ges} было найдено за {count} шага(ов).\n'
        elif ges < num:
            low = mid + 1
        elif ges > num:
            high = mid - 1


@logger_decor(param_for_decorator)
@contextmanager
def timer(foo):
    try:
        start = datetime.now()
        print(f'начало работы: {start}')
        yield  foo
    except Exception as e:
        return f'error ==> {e}'
    finally:
        end = datetime.now()
        print(f'конец работы: {end}')
        print(f'всего времени прошло: {end - start}')


if __name__ == '__main__':
    number = int(input('введите число от 1 до 20 000 000, а я попробую найти его как можно быстрее: '))

    with timer(func) as f:
        print(f(number))
