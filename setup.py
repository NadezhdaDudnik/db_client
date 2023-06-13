from distutils.core import setup

REQUIRES = [
    'records',
    'structlog'
]
setup(
    name='db_client',
    version='0.0.1',
    packages=['db_client'],
    url='https://github.com/NadezhdaDudnik/db_client.git',
    license='MIT',
    author='Nadezhda Dudnik',
    author_email='-',
    install_requires=REQUIRES,
    description='db client with allure and logger'
)
