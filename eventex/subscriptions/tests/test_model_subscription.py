from datetime import datetime
from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionModelTest(TestCase):
    def setUp(self) -> None:
        self.obj = Subscription(
            name='José das Couves',
            cpf='01234567890',
            email='josedascouves@mailinator.com',
            phone='21 999998888')
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscriotion must have an auto created_at attr"""
        self.assertIsInstance(self.obj.created_at, datetime)

    def test_str(self):
        self.assertEqual('José das Couves', str(self.obj))