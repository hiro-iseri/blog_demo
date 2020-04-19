from unittest import TestCase
from demo.demo import Demo

class TestDemo(TestCase):

    def test_add(self):
        self.assertEqual(Demo().add(1, 3), 4)