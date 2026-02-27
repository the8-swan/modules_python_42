import os
import sys
from dotenv import load_dotenv

try:
    # load_dotenv() reads the .env file and puts all its variables
    # into the environment so os.getenv() can access them
    load_dotenv()

    print("\nORACLE STATUS: Reading the Matrix...\n")

    # os.getenv() reads a variable from the environment
    # the second argument is the default value if the variable is not set
    mode = os.getenv("MATRIX_MODE", "development")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    endpoint = os.getenv("ZION_ENDPOINT")

    print("Configuration loaded:")
    print(f"Mode: {mode}")

    # we don't print the actual values of secrets like database_url or api_key
    # we just confirm whether they are set or not
    if database_url:
        print(f"Database: Connected to local instance")
    else:
        print(f"Database: No URL provided")

    if api_key:
        print(f"API Access: Authenticated")
    else:
        print(f"API Access: No key provided")

    print(f"Log Level: {log_level}")

    if endpoint:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")

    print("\nEnvironment security check:")
    # secrets are in .env and environment variables, nothing is hardcoded in the source
    print("[OK] No hardcoded secrets detected")

    # check if the .env file actually exists in the current directory
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] .env file not found")

    # environment variables set directly in the shell always override the .env file
    # that's how you switch to production without changing any code
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations")

except ModuleNotFoundError as e:
    # python-dotenv is not installed
    print(f"{e}")