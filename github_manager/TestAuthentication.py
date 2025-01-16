import unittest
from github_manager.authentication import Authentication
from unittest.mock import Mock


class TestAuthentication(unittest.TestCase):
    def test_get_headers(self):
        parameters = Mock()
        parameters.get_param.return_value = "fake-token"

        auth = Authentication(parameters)
        headers = auth.get_headers()
        self.assertEqual(headers, {
            "Authorization": "token fake-token",
            "Accept": "application/vnd.github.v3+json"
        })


if __name__ == "__main__":
    unittest.main()
