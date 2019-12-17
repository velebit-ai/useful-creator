from setuptools import setup

exec(open("useful/creator/version.py").read())

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="useful-creator",
    version=__version__,  # noqa
    description="Creating instances from dictionaries",
    classifiers=[
        "Licence :: OSI Approved :: MIT License",

        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6"
    ],
    url="https://github.com/velebit-ai/useful-creator",
    author="Velebit AI",
    author_email="contact@velebit.ai",
    packages=["useful.creator"],
    install_requires=requirements,
    include_package_data=True
)
