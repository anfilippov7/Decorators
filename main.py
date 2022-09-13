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
        file.write(f'\nФункция {str(func.__name__)} вызвана с параметрами:{str(*args)} {str(dict(**kwargs))}')
        file.write(f'\nФункция {str(func.__name__)} возвращает значение температуры: {str(func(*args, **kwargs))} градусов цельсия')
        file.close()
    return wrapper

# Задание №2

def patch_logger(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        func(*args, **kwargs)
        log_name = "logger.txt"
        file = open(log_name, "w", encoding='utf-8')
        file.write(f'Дата и время вызова функции {func.__name__}: ')
        file.write(str('{}'.format(start)))
        file.write(f'\nФункция {str(func.__name__)} вызвана с параметрами: {str(*args)} {str(dict(**kwargs))}')
        file.write(f'\nФункция {str(func.__name__)} возвращает значение температуры: {str(func(*args, **kwargs))} градусов цельсия')
        base_patch = os.getcwd()
        file.write(f'\nПуть к логам {os.path.join(base_patch, log_name)}')
        file.close()
    return wrapper

# @write_logger
@patch_logger
def temperature_air(town):
    try:
        gismeteo = Gismeteo()
        search_results = gismeteo.search.by_query(town)
        city_id = search_results[0].id
        current = gismeteo.current.by_id(city_id)
        return current.temperature.air.c
    except:
        print('Некорректные данные!')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    temperature_air(town="Москва")