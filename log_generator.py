import random
import time
from datetime import datetime

# Define log levels and sample messages
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
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    level = random.choice(log_levels)
    message = random.choice(log_messages)
    return f"[{timestamp}] {level}: {message}"

def main():
    """Generate and display logs at regular intervals."""
    print("Starting log generator. Press Ctrl+C to stop.")
    try:
        while True:
            log = generate_random_log()
            print(log)
            time.sleep(random.uniform(0.5, 2))  # Random delay between 0.5 and 2 seconds
    except KeyboardInterrupt:
        print("\nLog generator stopped.")

if __name__ == "__main__":
    main()
