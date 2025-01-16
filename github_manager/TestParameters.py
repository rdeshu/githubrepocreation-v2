import unittest
from parameters.params_impl import Parameters


class TestParameters(unittest.TestCase):
    def setUp(self):
        self.params = Parameters()

    def test_set_and_get_params(self):
        self.params.set_params(
            github_token="fake-token",
            repo_name="test-repo",
            repo_description="Test repo",
            organization_name="test-org"
        )
        self.assertEqual(self.params.get_param("github_token"), "fake-token")
        self.assertEqual(self.params.get_param("repo_name"), "test-repo")

    def test_get_param_missing(self):
        with self.assertRaises(ValueError):
            self.params.get_param("nonexistent_param")


if __name__ == "__main__":
    unittest.main()
