from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="geolocation-microservice",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A microservice for geolocation using Google Geolocation API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/geolocation-microservice",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask>=2.0.1",
        "requests>=2.25.1",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    entry_points={
        'console_scripts': [
            'geolocation-microservice=app.main:main',
        ],
    },
)