import json
import logging

class JSONFormatter(logging.Formatter):
    
    def format(self, record):
        # Create a dictionary out of standard LogRecord attributes
        log_entry = {
            "timestamp": self.formatTime(record, self.datefmt),
            "level": record.levelname,
            "message": record.getMessage(),
            "logger": record.name
        }

        # Safely capture extra variables if provided
        if hasattr(record, 'extra_data'):
            log_entry.update(record.extra_data)

        return json.dumps(log_entry)

def get_logger(name: str = "__name__") -> logging.Logger:
    """Create a structured JSON logger."""
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    if not logger.handlers:
        console_handler = logging.StreamHandler()
        console_handler.setLevel("INFO")
        console_handler.setFormatter(JSONFormatter())
        logger.addHandler(console_handler)

    return logger