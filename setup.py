from setuptools import setup, find_packages

setup(
    name="bootstrap-scss",
    version="0.2",
    packages=find_packages(),
    install_requires=[
        "django>=2.2",
        'django-libsass',
    ],
)
