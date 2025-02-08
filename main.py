class Money:
    def __init__(self, dollars, cents):
        """
        Конструктор класса Money.
        Принимает два аргумента: dollars (доллары) и cents (центы).
        Сохраняет общее количество центов в атрибуте total_cents.
        """
        self.total_cents = dollars * 100 + cents  # Преобразуем доллары и центы в общее количество центов

    @property
    def dollars(self):
        """
        Свойство-геттер для получения количества долларов.
        Возвращает количество долларов, вычисляя его из общего количества центов.
        """
        return self.total_cents // 100  # Делим total_cents на 100, чтобы получить доллары

    @dollars.setter
    def dollars(self, value):
        """
        Свойство-сеттер для установки количества долларов.
        Принимает целое неотрицательное число.
        Обновляет total_cents, сохраняя текущее количество центов.
        Если значение некорректно, выводит сообщение "Error dollars".
        """
        if isinstance(value, int) and value >= 0:
            # Обновляем total_cents, сохраняя текущие центы
            self.total_cents = value * 100 + (self.total_cents % 100)
        else:
            print('Error dollars')  # Сообщение об ошибке, если значение некорректно

    @property
    def cents(self):
        """
        Свойство-геттер для получения количества центов.
        Возвращает количество центов, вычисляя его из общего количества центов.
        """
        return self.total_cents % 100  # Остаток от деления total_cents на 100 — это центы

    @cents.setter
    def cents(self, value):
        """
        Свойство-сеттер для установки количества центов.
        Принимает целое неотрицательное число меньше 100.
        Обновляет total_cents, сохраняя текущее количество долларов.
        Если значение некорректно, выводит сообщение "Error cents".
        """
        if isinstance(value, int) and 0 <= value < 100:
            # Обновляем total_cents, сохраняя текущие доллары
            self.total_cents = (self.total_cents // 100) * 100 + value
        else:
            print('Error cents')  # Сообщение об ошибке, если значение некорректно

    def __str__(self):
        """
        Метод для строкового представления объекта.
        Возвращает строку в формате: "Ваше состояние составляет {dollars} долларов {cents} центов".
        Использует свойства dollars и cents для получения текущих значений.
        """
        return f'Ваше состояние составляет {self.dollars} долларов {self.cents} центов'


bill = Money(101, 99)
print(bill.__doc__)


# assert isinstance(bill, Money)
#
# print(bill)  # Ваше состояние составляет 101 долларов 99 центов
# print(bill.dollars, bill.cents)  # 101 99
# bill.dollars = 666
# print(bill)  # Ваше состояние составляет 666 долларов 99 центов
# bill.cents = 12
# print(bill)  # Ваше состояние составляет 666 долларов 12 центов
# assert bill.total_cents == 66612
# assert list(bill.__dict__.keys()) == ['total_cents']
