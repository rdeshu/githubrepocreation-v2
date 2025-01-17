# github_manager/authentication.py
from authentication_base import AuthenticationBase
class Authentication(AuthenticationBase):
    @staticmethod
    def get_headers(parameters):
        """
        Returns the headers required for GitHub API authentication.
        :param parameters: Instance of the Parameters class.
        :return: Dictionary containing authentication headers.
        """
        token = parameters.get_param("github_token")
        return {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }
