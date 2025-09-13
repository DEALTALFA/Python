
import logging
import datetime

# Configure logging
logging.basicConfig(
    filename=f'app_{datetime.datetime.now().strftime("%Y%m%d_%H%M%S")}.log',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Create a logger instance
logger = logging.getLogger('app_logger')

def log_info(message):
    """Log info level messages"""
    logger.info(message)

def log_error(message):
    """Log error level messages"""
    logger.error(message)

def log_warning(message):
    """Log warning level messages"""
    logger.warning(message)

def log_debug(message):
    """Log debug level messages"""
    logger.debug(message)

# Example usage
try:
    log_info("Application started")
    # Your application code here
    raise Exception
except Exception as e:
    log_error(f"An error occurred: {str(e)}")
finally:
    log_info("Application ended")