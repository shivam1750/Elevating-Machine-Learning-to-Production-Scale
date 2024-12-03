import logging
import os
from from_root import from_root
from datetime import datetime

# Function to initialize logging
def init_logging(log_dir='logs'):
    """
    Initialize logging with a specific directory and filename based on the current timestamp.
    """
    # Get current timestamp for log file naming
    log_filename = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
    # Construct the full log path
    log_path = os.path.join(from_root(), log_dir, log_filename)
    
    # Create log directory if it does not exist
    try:
        os.makedirs(log_dir, exist_ok=True)
    except OSError as e:
        print(f"Error creating log directory {log_dir}: {e}")
        return None

    # Configure logging
    logging.basicConfig(
        filename=log_path,
        format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
        level=logging.DEBUG,
    )
    return log_path

# Initialize logging and get the log path
log_path = init_logging()

# Log an info message to indicate logging has started
if log_path:
    logging.info(f"Logging initialized, writing to {log_path}")
else:
    print("Logging could not be initialized.")
