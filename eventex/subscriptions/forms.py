from django import forms
from django.core.exceptions import ValidationError

from eventex.subscriptions.models import Subscription
from eventex.subscriptions.validators import validate_cpf


class SubscriptionFormOld(forms.Form):
    name = forms.CharField(label='Nome')
    cpf = forms.CharField(label='CPF', validators=[validate_cpf])
    email = forms.EmailField(label='Email', required=False)
    phone = forms.CharField(label='Telefone', required=False)

    def clean_name(self):
        name = self.cleaned_data['name']
        words = [self.normalize_word(word) for word in name.split()]
        capitalized = ' '.join(words)
        return capitalized

    def clean(self):
        email = self.cleaned_data.get('email')
        phone = self.cleaned_data.get('phone')
        if not email and not phone:
            raise ValidationError('Informe seu e-mail ou telefone.')
        return self.cleaned_data

    def normalize_word(self, word):
        return word.capitalize() if len(word) > 2 else word.lower()


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['name', 'cpf', 'email', 'phone']

    def clean(self):
        self.cleaned_data = super().clean()
        email = self.cleaned_data.get('email')
        phone = self.cleaned_data.get('phone')
        if not email and not phone:
            raise ValidationError('Informe seu e-mail ou telefone.')
        return self.cleaned_data

    def clean_name(self):
        name = self.cleaned_data['name']
        words = [self.normalize_word(word) for word in name.split()]
        capitalized = ' '.join(words)
        return capitalized

    def normalize_word(self, word):
        return word.capitalize() if len(word) > 2 else word.lower()
