import re


class CheckValidation:
    """
    Объект класса CheckValidation обрабатывает запись о научном сотруднике.
    Используется для хранения полей записи и их валидации.
        Attributes
        ----------
            dictionary : dict
                Словарь хранит записи в виде "тип данных о сотруднике": данные о сотруднике.
    """
    dictionary: dict

    def __init__(self, tmp: dict) -> None:
        """
        Инициализирует экземпляр класса записи.
            Parameters
            ----------
                tmp : dict
                    Копия списка с полями записи.
        """
        self.dictionary = tmp.copy()

    def check_email(self) -> bool:
        """
        Проверяет электронную почту на валидность.
            Returns
            -------
                bool:
                    Результат проверки на корректность.
        """
        pattern = r"^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$"
        if re.match(pattern, self.dictionary["email"]):
            return True
        return False

    def check_weight(self) -> bool:
        """
        Проверяет значение веса на валидность.
            Returns
            -------
                bool:
                    Результат проверки на корректность.
        """
        try:
            weight = float(self.dictionary["weight"])
        except ValueError:
            return False
        return 30 < weight < 250

    def check_inn(self) -> bool:
        """
        Проверяет номер ИНН на валидность.
            Returns
            -------
                bool:
                    Результат проверки на корректность.
        """
        pattern = r"^\d{12}$"
        if re.match(pattern, self.dictionary["inn"]):
            return True
        return False

    def check_passport_series(self) -> bool:
        """
        Проверяет серию паспорта на валидность.
            Returns
            -------
                bool:
                    Результат проверки на корректность.
        """
        pattern = r"^\d{2}\s\d{2}$"
        if re.match(pattern, self.dictionary["passport_series"]):
            return True
        return False

    def check_occupation(self) -> bool:
        """
        Проверяет название профессии на валидность.
            Returns
            -------
                bool:
                    Результат проверки на корректность.
        """
        pattern = r"^([а-яА-Я]|[a-zA-Z]|-| ){3,}$"
        if re.match(pattern, self.dictionary["occupation"]):
            return True
        return False

    def check_work_experience(self) -> bool:
        """
        Проверяет значение рабочего стажа человека на валидность.
            Returns
            -------
                bool:
                    Результат проверки на корректность.
        """
        if isinstance(self.dictionary["work_experience"], int):
            if 0 <= self.dictionary["work_experience"] < 60:
                return True
        return False

    def check_political_views(self) -> bool:
        """
        Проверяет политические убеждения на валидность.
            Returns
            -------
                bool:
                    Результат проверки на корректность.
        """
        pattern = r"^.+(?:ие|ые)$"
        if re.match(pattern, self.dictionary["political_views"]):
            return True
        return False

    def check_worldview(self) -> bool:
        """
        Проверяет взгляд на мир на валидность.
            Returns
            -------
                bool:
                    Результат проверки на корректность.
        """
        pattern = r"^.+(?:изм|анство)$"
        if re.match(pattern, self.dictionary["worldview"]):
            return True
        return False

    def check_address(self) -> bool:
        """
        Проверяет адрес на валидность.
            Returns
            -------
                bool:
                    Результат проверки на корректность.
        """
        pattern = r"(?:ул\.|Аллея) (?:им[\.\s]|)[^\s]+ [^\s]*(?:\s|)\d+"
        if re.match(pattern, self.dictionary["address"]):
            return True
        return False
