# github_manager/repo_manager.py

import requests
from authentication import Authentication


class RepoManager:
    def __init__(self, parameters):
        self.parameters = parameters

    def create_repository(self) -> str:
        """
        Creates a new GitHub repository using the provided parameters.
        :return: URL of the created repository.
        """
        repo_name = self.parameters.get_param("repo_name")
        repo_description = self.parameters.get_param("repo_description")
        organization_name = self.parameters.get_param("organization_name")
        api_url = "https://api.github.com"

        if not repo_name:
            raise ValueError("Repository name is required.")

        # Determine the API endpoint based on the organization name
        if organization_name:
            url = f"{api_url}/orgs/{organization_name}/repos"
        else:
            url = f"{api_url}/user/repos"

        headers = Authentication.get_headers(self.parameters)
        data = {
            "name": repo_name,
            "description": repo_description,
            "private": False,
        }

        response = requests.post(url, json=data, headers=headers)
        if response.status_code == 201:
            return response.json()['html_url']
        else:
            raise Exception(f"Failed to create repository: {response.status_code}, {response.text}")
