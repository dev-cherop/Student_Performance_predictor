from setuptools import setup, find_packages
from typing import List


hyphen_e_dot = '-e .'
def get_requirements(file_path: str) -> List[str]:
    '''
    This function reads the requirements from a file and returns them as a list.
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements=[req.replace("\n", "") for req in requirements]
        if hyphen_e_dot in requirements:
            requirements.remove(hyphen_e_dot)
    return requirements

setup(
    name='mlproject',
    version='0.1.0',
    author='dev-cherop',
    author_email='cheropelishakamusongwe@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)