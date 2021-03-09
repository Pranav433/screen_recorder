
from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Microsoft :: Windows :: Windows 10',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]

with open("requirements.txt","r") as f:
    requirements = []
    for i in f.readlines():
        requirements.append(i.replace('\n',''))
with open("README.md",'r') as f:
    long_description = f.read()


setup(name="screen_recorder",version='1.0',description="A simple screen recorder package for python",long_description=long_description,url="https://github.com/Pranav433/screen_recorder",classifiers=classifiers,keywords='screen recorder',packages=find_packages(),install_requires=requirements,author="Pranav Parashar",author_email="krish420360@gmail.com",license='MIT',)