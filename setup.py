from setuptools import setup, find_packages

setup(
    name="linear-regression-advertising",
    version="0.1.0",
    author="Roshini Priya C H",
    description="Linear regression package for advertising sales analysis",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "scikit-learn",
        "matplotlib",
        "seaborn"
    ],
)
