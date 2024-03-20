"""Python setup.py for epitech_timeline_exporter package"""

import io
import os
from setuptools import setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("project_name", "VERSION")
    '0.1.0'
    >>> read("README.md")
    ...
    """

    content = ""
    with io.open(
        os.path.join(os.path.dirname(__file__), *paths),
        encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()
    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]


setup(
    name="epitech_timeline_exporter",
    version=read("epitech_timeline_exporter", "VERSION"),
    description="Timeline exporter for Epitech semesters",
    url="https://github.com/kreog-com/epitech-timeline-exporter",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="Alexandre Flion <huntears@kreog.com>",
    install_requires=read_requirements("requirements.txt"),
    entry_points={
        "console_scripts": ["etlexport = epitech_timeline_exporter.__main__:main"]
    },
    license_files=["LICENSE"],
)
