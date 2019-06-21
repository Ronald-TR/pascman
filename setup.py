import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pascman",
    version="0.0.3",
    author="Ronald Rodrigues Farias",
    author_email="ronald-farias@outlook.com",
    description="Eat every text that you want with this simpatic pacman! :D",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ronald-TR/pascman",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points = {
        'console_scripts': ['pascman=pascman.main:main'],
    }
)
