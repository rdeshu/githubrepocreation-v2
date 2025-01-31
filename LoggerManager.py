import os
import logging.config

class LoggerManager:
    _instance = None

    @classmethod
    def get_logger(cls, config_file="log/logging.conf"):
        if cls._instance is None:
            cls._initialize_logger(config_file)
        return logging.getLogger("root")

    @classmethod
    def _initialize_logger(cls, config_file):
        config_path = os.path.abspath(config_file)
        
        if not os.path.exists(config_path):
            raise FileNotFoundError(f"Logging configuration file not found: {config_path}")

        logging.config.fileConfig(config_path)
        cls._instance = True  # Mark that initialization is done
