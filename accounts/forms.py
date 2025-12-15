from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Profile
from django.contrib.auth import authenticate

class ProfileRegisterForm(forms.ModelForm):
    password = forms.CharField(
        label="Senha",
        widget=forms.PasswordInput,
    )
    confirm_password = forms.CharField(
        label="Confirme sua senha",
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ["first_name", "username", "email"]
        labels = {
            "first_name": "Nome",
            "username": "Usuário",
            "email": "E-mail",
        }

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise ValidationError("As senhas devem ser iguais.")

        return confirm_password

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("E-mail já cadastrado.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])

        if commit:
            user.save()

            Profile.objects.create(
                user=user,
                updated_at=None
            )

        return user


class LoginForm(forms.Form):
    username = forms.CharField(label="Usuário")
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)

    def clean(self):
        clean_data = super().clean()
        username = clean_data.get("username")
        password = clean_data.get("password")

        if username and password:
            user = authenticate(username=username, password=password)
            if user is None:
                raise ValidationError("Usuário ou senha inválidos.")
            clean_data["user"] = user

        return clean_data
