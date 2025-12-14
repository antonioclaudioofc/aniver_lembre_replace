from django import forms
from .models import Remiders


class ReminderForm(forms.ModelForm):
    class Meta:
        model = Remiders
        fields = [
            'contact',
            'days_before',
            'notifiy_at',
            'active',
        ]
        widgets = {
            'notifiy_at': forms.TimeInput(format='%H:%M', attrs={'type': 'time'}),
        }
