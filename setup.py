from setuptools import setup,find_packages
from typing import List


HYPHONE_EDOT="-e ."
def get_requires(file_path:str)->list[str]:
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]

    if HYPHONE_EDOT in requirements:
        requirements.remove(HYPHONE_EDOT)
    return requirements

       


setup(
    name = "ml_project",
    version = "0.0.1",
    author="amol",
    packages=find_packages(),
    author_email="amolbhavar27ab@gmail.com",
    install_requires=get_requires("requirements.txt")
)