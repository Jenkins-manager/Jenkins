from setuptools import setup, find_packages

setup(
    name="perManBackend", packages=find_packages(),
    setup_requires=["pytest-runner"],
    test_require=['pytest']
    )