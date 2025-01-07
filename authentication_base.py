# github_manager/authentication_base.py

from abc import ABC, abstractmethod


class AuthenticationBase(ABC):
    """
    Abstract base class for authentication.
    Defines methods to handle authentication for API requests.
    """

    @abstractmethod
    def get_headers(self) -> dict:
        """
        Abstract method to return authentication headers.
        :return: Dictionary containing authentication headers.
        """
        pass
