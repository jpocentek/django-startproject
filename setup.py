from setuptools import setup, find_packages

setup(
    name="{{ PROJECT_NAME }}",
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
        'Django==1.9.2',
    )
)

