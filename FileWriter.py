import json
from tqdm import tqdm


class FileWriter:
    """
    Класс FileWriter нужен для записи валидных записей в новый файл.
        Attributes
        ----------
            path : str
                 Путь к файлу, в который записываются валидные записи.
    """
    path: str

    def __init__(self, tmp: str) -> None:
        """
        Инициализирует экземпляр класса.
            Parameters
            ----------
                tmp : str
                    Путь к файлу, в который записываются валидные записи.
        """
        self.path = tmp

    def write_to_file(self, arr) -> None:
        """
        Записывает валидные записи в файл.
            Attributes
            ----------
                arr : list
                    Список записей
        """
        tmp = []
        for i in tqdm(range(len(arr.data)), desc="Запись результата валидации в файл", ncols=100):
            if not (False in arr.validation(i).values()):
                tmp.append(arr.data[i].dictionary.copy())
        json.dump(tmp, open(self.path, "w", encoding="windows-1251"), ensure_ascii=False, sort_keys=False, indent=4)
