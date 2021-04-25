from setuptools import setup
from fresh import __version__

setup(
    name="django-autorefresh",
    version=__version__,
    license="Simplified BSD",
    install_requires=["Django>=3.1.7", "watchdog>=2.0.3", "beautifulsoup4>=4.9.3"],
    description="Auto-refresh your browser when files in your project change.",
    long_description=open("README.md").read(),
    author="Isaac Bythewood, Jadson Lucio",
    url="http://github.com/jadsonlucio/django-autorefresh",
    download_url="http://github.com/jadsonlucio/django-autorefresh/downloads",
    include_package_data=True,
    packages=["fresh"],
    zip_safe=False,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django"
    ],
)
