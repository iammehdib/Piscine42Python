import importlib.metadata
import importlib.util

DEPENDENCIES = {
    "pandas": "Data manipulation ready",
    "numpy": "Numerical computation ready",
    "matplotlib": "Visualization ready",
}


def check_dependency(name: str, description: str) -> bool:
    if importlib.util.find_spec(name) is None:
        print(f"[MISSING] {name} - library not found")
        return False

    ver = importlib.metadata.version(name)
    print(f"[OK] {name} ({ver}) - {description}")
    return True


def analyze_all_dependencies() -> None:
    import matplotlib.pyplot as matplt
    import numpy as np
    import pandas as pd

    print()
    print("Analyzing Matrix data...")
    df = pd.DataFrame(np.random.randn(1000), columns=["matrix_signal"])
    print("Processing 1000 data points...")
    print("Generating visualization...")
    df.plot()
    matplt.savefig("matrix_analysis.png")
    matplt.close("all")
    print()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


def main() -> None:
    print("LOADING STATUS: Loading programs...")
    print()
    print("Checking dependencies:")

    is_all_dependencies_present = True
    for name, description in DEPENDENCIES.items():
        if not check_dependency(name, description):
            is_all_dependencies_present = False

    if is_all_dependencies_present:
        analyze_all_dependencies()
        return

    print()
    print("To install with pip: pip install -r requirements.txt")
    print("To install with Poetry: poetry install")


if __name__ == "__main__":
    main()
