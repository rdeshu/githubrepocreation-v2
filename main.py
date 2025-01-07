from githubparams_impl import Parameters
from github_manager.github_manager_impl import GitHubManagerImpl

# Step 1: Collect user input
user_input = {
    "github_token": input("Enter your GitHub token: "),
    "repo_name": input("Enter the repository name: "),
    "repo_description": input("Enter the repository description: "),
    "organization_name": input("Enter the organization name (leave blank for personal account): "),
}

# Step 2: Initialize parameters and set values
parameters = Parameters()
parameters.set_params(**user_input)

# Step 3: Create an instance of GitHubManagerImpl
github_manager = GitHubManagerImpl(parameters)

# Step 4: Run the main workflow
github_manager.run()
