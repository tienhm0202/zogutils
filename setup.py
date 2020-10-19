import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="zogvn-utils-tienhm", # Replace with your own username
    version="0.0.1",
    author="Hoang Manh Tien",
    author_email="tienhm.0202@gmail.com",
    description="Utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitlab.com/tienhm/zogvn-utils",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
