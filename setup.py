from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirement(file_path : str)->List[str]:
    requirement= []
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace("/n","") for req in requirement]

        if HYPEN_E_DOT in requirement:
            requirement.remove(HYPEN_E_DOT)

    return requirement

setup(
    name='mlproject',
    version='0.1.0',
    description='A short description of my package',
    author='abhijeet lanjewar',
    author_email='lanjewarabhijeet02@gmail.com',
    packages=find_packages(),
    install_requires=get_requirement('requirements.txt'),
)