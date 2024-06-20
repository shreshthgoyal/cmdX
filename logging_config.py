import logging

def setup_logging():
    """
    Sets up logging configuration.
    
    This function configures the logging to output logs to both a file (app.log)
    and the console (stream). It sets the log level to INFO and defines the format
    for the log messages to include the timestamp, log level, and message.
    """
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s %(message)s',
        handlers=[
            logging.FileHandler("app.log"),
            logging.StreamHandler()
        ]
    )

setup_logging()
