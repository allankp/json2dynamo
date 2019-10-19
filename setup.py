from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='json2dynamo',
    version='0.1.1',
    author='Allan Kilpatrick',
    author_email='allanklp@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/allankp/json2dynamo',
    packages=['json2dynamo'],
    package_dir={'json2dynamo': 'json2dynamo'},
    install_requires=['dynamodb-json==1.3', "Click==7.0"],
    include_package_data=True,
    entry_points={"console_scripts": ["json2dynamo=json2dynamo.app:cli"]}
)
