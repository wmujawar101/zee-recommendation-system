import os

# General Settings
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))  # Get the root directory of the project
DEBUG = True  # Toggle for enabling/disabling debug mode in your app (useful for development)

# Paths
MODEL_DIR = os.path.join(PROJECT_ROOT, 'model')  # Directory where models are stored
MODEL_FILE = os.path.join(MODEL_DIR, '{}')
SVD_MODEL = os.path.join(MODEL_DIR, 'svd_model')


# API Settings
API_HOST = '0.0.0.0'  # Host for your API
API_PORT = 8000  # Port for your API

# Model Type
COSINE_MODEL = "Cosine"
PEARSON_MODEL = "Pearson"

# Matrix Type
USER_USER_MATRIX = "User"
ITEM_ITEM_MATRIX = "Item"
