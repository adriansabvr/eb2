from django.test import SimpleTestCase
from django.urls import reverse, resolve
from properties.views import PropertyDetailView, PropertyListView


class TestUrls(SimpleTestCase):
    def test_properties_url_resolves(self):
        url = reverse("properties:properties")
        self.assertEquals(resolve(url).func, PropertyListView)

    def test_property_url_resolves(self):
        url = reverse("properties:property", kwargs={"property_id": 123})
        self.assertEquals(resolve(url).func, PropertyDetailView)
