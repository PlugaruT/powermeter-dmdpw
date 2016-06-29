import setuptools

setuptools.setup(
    name="powermeter",
    version="0.0.1",

    author="Tudor Plugaru",
    author_email="plugaru.tudor@gmail.com",

    description="Python API for reading from DMDPW powermeters",
    long_description=open('readme.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=['pymodbus'],

    classifiers=[
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
)