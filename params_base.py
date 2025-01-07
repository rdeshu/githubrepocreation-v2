# parameters/params_base.py

from abc import ABC, abstractmethod


class ParametersBase(ABC):
    """
    Abstract base class for parameters.
    Defines methods to set and get parameter values.
    """

    @abstractmethod
    def set_params(self, **kwargs):
        """
        Abstract method to set parameters dynamically.
        :param kwargs: Dictionary of parameter values.
        """
        pass

    @abstractmethod
    def get_param(self, key: str):
        """
        Abstract method to get a parameter by key.
        :param key: Name of the parameter.
        :return: Value of the parameter.
        """
        pass
