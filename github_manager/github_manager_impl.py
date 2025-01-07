# github_manager/github_manager_impl.py

from github_manager.github_manager import GitHubManager
from github_manager.repo_manager import RepoManager


class GitHubManagerImpl(GitHubManager):
    def __init__(self, parameters):
        self.parameters = parameters
        self.repo_manager = RepoManager(self.parameters)

    def create_repository(self) -> str:
        """
        Implements the abstract method to create a GitHub repository.
        Calls the RepoManager to perform the creation.

        :return: URL of the created repository.
        """
        return self.repo_manager.create_repository()

    def run(self):
        """
        Implements the abstract method to handle the main workflow.
        """
        try:
            # Create repository
            repo_url = self.create_repository()
            print(f"Repository created successfully: {repo_url}")
        except Exception as e:
            print(f"Error: {e}")
