from django.test import TestCase

# Create your tests here.
from .forms import PriceRuleForm

class PriceRuleFormTest(TestCase):

    def test_init_without_entry(self):
        with self.assertRaises(KeyError):
            PriceRuleForm()
