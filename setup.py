import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="golddigger-Soldy",
    version="0.0.1",
    author="Soldy",
    author_email="golddigger@gidigi.com",
    description="Unsafe security mainer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Soldy/golddigger",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3 License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
