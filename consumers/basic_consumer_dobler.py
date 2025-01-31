"""
basic_consumer_dobler.py

Read a log file as it is being written with enhanced features.
"""

#####################################
# Import Modules
#####################################

# Import packages from Python Standard Library
import os
import time

# Import functions from local modules
from utils.utils_logger import logger, get_log_file_path

#####################################
# Define a function to process a single message
#####################################

def process_message(log_file) -> None:
    """
    Read a log file and process each message.

    Args:
        log_file (str): The path to the log file to read.
    """
    ALERT_PATTERNS = ["error", "failed", "ALERT:", "I just loved a movie! It was funny."]
    delay_seconds = 1  # Initial sleep duration
    
    while True:
        try:
            with open(log_file, "r") as file:
                file.seek(0, os.SEEK_END)  # Move to the end of the file
                print("Consumer is ready and waiting for a new log message...")

                while True:
                    line = file.readline()
                    
                    if not line:
                        time.sleep(delay_seconds)
                        delay_seconds = min(delay_seconds * 2, 5)  # Adaptive backoff up to 5 sec
                        if os.stat(log_file).st_size < file.tell():  # Detect file rotation
                            print("Log file rotated. Reopening...")
                            break  # Exit inner loop to reopen file
                        continue

                    delay_seconds = 1  # Reset delay on new message
                    message = line.strip()
                    print(f"Consumed log message: {message}")

                    if any(pattern in message for pattern in ALERT_PATTERNS):
                        print(f"ALERT: {message}")
                        logger.warning(f"ALERT: {message}")
        
        except FileNotFoundError:
            print("Log file not found. Waiting...")
            time.sleep(2)
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            time.sleep(2)

#####################################
# Define main function for this script.
#####################################

def main() -> None:
    """Main entry point."""

    logger.info("START...")
    log_file_path = get_log_file_path()
    logger.info(f"Reading file located at {log_file_path}.")

    try:
        process_message(log_file_path)
    except KeyboardInterrupt:
        print("User stopped the process.")
    
    logger.info("END.....")

#####################################
# Conditional Execution
#####################################

if __name__ == "__main__":
    main()
