"""Setup script for realpython-reader"""

import os.path
from setuptools import setup

# The directory containing this file
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
with open(os.path.join(HERE, "README.md")) as fid:
    README = fid.read()

# This call to setup() does all the work
setup(
    name="YTDownloader",
    version="1.0.0",
    description="Read the latest Real Python tutorials",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/realpython/reader",
    author="Real Python",
    author_email="office@realpython.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    packages=["reader"],
    include_package_data=True,
    install_requires=[
        "pytube", "string", "os", "datetime", "random", "time"
    ],
    entry_points={"console_scripts": ["ytdownloader=ytdownloader.__main__:main"]},
)
