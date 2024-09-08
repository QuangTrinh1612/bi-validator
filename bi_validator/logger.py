import logging
import os
from datetime import datetime

# Create a log directory if it doesn't exist
LOG_DIR = 'logs'
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Generate a log file with a timestamp
log_file = os.path.join(LOG_DIR, f'bi_validator_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log')

# Configure the logger
logging.basicConfig(
    level=logging.INFO,  # Set log level to INFO (you can change it to DEBUG or ERROR)
    format='%(asctime)s [%(levelname)s] %(message)s',  # Define the log message format
    handlers=[
        logging.FileHandler(log_file),  # Log to the file
        logging.StreamHandler()  # Log to the console
    ]
)

def log_info(message):
    """Logs an informational message."""
    logging.info(message)

def log_warning(message):
    """Logs a warning message."""
    logging.warning(message)

def log_error(message):
    """Logs an error message."""
    logging.error(message)

def log_debug(message):
    """Logs a debug message."""
    logging.debug(message)

def log_critical(message):
    """Logs a critical message."""
    logging.critical(message)