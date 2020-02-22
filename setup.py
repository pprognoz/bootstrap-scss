from setuptools import setup, find_packages

setup(
    name="bootstrap-scss",
    version="4.4.1-1",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "django>=2.2",
        'django-libsass',
        'django-compressor',
    ],
)
