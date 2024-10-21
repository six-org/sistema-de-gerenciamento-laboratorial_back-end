import re
from datetime import date
from django.core.validators import ValidationError
from dateutil.relativedelta import relativedelta


def maior_de_idade_validator(value):
    "Válida se o usuario é maior de idade"
    idade = relativedelta(date.today(), value)
    if idade.years >= 18:
        return value
    raise ValidationError('É necessário ser maior de idade')


def valid_cpf_validator(value):
    """ válida o CPF do usuário com o cálculo do mesmo """

    cpf = str(value)
    cpf = re.sub(r'[^0-9]', '', cpf)

    if not cpf or len(cpf) != 11:
        raise ValidationError('Digite um cpf valido')

    new_cpf = cpf[:-2]
    reverse = 10
    total = 0

    for index in range(19):
        if index > 8:
            index -= 9

        total += int(new_cpf[index]) * reverse

        reverse -= 1
        if reverse < 2:
            reverse = 11
            digit = 11 - (total % 11)

            if digit > 9:
                digit = 0
            total = 0
            new_cpf += str(digit)

    sequence = new_cpf == str(new_cpf[0]) * len(cpf)

    if cpf == new_cpf and not sequence:
        return cpf

    raise ValidationError("Digite um cpf valido")
