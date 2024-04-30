from setuptools import setup, find_packages

setup(
    name="dift",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],  # Use the list of requirements as dependencies
    author="Joël Seytre",
    author_email="joel@kartoon.ai",
    description="Patched version of the DIFT repository to use with recent diffusers version",
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url="https://github.com/kartoon-ai/dift.git",
)