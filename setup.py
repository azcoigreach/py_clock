from setuptools import setup

setup(
    author="azcoigreach",
    author_email="azcoigreach@gmail.com",
    name='py_clock',
    version='0.1',
    py_modules=['py_clock'],
    include_package_data=True,
    install_requires=[
        'click',
        'pyfiglet',
    ],
    entry_points='''
        [console_scripts]
        py_clock=py_clock:cli
    ''',
)
