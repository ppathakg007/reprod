from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'Test Package'
LONG_DESCRIPTION = DESCRIPTION

setup(
name="test_package_for_dbk_support",
version=VERSION,
author="Thermo Fisher Scientific",
author_email="",
description=DESCRIPTION,
long_description=LONG_DESCRIPTION,
packages=find_packages(),
install_requires=[],
)