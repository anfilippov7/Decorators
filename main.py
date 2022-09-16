import datetime
from pygismeteo import Gismeteo
import os

# Задание №1

def write_logger(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        func(*args, **kwargs)
        file = open("logger.txt", "w", encoding='utf-8')
        file.write(f'Дата и время вызова функции {func.__name__}: ')
        file.write(str('{}'.format(start)))
        file.write(f'\nФункция {str(func.__name__)} вызвана с параметрами:{str(*args)} {dict(**kwargs)}')
        file.write(f'\nФункция {str(func.__name__)} возвращает значение температуры: {str(func(*args, **kwargs))} градусов цельсия')
        result = func(*args, **kwargs)
        file.close()
        return f'Температура в городе {str(*args)}{("".join(dict(**kwargs).values()))} {result} градусов'
    return wrapper

# Задание №2

def parametrized_decor(parametr):
    def patch_logger(func):
        def wrapper(*args, **kwargs):
            start = datetime.datetime.now()
            func(*args, **kwargs)
            file = open(log_name, "w", encoding='utf-8')
            file.write(f'Дата и время вызова функции {func.__name__}: ')
            file.write(str('{}'.format(start)))
            file.write(f'\nФункция {str(func.__name__)} вызвана с параметрами: {str(*args)} {dict(**kwargs)}')
            file.write(f'\nФункция {str(func.__name__)} возвращает значение температуры: {str(func(*args, **kwargs))} градусов цельсия')
            result = func(*args, **kwargs)
            file.close()
            return f'Температура в городе {str(*args)}{("".join(dict(**kwargs).values()))} {result} градусов\n' \
                   f'Путь сохраненного файла логирования {parametr}'
        return wrapper
    return patch_logger

log_name = "logger.txt"
base_patch = os.getcwd()
path = os.path.join(base_patch, log_name)

# @write_logger
@parametrized_decor(parametr = path)
def temperature_air(town):
    try:
        gismeteo = Gismeteo()
        search_results = gismeteo.search.by_query(town)
        city_id = search_results[0].id
        current = gismeteo.current.by_id(city_id)
        return current.temperature.air.c
    except:
        print('Некорректные данные!')

print(temperature_air(town="Москва"))

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    temperature_air(town="Москва")