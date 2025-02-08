class Money:
    def __init__(self, dollars, cents):
        self.total_cents = dollars * 100 + cents  # Сохраняем общее количество центов

    @property
    def dollars(self):
        return self.total_cents // 100  # Возвращаем количество долларов

    @dollars.setter
    def dollars(self, value):
        if isinstance(value, int) and value >= 0:  # Проверяем, что значение корректно
            self.total_cents = value * 100 + self.cents  # Обновляем total_cents, сохраняя центы
        else:
            print("Error dollars")  # Выводим сообщение об ошибке

    @property
    def cents(self):
        return self.total_cents % 100  # Возвращаем количество центов

    @cents.setter
    def cents(self, value):
        if isinstance(value, int) and 0 <= value < 100:  # Проверяем, что значение корректно
            self.total_cents = self.dollars * 100 + value  # Обновляем total_cents, сохраняя доллары
        else:
            print("Error cents")  # Выводим сообщение об ошибке

    def __str__(self):
        return f"Ваше состояние составляет {self.dollars} долларов {self.cents} центов"


bill = Money(101, 99)
assert isinstance(bill, Money)

print(bill)  # Ваше состояние составляет 101 долларов 99 центов
print(bill.dollars, bill.cents)  # 101 99
bill.dollars = 666
print(bill)  # Ваше состояние составляет 666 долларов 99 центов
bill.cents = 12
print(bill)  # Ваше состояние составляет 666 долларов 12 центов
assert bill.total_cents == 66612
assert list(bill.__dict__.keys()) == ['total_cents']