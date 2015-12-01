from setuptools import setup, find_packages

setup(
    name="doubledjango",
    version='0.0.0',

    url="",
    author="Jakub Pocentek",
    author_email="jpocentek@gmail.com",

    packages=find_packages(),
    include_package_data=True,
    scripts=[
        'scripts/manage.py',
    ],

    install_requires=(
        'Django==1.8.7',
    )
)

