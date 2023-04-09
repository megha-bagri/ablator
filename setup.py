from setuptools import find_packages, setup
from pathlib import Path

package_path = __file__
setup(
    name="trainer",
    version="0.0.1",
    author="Iordanis Fostiropoulos",
    author_email="danny.fostiropoulos@gmail.com",
    packages=find_packages(),
    description="Model Trainer and Ablation tool-kit",
    python_requires=">3.10",
    long_description=Path(package_path).parent.joinpath("README.md").read_text(),
    install_requires=[
        "numpy",
        "pandas",
        "scikit_learn",
        "torch",
        "tqdm",
        "tensorboard",
        "matplotlib",
        "omegaconf",
        "setproctitle",
        "torchvision",
        "sqlalchemy==2.0.6",
        "tabulate",
        "ray",
        "pynvml",
        "optuna"
    ],
    extras_require={
        "dev": ["mypy", "pytest", "pylint", "flake8", "black"],
    },
)