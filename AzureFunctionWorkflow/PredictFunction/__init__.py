# __init__.py
import logging

# Set up shared logger configuration for functions in this directory
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
