from django import forms
from .models import MedicationRecord

class MedicationForm(forms.ModelForm):
    class Meta:
        model = MedicationRecord
        fields = ['dose']
        widgets = {
            'dose': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'دوز مصرفی (میلی‌گرم)'}),
        }
