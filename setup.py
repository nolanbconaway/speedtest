"""Setup file for the module."""

from setuptools import setup

setup(
    name="speedtestimage",
    packages=["speedtestimage"],
    version="0.1.2",
    install_requires=["speedtest-cli", "pillow"],
    entry_points={"console_scripts": ["speedtestimage=speedtestimage.__main__:main"]},
    package_data={"speedtestimage": ["Courier.ttf"]},
)

