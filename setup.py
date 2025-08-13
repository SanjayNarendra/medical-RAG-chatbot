from setuptools import setup,find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name = "Medical chatbot RAG",
    version = "0.1",
    author = "Sanjay Narendra",
    packages = find_packages(),
    install_requires = requirements,
)