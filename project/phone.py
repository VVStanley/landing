from django.db import models
from django.core.validators import RegexValidator


class PhoneField(models.CharField):

    default_validators = [
        RegexValidator(
            regex=r'8\d{10}',
            message='Введите корректный номер телефона',
        )
    ]
    description = 'Номер телефона'

    def __init__(self, *args, **kwargs):
        kwargs.setdefault('max_length', 20)
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        del kwargs["max_length"]
        return name, path, args, kwargs


def replace_phone(phone_number):
    phone_number = str(phone_number)
    return phone_number.replace('+7', '8').replace('(', '').replace(')', '').replace(' ', '').replace('-', '')
