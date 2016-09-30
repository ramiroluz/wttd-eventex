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
        form = self.make_validated_form(cpf='ABCD5678901')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        '''CPF must have 11 digits.'''
        form = self.make_validated_form(cpf='1234')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def test_name_must_be_capitalized(self):
        '''Name must be capitalized'''
        form = self.make_validated_form(name='RAMIRO batista da luz')
        self.assertEqual('Ramiro Batista da Luz', form.cleaned_data['name'])

    def test_email_is_optional(self):
        '''Email is optional.'''
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_phone_is_optional(self):
        '''Phone is optional.'''
        form = self.make_validated_form(phone='')
        self.assertFalse(form.errors)

    def test_must_inform_email_or_phone(self):
        '''Email and Phone are optional but one must be informed.'''
        form = self.make_validated_form(email='', phone='')
        self.assertListEqual(['__all__'], list(form.errors))

    def test_invalid_email_without_phone(self):
        '''Invalid email without phone must have two errors.'''
        form = self.make_validated_form(email='asdf', phone='')
        error_list = sorted(['email', '__all__'])
        form_errors = sorted(list(form.errors))
        self.assertListEqual(error_list, form_errors)

    def assertFormErrorCode(self, form, field, error_code):
        errors = form.errors.as_data()
        error_list = errors[field]
        exception = error_list[0]
        self.assertEqual(error_code, exception.code)

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors.as_data()
        error_list = errors[field]
        self.assertEqual([msg], error_list)

    def make_validated_form(self, **kwargs):
        valid = dict(name='Ramiro Batista da Luz', cpf='12345678901',
                    email='ramiroluz@gmail.com', phone='41 9173-2231')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form