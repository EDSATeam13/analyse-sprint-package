from setuptools import setup, find_packages

setup(
    name='analyse_sprint_package',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='',
    long_description=open('README.md').read(),
    install_requires=['numpy', 'pandas'],
    url='https://github.com/EDSATeam13/analyse_sprint_package.git',
    author='Tsundukani Makhubela, Pono Pitsoe, Silindokuhle Kubheka, Oarabile Tsele, Mixo Shitlhangu',
    author_email='<tsundukani@icloud.com>'
)
