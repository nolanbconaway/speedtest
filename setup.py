"""Setup file for the module."""

from setuptools import setup

setup(
    name="speedtestimage",
    packages=["speedtestimage"],
    version="0.1.1",
    install_requires=["speedtest-cli", "pillow"],
    scripts=["speedtestimage/speedtestimage"],
    package_data={"speedtestimage": ["Courier.ttf"]},
)

