from setuptools import find_packages, setup

setup(
    name='local_package',
    packages=find_packages(),
    version='0.1.0',
    description='{{ cookiecutter.description }}',
    author='{{ cookiecutter.author_name }}',
    license='MIT',
)