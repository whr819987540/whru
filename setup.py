from setuptools import setup

setup(
    name='whru',
    version='0.2',
    description='My custom Python module',
    author='whr819987540',
    author_email='steeliron550@gmail.com',
    packages=['whru'],
    install_requires=[
        "torch>=1.7.0",
        "tensorflow>=2.0.2",
    ],
)