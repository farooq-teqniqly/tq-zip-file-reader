"""
Setup module.
"""

from setuptools import setup, find_packages
import tq


def long_description():
    """
    Returns the text of the readme.
    :return: The text of the readme.
    """
    with open("README.md", encoding="utf-8") as file:
        return file.read()


PROJECT_URL = "https://github.com/farooq-teqniqly/tq-zip-file-reader"

setup(
    name="tq-zip-file-reader",
    version=tq.__version__,
    description=tq.__doc__.strip(),
    long_description=long_description(),
    long_description_content_type="text/markdown",
    url=PROJECT_URL,
    author=tq.__author__,
    author_email="farooq@teqniqly.com",
    license=tq.__license__,
    packages=find_packages(include=["tq", "tq.*"]),
    python_requires=">=3.9",
    install_requires=[],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3 :: Only",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Utilities"
    ],
    project_urls={"GitHub": PROJECT_URL}
)
