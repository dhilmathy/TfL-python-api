import requests
import urllib.parse
from .config import base_url

class RestClient():
    """RestClient.

    :param ApiToken api_token: API token to access TfL unified API
    """

    def __init__(self, api_token):
        self.api_token = { "app_id": api_token.app_id, "app_key": api_token.app_key }

    def send_request(self, location, params=None):
        return requests.get(base_url + location + "?" + self._get_query_strings(params))

    def _get_query_strings(self, params):
        if params is None:
            params = {}
        if self.api_token is not None:
            params.update(self.api_token)
        return urllib.parse.urlencode(params)