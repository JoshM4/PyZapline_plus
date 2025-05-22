from setuptools import setup, find_packages

setup(
    name="pyzaplineplus",
    version="1.0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scipy",
        "scikit-learn",
        "matplotlib",
    ],
    python_requires=">=3.13",
) 