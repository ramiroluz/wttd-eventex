from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscribeGet(TestCase):
    def test_form_has_fields(self):
        '''Form must have 4 fields'''
        form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(
            expected, list(form.fields)
        )

    def test_cpf_is_digit(self):
        '''CPF must only accept digits'''
        form = self.make_validation_form(cpf='ABCD5678901')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        '''CPF must have 11 digits.'''
        form = self.make_validation_form(cpf='1234')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def assertFormErrorCode(self, form, field, error_code):
        errors = form.errors.as_data()
        error_list = errors[field]
        exception = error_list[0]
        self.assertEqual(error_code, exception.code)

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors.as_data()
        error_list = errors[field]
        self.assertEqual([msg], error_list)

    def make_validation_form(self, **kwargs):
        valid = dict(name='Ramiro Batista da Luz', cpf='12345678901',
                    email='ramiroluz@gmail.com', phone='41 9173-2231')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form