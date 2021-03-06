from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open('requirements.txt') as fh:
    requirements = fh.read().splitlines()

setup(
    name='PyWiW',
    version='0.1.1',
    author='Bakr Annour',
    author_email='b.annour@stuart.com',
    description='A When I Work API Python wrapper',
    long_description=long_description,
    long_description_content_type='text/markdown',
    license='',
    url='https://github.com/bannour-stuart/PyWiW',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: None',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Topic :: Office/Business :: Scheduling'
    ],
    packages=find_packages(),
    install_requires=requirements,
)