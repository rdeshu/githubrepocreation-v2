# github_manager/github_manager.py

from abc import ABC, abstractmethod


class GitHubManager(ABC):
    """
    Abstract base class for GitHub manager.
    """

    @abstractmethod
    def create_repository(self) -> str:
        """
        Abstract method for creating a GitHub repository.
        """
        pass

    @abstractmethod
    def run(self):
        """
        Abstract method for orchestrating the workflow.
        """
        pass
