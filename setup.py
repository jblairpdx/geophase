from codecs import open as codecs_open
from setuptools import setup, find_packages


# Get the long description from the relevant file
with codecs_open('README.rst', encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='geophase',
    version='0.0.1',
    description=(
        u"Creation & comparison of timespan-aware (phased) geospatial data."),
    long_description=long_description,
    classifiers=[],
    keywords='',
    author=u"Jacob Blair",
    author_email='jblairpdx@gmail.com',
    url='https://github.com/jblairpdx/geophase',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'click',
        ],
    extras_require={
        'test': ['pytest'],
        },
    entry_points="""
    [console_scripts]
    geophase=geophase.scripts.cli:cli
    """
    )
