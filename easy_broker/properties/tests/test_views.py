from django.http import response
from django.test import TestCase, Client, client
from django.urls import reverse
from properties.views import PropertyDetailView, PropertyListView
import json
import unittest
from unittest.mock import patch


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.properties_url = reverse("properties:properties")

    def test_properties_list_GET(self):
        response = self.client.get(self.properties_url)
        self.assertEquals(response.status_code, 200)

    def test_properties_detail_GET(self):
        property_url = reverse("properties:property", kwargs={"property_id": "1"})
        response = self.client.get(property_url)

        # Bad property id raise 404
        self.assertEquals(response.status_code, 404)
