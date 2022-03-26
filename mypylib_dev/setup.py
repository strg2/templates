# License
"""Install MyPyLib"""

import setuptools

__version__ = '0.0.1'

with open('README.md') as f:
  _LONG_DESCRIPTION = f.read()

setuptools.setup(
    name='mypylib',
    version=__version__,
    description='MyPyLib: A test project.',
    long_description=_LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='John Doe',
    author_email='',
    url='http://github.com/',
    license='',
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
    ],
)
