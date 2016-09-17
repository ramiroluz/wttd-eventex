from datetime import datetime

from django.test import TestCase
from eventex.subscriptions.models import Subscription


class SubscriptionTest(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Ramiro Batista da Luz',
            cpf='12345678901',
            email='ramiroluz@gmail.com',
            phone='41 9173-2231'
        )
        self.obj.save()

    def test_create(self):
        self.assertTrue(Subscription.objects.exists())

    def test_created_at(self):
        """Subscritpion must have a created_at attribute."""
        self.assertIsInstance(self.obj.created_at, datetime)