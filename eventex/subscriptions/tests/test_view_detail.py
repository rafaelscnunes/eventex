from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):
    def setUp(self) -> None:
        self.obj = Subscription.objects.create(
            name='José das Couves',
            cpf='01234567890',
            email='josedascouves@mailinator.com',
            phone='21 999998888'
        )
        self.resp = self.client.get('/inscricao/{}/'.format(self.obj.pk))

    def test_get(self):
        self.assertEqual(200, self.resp.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.resp, 'subscriptions/subscription_detail.html')

    def test_context(self):
        subscription = self.resp.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        contents = (self.obj.name, self.obj.cpf, self.obj.email, self.obj.phone)
        for expected in contents:
            with self.subTest():
                self.assertContains(self.resp, expected)


class SubscriptionDetailNotFound(TestCase):
    def test_not_found(self):
        resp = self.client.get('/inscricao/0/')
        self.assertEqual(404, resp.status_code)