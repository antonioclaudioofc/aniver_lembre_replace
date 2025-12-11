from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from datetime import date


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, error_messages={
        "unique": "Este usuário já possui um perfil associado.",
        "null": "Usuário obrigatório"
    })

    birthday = models.DateField(error_messages={
        "invalid": "A data inválida",
        "null": "Campo obrigatório",
        "blank": "Campo obrigatório",
    })

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    def clean(self):
        super().clean()

        if self.birthday and self.birthday > date.today():
            raise ValidationError({
                "birthday": "A data de aniversátio não pode estar no futuro."
            })

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"
