import os
import logging.config

class LoggerManager:
    _instance = None

    def __new__(cls, config_file=None):
        if cls._instance is None:
            cls._instance = super(LoggerManager, cls).__new__(cls)
            cls._instance._initialize_logger(config_file)
        return cls._instance

    def _initialize_logger(self, config_file):
        # Default path to 'log/logging.conf' in the project directory
        if config_file is None:
            base_dir = os.path.dirname(os.path.abspath(__file__))  # Get the current script's directory
            config_file = os.path.join(base_dir, "logging.conf")  # Assumes logging.conf is inside log/

        config_path = os.path.abspath(config_file)

        # Check if the file exists, raise error if not found
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Logging configuration file not found: {config_path}")

        print(f"Loading logging config from: {config_path}")  # Debugging print statement
        logging.config.fileConfig(config_path)

    def get_logger(self):
        return logging.getLogger("root")  # Ensure "root" matches [logger_root] in logging.conf
