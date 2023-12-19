from django import forms
from .models import FormObratZvonot


# форма обратной связи на странице контакты
class FormObratZvonok(forms.ModelForm):
    class Meta:
        model = FormObratZvonot
        fields = [
            'name',
            'body'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'form-control rows=5'}),
            'body': forms.Textarea(attrs={'placeholder': 'Сообщение', 'class': 'form-control'}),
        }