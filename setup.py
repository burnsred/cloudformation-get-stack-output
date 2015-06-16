from setuptools import setup

setup(
    name='cloudformation-get-stack-output',
    version='0.0.1',
    scripts=['bin/cloudformation-get-stack-output'],
    include_package_data=True,
    license='MIT License',
    author='Michael Bertolacci',
    author_email='michael@burnsred.com.au',
    url='',
    long_description=open('README.md').read(),
    install_requires=['boto>=2.34.0'],
)