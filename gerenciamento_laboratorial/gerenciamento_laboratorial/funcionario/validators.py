from django.core.validators import RegexValidator

cargo_regex_validator = RegexValidator(
    regex=r'^[a-zá-ùA-ZÁ-Ù\s]+$',
    message="O texto deve conter apenas letras"
)
