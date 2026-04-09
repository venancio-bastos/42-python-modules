import sys
import os
import site


def is_in_matrix() -> bool:
    return hasattr(sys, "real_prefix") or (
        hasattr(sys, "base_prefix") and sys.base_prefix != sys.prefix
    )


def main() -> None:
    if not is_in_matrix():
        print("MATRIX STATUS: You're still plugged in")
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("To enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate  # On Unix")
        print("matrix_env\\Scripts\\activate   # On Windows")
        print("Then run this program again.")
    else:
        print("MATRIX STATUS: Welcome to the construct")
        print(f"Current Python: {sys.executable}")
        
        env_path = sys.prefix
        env_name = os.path.basename(env_path)
        
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {env_path}")
        print("SUCCESS: You're in an isolated environment!")
        print(
            "Safe to install packages without affecting\n"
            "the global system."
        )
        
        try:
            site_pkgs = site.getsitepackages()[0]
        except AttributeError:
            site_pkgs = os.path.join(env_path, "lib", "site-packages")
            
        print("Package installation path:")
        print(site_pkgs)


if __name__ == "__main__":
    main()
