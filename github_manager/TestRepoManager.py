import unittest
from unittest.mock import patch
from github_manager.repo_manager import RepoManager


class TestRepoManager(unittest.TestCase):
    @patch('github_manager.repo_manager.requests.post')
    def test_create_repository_success(self, mock_post):
        mock_post.return_value.status_code = 201
        mock_post.return_value.json.return_value = {"html_url": "https://github.com/test-repo"}

        repo_manager = RepoManager()
        url = "https://api.github.com/user/repos"
        headers = {"Authorization": "token fake-token"}
        data = {"name": "test-repo", "description": "Test repo", "private": False}

        result = repo_manager.create_repository(url, headers, data)
        self.assertEqual(result, "https://github.com/test-repo")

    @patch('github_manager.repo_manager.requests.post')
    def test_create_repository_failure(self, mock_post):
        mock_post.return_value.status_code = 400

        repo_manager = RepoManager()
        url = "https://api.github.com/user/repos"
        headers = {"Authorization": "token fake-token"}
        data = {"name": "test-repo", "description": "Test repo", "private": False}

        with self.assertRaises(Exception):
            repo_manager.create_repository(url, headers, data)


if __name__ == "__main__":
    unittest.main()
