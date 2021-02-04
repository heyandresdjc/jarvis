from setuptools import setup, find_packages


def read_requirements():
    with open('requirements.txt') as req:
        content = req.read()
        requirements = content.split('\n')
    return requirements


setup(
    name='jarvis',
    version='0.0.1',
    packages=find_packages(),
    url='',
    license='MIT',
    author='Andres DJC',
    author_email='heyandresdjc@gmail.com',
    description='',
    include_package_data=True,
    install_requires=read_requirements(),
    entry_points='''
        [console_scripts]
        jarvis=jarvis.cli:cli
    '''
)
