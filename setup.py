from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[:str]:
    '''
    this function return the required packages from the given file path
    '''
    requirements=[]
    with open(file_path)as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n',"") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements



setup(
    name='mlproject',
    version='1.0.0',
    author='Mastan',
    author_email='venkatamastan.mudigonda@gmai.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)