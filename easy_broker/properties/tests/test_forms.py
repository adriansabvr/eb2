from django.test import SimpleTestCase
from properties.forms import ContactForm


class TestForms(SimpleTestCase):
    def test_contact_form(self):
        form = ContactForm(
            data={
                "name": "test_name",
                "phone": "5501020304",
                "email": "test@test.com",
                "message": "Testing message",
            }
        )

        self.assertTrue(form.is_valid())

    def test_contact_form_no_data(self):
        form = ContactForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 4)
