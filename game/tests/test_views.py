import unittest

from django.test import TestCase
from django.urls import reverse


class TemplateTest(TestCase):

    def test_response(self):
        """
        Test page response
        :return:
        """
        response = self.client.get(reverse('game:index'))
        self.assertTemplateUsed(response, 'game/home.html')


if __name__ == '__main__':
    unittest.main(verbosity=2)
