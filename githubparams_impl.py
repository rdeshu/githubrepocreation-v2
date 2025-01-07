# parameters/params_impl.py

from params_base import ParametersBase


class Parameters(ParametersBase):
    """
    Concrete implementation of ParametersBase.
    Stores parameters in a dictionary for dynamic usage.
    """

    def __init__(self):
        # Predefined parameter keys
        self._params = {
            "github_token": None,
            "repo_name": None,
            "repo_description": None,
            "organization_name": None,
        }

    def set_params(self, **kwargs):
        """
        Sets parameters dynamically from user input.
        :param kwargs: Dictionary of parameter values.
        """
        for key, value in kwargs.items():
            if key in self._params:
                self._params[key] = value
            else:
                raise KeyError(f"Invalid parameter: {key}")

    def get_param(self, key: str):
        """
        Retrieves the value of a parameter by key.
        :param key: Name of the parameter.
        :return: Value of the parameter.
        """
        value = self._params.get(key)
        if value is None:
            raise ValueError(f"Parameter '{key}' is not set.")
        return value
