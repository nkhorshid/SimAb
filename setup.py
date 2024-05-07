from setuptools import setup, find_packages

setup(
    name='SimAb_test',
    url='https://github.com/nkhorshid/SimAb',
    author='Niloofar Khorshid',
    author_email='nd.khorshid@gmail.com',

    packages=find_packages(),
    # Needed for dependencies
    install_requires=['numpy'],

    version='0.0.2',

    license='MIT',
    description='An example of a python package from pre-existing code',
    # We will also need a readme eventually (there will be a warning)
    long_description=open('README.md').read(),
)
