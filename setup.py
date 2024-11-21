import setuptools

with open("README.md") as f:
    long_description = f.read()


setuptools.setup(
    name = "protogen_beeper",
    version = "0.0.3",
    author = "Prootzel",
    author_email = "lirkel123@gmail.com",
    description = "A library to test how to develop modules",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Prootzel/Protogen_Test_Library",
    packages = setuptools.find_packages(),
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)