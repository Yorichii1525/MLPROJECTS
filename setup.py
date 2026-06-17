from setuptools import find_packages, setup

HYPEN_E_DOT = '-e .'

def get_reqirements(file_path:str)->list[str]:
    '''
        This function will return list of reqirements

    '''

    reqirements=[]
    with open(file_path) as file_obj:
        reqirements=file_obj.readline()
        reqirements=[req.replace("\n", "") for req in reqirements]

        if HYPEN_E_DOT in reqirements:
            reqirements.remove(HYPEN_E_DOT)

    return reqirements



setup(

    name="MLproject",
    version="0.0.0.1",
    author='Jagadish',
    author_email='jagadishbevara1525@gmail.com',
    packages='find_packages()',
    install_requires=get_reqirements('requirements.txt')
)