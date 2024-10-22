from django.core.validators import RegexValidator

text_regex_validator = RegexValidator(
    regex=r'^[a-zá-ùA-ZÁ-Ù0-9\s,-]+$',
    message="O texto deve conter apenas letras, espaços, vírgulas, traços('-') e números."
)
