from django.core import mail
from django.test import TestCase


class SubscribePostValid(TestCase):
    def setUp(self) -> None:
        data = dict(name='Rafael Nunes', cpf='12345678901', email='rafaelscnunes@gmail.com', phone='21981246171')
        self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'
        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'contato_eventex@mailinator.com'
        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['contato_eventex@mailinator.com', 'rafaelscnunes@gmail.com']
        self.assertEqual(expect, self.email.to)

    def test_subscrition_email_body(self):
        contents = ['Rafael Nunes',
                   '12345678901',
                   'rafaelscnunes@gmail.com',
                   '21981246171']
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
