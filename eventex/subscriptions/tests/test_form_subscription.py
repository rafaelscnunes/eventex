from django.test import TestCase
from eventex.subscriptions.forms import SubscriptionForm


class SubscriptionFormTest(TestCase):
    def make_validated_form(self, **kwargs):
        valid = dict(name='Jose Das Couves', cpf='01234567890',
                     email='josedascouves@mailinatro.com', phone='21 999998888')
        data = dict(valid, **kwargs)
        form = SubscriptionForm(data)
        form.is_valid()
        return form

    def assertFormErrorMessage(self, form, field, msg):
        errors = form.errors
        errors_list = errors[field]
        self.assertListEqual([msg], errors_list)

    def assertFormErrorCode(self, form, field, code):
        errors = form.errors.as_data()
        errors_list = errors[field]
        exception = errors_list[0]
        self.assertEqual(code, exception.code)

    def test_form_has_fields(self):
        """Form must have 4 fields."""
        form = SubscriptionForm()
        expected = ['name', 'cpf', 'email', 'phone']
        self.assertSequenceEqual(expected, list(form.fields))

    def test_cpf_is_digit(self):
        """CPF must accept only digits"""
        form = self.make_validated_form(cpf='ABCD4567890')
        self.assertFormErrorCode(form, 'cpf', 'digits')

    def test_cpf_has_11_digits(self):
        """CPF must have 11 digits"""
        form = self.make_validated_form(cpf='0123')
        self.assertFormErrorCode(form, 'cpf', 'length')

    def test_name_must_be_capitalized(self):
        """Name must be capitalized"""
        # JOSÉ das Couves -> José Das Couves
        form = self.make_validated_form(name='JOSÉ das Couves')
        self.assertEqual('José Das Couves', form.cleaned_data['name'])

    def test_email_is_optional(self):
        """Email is optional"""
        form = self.make_validated_form(email='')
        self.assertFalse(form.errors)

    def test_phone_is_optional(self):
        """Phone is optional"""
        form = self.make_validated_form(phone='')
        self.assertFalse(form.errors)

    def test_must_inform_email_or_phone(self):
        """Email and Phone are optional, but one must be informed"""
        form = self.make_validated_form(email='', phone='')
        self.assertListEqual(['__all__'], list(form.errors))
