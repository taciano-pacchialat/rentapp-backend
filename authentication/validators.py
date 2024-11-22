# authentication/validators.py
import re
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _

class CustomPasswordValidator:
    def validate(self, password, user=None):
        if len(re.findall(r'\d', password)) < 2:
            raise ValidationError(
                _("The password must contain at least two digits."),
                code='password_no_number',
            )
        if len(re.findall(r'[!@#$%^&*(),.?":{}|<>]', password)) < 2:
            raise ValidationError(
                _("The password must contain at least two special characters."),
                code='password_no_special',
            )

    def get_help_text(self):
        return _(
            "Your password must contain at least two digits and two special characters."
        )