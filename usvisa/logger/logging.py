import logging
import os
from datetime import datetime

# Generate the log file name with the current timestamp
LOG_PATH: str = f"{datetime.now().strftime('%d_%m_%Y_%H_%M_%S')}.log"

# Define the log directory
FILE_PATH = os.path.join(os.getcwd(), "logs")

# Create the directory if it doesn't exist
os.makedirs(FILE_PATH, exist_ok=True)

# Join the file path with the directory
LOG_FILE_PATH = os.path.join(FILE_PATH, LOG_PATH)

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    level=logging.DEBUG,  # You can set the level to logging.DEBUG for more detailed logs
    format="%(asctime)s - %(levelname)s - %(message)s - %(module)s - Line: %(lineno)d",
)

