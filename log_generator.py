import random
import time
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s: %(message)s")

log_levels = ["INFO", "WARNING", "ERROR"]
log_messages = [
    "User logged in successfully",
    "File not found",
    "System running smoothly",
    "Disk space running low",
    "Network connection lost",
    "Database query failed",
    "Application started",
    "Unexpected input received",
    "Service restarted",
    "Configuration updated",
]

def generate_random_log():
    """Generate a random log entry."""
    level = random.choice(log_levels)
    message = random.choice(log_messages)
    logger = getattr(logging, level.lower())
    logger(message)

def main():
    """Generate logs at regular intervals."""
    logging.info("Starting log generator. Press Ctrl+C to stop.")
    try:
        while True:
            generate_random_log()
            time.sleep(random.uniform(0.5, 2))  # Random delay between logs
    except KeyboardInterrupt:
        logging.info("Log generator stopped.")

if __name__ == "__main__":
    main()

