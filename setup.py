from setuptools import find_packages, setup
from typing import List
HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    """
    This function will return the list of requirements

    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "")for req in requirements]
        # Inside my requirements.txt packages are available
        # like---> pandas
        #          numpy
        # when i am go to the next line \n is require so.. we replace this by ""
        if HYPEN_E_DOT in requirements: # -e . i don't want here bcz it autometically trigger the setup.py also present in requirements.txt
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(

name= "MLProjects",
version = "0.0.1",
author= "Deepak",
author_email= "kdeepak8250@gmail.com",
packages= find_packages(),
install_requires = get_requirements("requirements.txt")

)