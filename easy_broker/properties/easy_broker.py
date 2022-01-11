import requests
import json
from typing import Dict, Any, List
from dataclasses import dataclass
from enum import Enum


@dataclass
class EasyBrokerClientError:
    error_code: str
    error_msg: str


class Status(Enum):
    ALL = "all"
    PUBLISHED = "published"
    NOT_PUBLISHED = "not_published"
    RESERVED = "reserved"
    SOLD = "sold"
    RENTED = "rented"
    SUSPENDED = "suspended"


class EasyBrokerClient:
    """
    Client to consume Easy Broker API
    """

    api_url: str = "https://api.stagingeb.com/v1/"
    api_key: str

    def __init__(self, api_key: str) -> None:
        """Inits EasyBrokerClient Class"""
        self.api_key = api_key

    def post_contact_request(self, payload: Dict[str, Any]) -> Any | EasyBrokerClientError:
        headers: Dict[str, Any] = {"X-Authorization": self.api_key}
        return self.post(self.contact_request_url, headers, payload)

    def get_properties(
        self, page: int, limit: int, filters: Dict[str, str], statuses: List[Status]
    ) -> Any | EasyBrokerClientError:
        """EasyBroker API method to check the list of your properties"""

        args: Dict[str, Any] = {
            "page": page,
            "limit": limit,
            "search": filters,
            "search[statuses]": [status.value for status in statuses],
        }
        headers: Dict[str, Any] = {"X-Authorization": self.api_key}

        return self.get(self.properties_url, headers, args)

    def get_property(self, property_id: str) -> Any | EasyBrokerClientError:
        """EasyBroker API method to detail a property by id"""

        args: Dict[str, Any] = {"property_id": property_id}
        headers: Dict[str, Any] = {"X-Authorization": self.api_key}

        return self.get(f"{self.properties_url}/{property_id}", headers, args)

    def get(self, url: str, headers: Dict[str, Any], args: Dict[str, Any]) -> Any | EasyBrokerClientError:
        try:
            response = requests.get(url, headers=headers, params=args)
        except:
            return EasyBrokerClientError("11001", "Failed to stablish connection")

        if response.status_code == 200:
            response_json = json.loads(response.text)
            return response_json

        return EasyBrokerClientError(response.status_code, response.text)

    def post(self, url: str, headers: Dict[str, Any], payload: Dict[str, Any]) -> Any | EasyBrokerClientError:
        try:
            response = requests.post(url, headers=headers, json=payload)
        except:
            return EasyBrokerClientError("11001", "Failed to stablish connection")

        if response.status_code == 200:
            response_json = json.loads(response.text)
            return response_json

        return EasyBrokerClientError(response.status_code, response.text)

    @property
    def properties_url(self) -> str:
        return f"{self.api_url}properties"

    @property
    def contact_request_url(self) -> str:
        return f"{self.api_url}contact_requests"
