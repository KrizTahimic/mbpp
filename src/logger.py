import logging
import os
from datetime import datetime

def setup_logging(log_dir="logs", debug=False, module_name=None):
    """Configure logging for the entire application"""
    
    os.makedirs(log_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_filename = f"app_{timestamp}.log"
    log_file = os.path.join(log_dir, log_filename)
    
    # Get logger - use module name if provided
    logger = logging.getLogger(module_name if module_name else "")
    
    # Set level for all handlers
    logger.setLevel(logging.DEBUG if debug else logging.INFO)
    
    # Create file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    ))
    
    # Create console handler (optional)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(logging.Formatter(
        '%(levelname)s - %(message)s'
    ))
    
    # Add handlers to logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger, log_file