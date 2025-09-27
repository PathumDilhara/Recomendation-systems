from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# pypi is for pip installation

AUTHOR_NAME = 'Pathum Dilhara'
SRC_REPO = 'src'
LIST_OF_REQUIREMENTS = ['streamlit']

setup(
    name=SRC_REPO,
    version='0.0.1',
    author=AUTHOR_NAME,
    author_email='diharapathum870@gmail.com',
    description='A samll python web app for movire recommendation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    # url='github url is ok'
    package = [SRC_REPO],
    python_requires = '>=3.7',
    install_requires = LIST_OF_REQUIREMENTS
)