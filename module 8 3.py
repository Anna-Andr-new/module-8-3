class IncorrectVinNumber(Exception):
    def _init__ (self,message):
        self.message = message

class IncorrectCarNumbers(Exception):
    def __init__(self, message):
        self.message = message

class Car:
    def __init__(self, model, _vin, _numbers):
        self.model = model
        self._vin = _vin
        self._numbers = _numbers


    def __is_valid_vin(_vin):#принимает _vin и проверяет его на корректность.
        if not isinstance(_vin, int):
            raise IncorrectVinNumber('Некорректный тип vin номера')
        if not (1000000 <= _vin <= 9999999):
            raise IncorrectVinNumber('Неверный диапазон для vin номера')
        return True

    def __is_valid_numbers (_numbers):
        if not isinstance(_numbers, str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
        if len(_numbers) != 6:
            raise IncorrectCarNumbers ('Неверная длина номера')
        return True


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