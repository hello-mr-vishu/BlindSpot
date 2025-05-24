from setuptools import setup, find_packages 
from typing import List

def get_requirements()->List[str]:
    """
    This function returns a list of requirements
    """
    requrement_lst:List[str]= []
    try:
        with open('requirements.txt','r') as file:
            # Read the lines from the file
            lines = file.readlines()
            # Process each line
            for line in lines:  
                requirement = line.strip()
                # Ignore empty lines and "-e ."
                if requirement and requirement != '-e .':
                    requrement_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found")
    return requrement_lst       

# print(get_requirements())

setup(
    name= "NetworkSecurity",
    version= '0.0.1',
    author='Vishnu Vardhan',
    author_email= 'vishnurongali21@gmail.com',
    packages=find_packages(),
    install_requires =  get_requirements()                
)