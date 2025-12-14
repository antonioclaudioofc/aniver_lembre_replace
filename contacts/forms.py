from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'birthday', 'relationship', 'notes']
        widgets = {
            'birthday': forms.DateInput(format='%d-%m-%Y', attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={'rows': 4}),
        }

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        birthday = cleaned_data.get('birthday')

        if not name:
            self.add_error('name', 'O nome é obrigatório.')

        if not birthday:
            self.add_error('birthday', 'A data de nascimento é obrigatória.')

        if birthday and birthday > forms.fields.datetime.date.today():
            self.add_error(
                'birthday', 'A data de nascimento não pode ser no futuro.')

        return cleaned_data
