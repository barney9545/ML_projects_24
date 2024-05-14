from setuptools import find_packages,setup
hyphen_e = '-e.'

def get_requirements(file_path:str):
    '''
    this return list of requirements
    '''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n','')for req in requirements]

        if hyphen_e in requirements:
            requirements.remove(hyphen_e)
setup (
    name = 'ml_project',
    version = '0.0.1',
    author= 'Darshan',
    packages=find_packages(),
    install_requires = get_requirements('requirements.txt')


)