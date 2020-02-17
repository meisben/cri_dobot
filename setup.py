# -*- coding: utf-8 -*-
"""Setup file for Common Robot Interface.
"""

from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="cri_dobot",
    version="0.0.1",
    description="Common Robot Interface",
    license="GPLv3",
    long_description=long_description,
    author="Ben Money-Coomes",
    author_email="ben.money@gmail.com",
    url="https://github.com/meisben",
    packages=["cri_dobot",],
    install_requires=["numpy", "transforms3d"]
)
