from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="",
    version="0.0.1",
    author="",
    author_email="",
    description="",
    long_description=page_description,
    long_description_content_type="text/markdow",
    url="",
    download_url="",
    packages=find_packages(),
    package_dir="",
    package_data="",
    password="",
    provides="",
    platforms="",
    py_modules="",
    include_package_data="",
    include_dirs="",
    install_requires=requirements,
    python_requires='>=3.8'
)