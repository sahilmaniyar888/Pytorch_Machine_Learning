"""Quick import check for packages listed in requirements.txt."""

from __future__ import annotations


def main() -> None:
    import cv2
    import matplotlib
    import numpy
    import pandas
    import scipy
    import seaborn
    import sklearn
    import statsmodels
    import torch

    print("All imports successful:")
    print(f"numpy: {numpy.__version__}")
    print(f"pandas: {pandas.__version__}")
    print(f"scikit-learn: {sklearn.__version__}")
    print(f"matplotlib: {matplotlib.__version__}")
    print(f"seaborn: {seaborn.__version__}")
    print(f"scipy: {scipy.__version__}")
    print(f"statsmodels: {statsmodels.__version__}")
    print(f"torch: {torch.__version__}")
    print(f"opencv-python (cv2): {cv2.__version__}")


if __name__ == "__main__":
    main()
