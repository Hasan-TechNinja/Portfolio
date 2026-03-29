import os
import sys

# Get current directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Add project root to Python path
sys.path.insert(0, BASE_DIR)

# Set correct settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio.settings")  # 👈 change if needed

from django.core.wsgi import get_wsgi_application

app = get_wsgi_application()