class IncorrectCarNumbers(Exception):
    def __init__(self, message, *args):
        self.message = message

class  IncorrectVinNumber(Exception):
    def __init__(self, message, *args):
        self.message = message

class Car:
    def __init__(self, model, vin, numbers):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_numbers(numbers):
            self.__numbers = numbers
    @staticmethod
    def __is_valid_vin(vin_numbers):
        if not isinstance(vin_numbers, int):
            raise IncorrectVinNumber("Некорректный тип vin номер")
        elif not 1000000 <= vin_numbers <= 9999999:
            raise IncorrectCarNumbers ('Неверный диапазон для vin номера')
        return True

    @staticmethod
    def __is_valid_numbers(numbers):
        if len(numbers) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
        elif not isinstance(numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
  print(exc.message)
except IncorrectCarNumbers as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')
