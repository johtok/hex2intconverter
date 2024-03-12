from setuptools import setup

setup(
    name='hex_conversion_package',
    version='1.0',
    packages=['hex_conversion_package'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'hex-converter = hex_conversion_package.cli_hex_converter:main',
        ],
    },
)
