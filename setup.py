from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in model_no/__init__.py
from model_no import __version__ as version

setup(
	name="model_no",
	version=version,
	description="Model no",
	author="Darshit Patel",
	author_email="darshpatelvadadoriya@gmai.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
