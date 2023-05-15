import os

from dotenv import load_dotenv

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Load minimum env vars needed for .env
env = os.environ.get("ENV", "LOCAL").lower()

# Load .env before other settings to properly set environment defaults from the
# config (those not already set at the OS/instance)
dotenv_path = BASE_DIR + "/config/.env." + env
load_dotenv(dotenv_path=dotenv_path)

BASE_URL = os.environ.get("BASE_URL")

IS_PROD_ENV = env == "prod"
IS_LOCAL_ENV = env == "local"
IS_DEV_ENV = env == "dev"

REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = int(os.environ.get("REDIS_PORT", 6379))
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD")

MONGODB_HOST = os.environ.get("MONGODB_HOST", "mongodb")
MONGODB_PORT = int(os.environ.get("MONGODB_PORT", 27017))
MONGODB_NAME = os.environ.get("MONGODB_NAME", "szalinski")
MONGODB_COLLECTION = os.environ.get("MONGODB_COLLECTION", "collection")
MONGODB_USER = os.environ.get("MONGODB_USER", "root")
MONGODB_PASS = os.environ.get("MONGODB_PASS", "toor2023")
