from setuptools import setup

exec(open("useful/creator/version.py").read())

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="useful-creator",
    version=__version__,  # noqa
    description="Useful packages",
    classifiers=[
        "Licence :: Other/Proprietary Licence",

        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6"
    ],
    url="https://gitlab.com/velebit/useful/creator",
    author="Velebit",
    author_email="dev@velebit.ai",
    packages=["useful.creator"],
    install_requires=requirements,
    include_package_data=True
)
