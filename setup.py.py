from setuptools import setup

setup(
   name='autodsc',
   version='1.0',
   description='A useful module',
   author='unk',
   author_email='unk@mail.com',
   packages=['eda', 'models', 'utils'],  #same as name
   install_requires=['multimethod ', 'tangled_up_in_unicode'],
)