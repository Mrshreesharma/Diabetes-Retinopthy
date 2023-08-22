from setuptools import find_packages,setup
from typing import List

hyphon_E_dot = '-e .'
def get_requirements(file_path:str)->List[str]:

    '''
    this function will return a list of requiremnets
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements =[req.replace("/n","") for req in requirements]

        if hyphon_E_dot in requirements:
            requirements.remove(hyphon_E_dot)
    return requirements


setup(name= 'mlproject',
version='0.0.1',
author='Shree',
author_email='Shree370@gmail.com',
packages=find_packages(),
install_requires= get_requirements('requirements.txt')
)


