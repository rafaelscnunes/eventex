from django.core import mail
from django.test import TestCase
from django.shortcuts import resolve_url as r


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='José das Couves',
                    cpf='01234567890',
                    email='josedascouves@mailinator.com',
                    phone='21 999998888')
        self.client.post(r('subscriptions:new'), data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato_eventex@mailinator.com'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato_eventex@mailinator.com', 'josedascouves@mailinator.com']
        self.assertEqual(expect, self.email.to)

    def test_subscrition_email_body(self):
        contents = ['José Das Couves',
                   '01234567890',
                   'josedascouves@mailinator.com',
                   '21 999998888']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
