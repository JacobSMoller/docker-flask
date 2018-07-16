from distutils.core import setup

setup(
    name='MyApp',
    version='0.0.1',
    author='J.S-Moeller',
    author_email='scherffenberg91@gmail.com',
    license='LICENSE.txt',
    description='Dockerizing a flask app with setup file.',
    long_description=open('README.md').read(),
    install_requires=[
        "flask>=1.0.0,<1.1.0",
        "gunicorn>=19.9.0,<20.0.0"
    ],
)
