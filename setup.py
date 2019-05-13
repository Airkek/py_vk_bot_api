import setuptools

from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip

def packages():
    pipfile = Project(chdir=False).parsed_pipfile
    return convert_deps_to_pip(pipfile['packages'], r=False)

setuptools.setup(
    name='py_vk_bot_api',
    version='1.0',
    author='Airkek',
    author_email='antonyblack05@gmail.com',
    description='Python vk.com API wrapper',
    url='https://github.com/Airkek/py_vk_bot_api/',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=packages()
)
