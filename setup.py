
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fintools",
    version="0.1.1",
    author="Meng yangyang",
    author_email="mengyy_linux@163.com",
    description="Finance tools",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hotbaby/finance-tools",
    install_requires=["click>=7.0", "numpy>=1.15.4"],
    entry_points={
        'console_scripts': [
            'fin-eaoi=fin_tools.bin.eaoi:cli'
        ]
    },
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
