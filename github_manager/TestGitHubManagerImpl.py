import unittest
from unittest.mock import Mock, patch
from github_manager.github_manager_impl import GitHubManagerImpl
from github_manager.repo_manager import RepoManager
from github_manager.authentication import Authentication
from parameters.params_impl import Parameters


class TestGitHubManagerImpl(unittest.TestCase):
    def setUp(self):
        # Mock parameters
        self.parameters = Mock()
        self.parameters.get_param.side_effect = lambda key: {
            "repo_name": "test-repo",
            "repo_description": "Test description",
            "organization_name": "test-org",
            "github_token": "fake-token",
        }.get(key)

        # Mock RepoManager
        self.repo_manager = Mock()
        self.repo_manager.create_repository.return_value = "https://github.com/test-org/test-repo"

        # Mock Authentication
        self.auth = Mock()
        self.auth.get_headers.return_value = {"Authorization": "token fake-token"}

        # Patch RepoManager and Authentication in GitHubManagerImpl
        with patch('github_manager.github_manager_impl.RepoManager', return_value=self.repo_manager), \
             patch('github_manager.github_manager_impl.Authentication', return_value=self.auth):
            self.github_manager = GitHubManagerImpl(self.parameters)

    def test_create_repository(self):
        result = self.github_manager.create_repository()
        self.assertEqual(result, "https://github.com/test-org/test-repo")

    def test_run_success(self):
        with patch('builtins.print') as mock_print:
            self.github_manager.run()
            mock_print.assert_called_with("Repository created successfully: https://github.com/test-org/test-repo")

    def test_run_failure(self):
        self.repo_manager.create_repository.side_effect = Exception("API error")
        with patch('builtins.print') as mock_print:
            self.github_manager.run()
            mock_print.assert_called_with("Error: API error")


if __name__ == "__main__":
    unittest.main()
