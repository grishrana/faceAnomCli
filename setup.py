from setuptools import setup, find_packages

setup(
    name="FAC",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["click", "opencv-contrib-python"],
    entry_points={
        "console_scripts": [
            "fac = fac.faceAnomCli:main",
        ],
    },
)
