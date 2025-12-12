from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Profile


class ProfileRegisterForm(forms.ModelForm):
    password = forms.CharField(
        label="Insira sua senha",
        widget=forms.PasswordInput,
    )
    confirm_password = forms.CharField(
        label="Insira novamente sua senha",
        widget=forms.PasswordInput
    )
    birthday = forms.DateField(
        label="Insira sua data de nascimento",
        widget=forms.DateInput(attrs={"type": "date"})
    )

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]

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
                birthday=self.cleaned_data["birthday"]
            )

        return user
