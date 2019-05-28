from setuptools import setup


setup(
    name='json2dynamo',
    version='0.0.2',
    author='Allan Kilpatrick',
    author_email='allanklp@gmail.com',
    url='https://github.com/allankp/json2dynamo',
    packages=['json2dynamo'],
    package_dir={'json2dynamo': 'json2dynamo'},
    install_requires=['dynamodb-json==1.3', "Click==7.0"],
    include_package_data=True,
    entry_points={"console_scripts": ["json2dynamo=json2dynamo.app:cli"]}
)
