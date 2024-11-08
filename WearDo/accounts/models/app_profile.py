from django.contrib.auth import get_user_model
from django.core.validators import RegexValidator
from django.db import models

UserModel = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    first_name = models.CharField(
        max_length=30
    )

    last_name = models.CharField(
        max_length=30
    )

    phone_number = models.CharField(
        max_length=13,  # Adjusted to fit +359XXXXXXXXX or 0XXXXXXXXX
        validators=[RegexValidator(
            regex=r'^(\+359|0)(87|88|89)\d{7}$',
            message="Phone number must be in the format +359XXXXXXXXX or 0XXXXXXXXX."
        )],
    )

    date_of_birth = models.DateField()