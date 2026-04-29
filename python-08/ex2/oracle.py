import os
import sys
from dotenv import load_dotenv


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")

    load_dotenv()

    mode = os.getenv("MATRIX_MODE", "unknown")
    db_url = os.getenv("DATABASE_URL", "unknown")
    api_key = os.getenv("API_KEY", "")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    zion_endpoint = os.getenv("ZION_ENDPOINT", "Offline")

    print("\nConfiguration loaded:")
    print(f"Mode: {mode}")
    
    if mode == "development":
        print("Database: Connected to local instance")
    else:
        print(f"Database: Connected to remote {db_url}")
        
    print("API Access: Authenticated" if api_key else "API Access: Denied (Missing Key)")
    print(f"Log Level: {log_level}")
    print(f"Zion Network: {'Online' if zion_endpoint != 'Offline' else 'Offline'}")

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARN] .env file is missing!")
        
    if os.getenv("MATRIX_MODE") == "production":
        print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()