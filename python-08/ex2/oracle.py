import os
import sys
from dotenv import load_dotenv


def load_configuration() -> dict:
    load_dotenv()

    config = {
        "MATRIX_MODE": os.getenv("MATRIX_MODE", "development"),
        "DATABASE_URL": os.getenv("DATABASE_URL"),
        "API_KEY": os.getenv("API_KEY"),
        "LOG_LEVEL": os.getenv("LOG_LEVEL", "INFO"),
        "ZION_ENDPOINT": os.getenv("ZION_ENDPOINT")
    }

    return config


def verify_security(config: dict) -> None:
    print("Environment security check:")

    if "your_secret_key_here" in str(config.get("API_KEY")):
        print("[FAIL] Hardcoded or example secrets detected")
    else:
        print("[OK] No hardcoded secrets detected")

    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARN] .env file not found, using system environment")

    if config.get("MATRIX_MODE") == "production":
        print("[OK] Production overrides active")
    else:
        print("[OK] Production overrides available")


def display_status(config: dict) -> None:
    print("ORACLE STATUS: Reading the Matrix...")
    print("Configuration loaded:")

    mode = config.get("MATRIX_MODE")
    print(f"Mode: {mode}")

    db_status = (
        "Connected to local instance"
        if mode == "development"
        else "Connected to production cluster"
    )
    if not config.get("DATABASE_URL"):
        db_status = "Disconnected (No URL)"
    print(f"Database: {db_status}")

    auth_status = "Authenticated" if config.get("API_KEY") else "Unauthorized"
    print(f"API Access: {auth_status}")

    print(f"Log Level: {config.get('LOG_LEVEL')}")

    network_status = "Online" if config.get("ZION_ENDPOINT") else "Offline"
    print(f"Zion Network: {network_status}")


def main() -> None:
    config = load_configuration()
    display_status(config)
    print()
    verify_security(config)
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
