from django.test import TestCase

from eventex.subscriptions.models import Subscription


class SubscriptionDetailGet(TestCase):
    def setUp(self):
        self.obj = Subscription(
            name='Ramiro Batista da Luz',
            cpf='12345678901',
            email='ramiroluz@gmail.com',
            phone='41 9173-2231'
        )
        self.obj.save()
        self.response = self.client.get('/inscricao/{}/'.format(self.obj.pk))

    def test_get(self):
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        self.assertTemplateUsed(self.response,
                                'subscriptions/subscription_detail.html')

    def test_context(self):
        subscription = self.response.context['subscription']
        self.assertIsInstance(subscription, Subscription)

    def test_html(self):
        contents = (self.obj.name, self.obj.cpf, self.obj.email, self.obj.phone)
        with self.subTest():
            for content in contents:
                self.assertContains(self.response, content)


class SubscriptionDetailnotFound(TestCase):
    def test_not_found(self):
        self.response = self.client.get('/inscricao/0/')
        self.assertEqual(404, self.response.status_code)