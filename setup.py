from setuptools import setup, find_packages

with open("requirements.txt") as requirements:
    setup(
        name="kajou",
        version="0.0.1",
        packages=find_packages(),
        install_requires=requirements,
        entry_points={
            "console_scripts": [
                "kajou=src.main:main"
            ]
        }
    )
