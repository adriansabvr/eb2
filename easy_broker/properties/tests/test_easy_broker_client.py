import unittest
import json
from unittest.mock import patch
from properties.easy_broker import EasyBrokerClient, EasyBrokerClientError, Status


class TestEasyBrokerClient(unittest.TestCase):
    def setUp(self) -> None:
        test_api_key = "testapikey"
        self.eb_client = EasyBrokerClient(test_api_key)

    def tearDown(self) -> None:
        pass

    def test_properties_url(self) -> None:
        url = "https://api.stagingeb.com/v1/properties"
        self.assertEqual(self.eb_client.properties_url, url)

    def test_get_properties(self) -> None:
        with patch("properties.easy_broker.requests.get") as mocked_get:
            mocked_get.return_value.status_code = 200

            # Mock json response
            mocked_json_response = {
                "pagination": {"page": 1, "limit": 20},
                "content": [{"title": "Local 1"}, {"title": "Local 2"}, {"title": "Casa 3"}],
            }

            mocked_get.return_value.text = json.dumps(mocked_json_response, indent=4)
            json_response = self.eb_client.get_properties(1, 20, {}, [])

            self.assertEqual(json_response, mocked_json_response)

        # Test Failed Connection
        api_url = self.eb_client.api_url
        self.eb_client.api_url = "www.testapi.com/v1/"

        expectedError = EasyBrokerClientError("11001", "Failed to stablish connection")
        error = self.eb_client.get_properties(1, 20, {}, [])
        self.assertEqual(error, expectedError)

        self.eb_client.api_url = api_url


if __name__ == "__main__":
    unittest.main()
