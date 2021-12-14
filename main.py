import json
import yaml


def deserialization_file(path: str) -> list:
    """
    Десериализует отсортированные записи из файла
    :param path: str
            Путь к файлу
    :return: Список словарей
    """
    with open(path, 'r', encoding="windows-1251") as read_file:
        return yaml.load(read_file, Loader=yaml.Loader)


def serialization_file(path: str, arr: list) -> None:
    """
    Сериализует отсортированные записи в файл
    :param path: str
            Путь к файлу
    :param arr: list
            Список записей
    :return: None
    """

    with open(path, 'w', encoding="windows-1251") as write_file:
        yaml.dump(arr, write_file, sort_keys=False, default_flow_style=False)


def shell_sort(lst: list, key: str) -> list:
    """
    Сортировка Шелла
    :param lst: list
        Список записей
    :param key: str
        Ключ сортировки
    :return: Отсортированный список
    """
    n = len(lst) // 2
    while n > 0:
        for i in range(n, len(lst)):
            tmp = lst[i]
            position = i
            while position >= n and lst[position - n][key] > tmp[key]:
                lst[position] = lst[position - n]
                position -= n
                lst[position] = tmp
        n //= 2

    return lst


res_data = json.load(open("result_117_1.txt", encoding="windows-1251"))
print(*res_data[:10], sep='\n')
while True:
    print("1. Сортировать по полю 'inn'")
    print("2. Сортировать по полю 'work_experience'")
    print("0. Выйти из программы")
    cmd = input("Выберите пункт: ")

    if cmd == "1":
        print("Сортировка по полю 'inn'")
        sort_data = shell_sort(res_data, "inn")
        print(*sort_data[:10], sep='\n')
        serialization_file("sort_data.yaml", sort_data)
        print("Сериализация завершена")
        tmp_data = deserialization_file("sort_data.yaml")
        print("Десериализация завершена")
        print(*tmp_data[:10], sep='\n')

    elif cmd == "2":
        print("Сортировка по полю 'work_experience'")
        sort_data = shell_sort(res_data, "work_experience")
        print(*sort_data[:10], sep='\n')
        serialization_file("sort_data.yaml", sort_data)
        print("Сериализация завершена")
        tmp_data = deserialization_file("sort_data.yaml")
        print("Десериализация завершена")
        print(*tmp_data[:10], sep='\n')
    elif cmd == "0":
        break
    else:
        print("Вы ввели не правильное значение")
