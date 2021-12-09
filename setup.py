from setuptools import find_packages, setup

setup(
    name='rand_num',
    packages=find_packages(include=['rand_num']),
    version='0.1.0',
    description='Random Number Generator',
    author='Lopez Chaidez Luis Enrique',
    license='MIT',
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',

)