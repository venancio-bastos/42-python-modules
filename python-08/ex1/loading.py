import sys
import importlib.metadata

try:
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    HAS_DEPS = True
except ImportError as e:
    MISSING_DEP = e.name
    HAS_DEPS = False


def print_status() -> None:
    print("LOADING STATUS: Loading programs...")
    packages = {
        "pandas": "Data manipulation ready",
        "requests": "Network access ready",
        "matplotlib": "Visualization ready",
        "numpy": "Numerical computation ready"
    }

    print("Checking dependencies:")
    for pkg, msg in packages.items():
        try:
            version = importlib.metadata.version(pkg)
            print(f"[OK] {pkg} ({version}) - {msg}")
        except importlib.metadata.PackageNotFoundError:
            print(f"[FAIL] {pkg} is missing.")


def analyze_data() -> None:
    print("Analyzing Matrix data...")
    print("Processing 1000 data points...")

    np.random.seed(42)
    data = np.random.randn(1000, 2)
    df = pd.DataFrame(data, columns=["Anomaly Score", "Glitch Probability"])

    print("Generating visualization...")
    plt.figure(figsize=(10, 6))
    plt.scatter(
        df["Anomaly Score"], df["Glitch Probability"], alpha=0.5, c="green"
    )
    plt.title("Matrix Anomaly Detection")
    plt.xlabel("Anomaly Score")
    plt.ylabel("Glitch Probability")
    plt.grid(True)
    plt.savefig("matrix_analysis.png")

    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    if not HAS_DEPS:
        print("LOADING STATUS: Failed to load programs.")
        print(f"Missing dependency: {MISSING_DEP}")
        print("Please install dependencies to continue:")
        print("Using pip:    pip install -r requirements.txt")
        print("Using Poetry: poetry install")
        sys.exit(1)

    print_status()
    analyze_data()


if __name__ == "__main__":
    main()
