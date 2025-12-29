from dotenv import load_dotenv
import os

# Check current working directory
print(f"Current directory: {os.getcwd()}")

# Check if .env file exists
env_path = ".env"
print(f".env file exists: {os.path.exists(env_path)}")

# Try loading with explicit path
load_dotenv(dotenv_path=env_path, verbose=True)

access_key = os.getenv("AWS_ACCESS_KEY_ID")
secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
region = os.getenv("AWS_DEFAULT_REGION")

print(f"AWS Access Key: {access_key}")
print(f"AWS Secret Key: {secret_key}")
print(f"AWS Region: {region}")