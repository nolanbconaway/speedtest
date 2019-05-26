from setuptools import setup

setup(
    name="speedtestimage",
    version="0.1",
    install_requires=["speedtest-cli", "pillow"],
    scripts=["speedtestimage"],
)

