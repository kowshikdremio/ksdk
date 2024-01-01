from setuptools import setup, find_packages
import codecs
import os

VERSION = '0.0.3'
DESCRIPTION = 'Functions for interacting Dremio Sonar'

# Setting up
setup(
	name="dremiosonar",
	version=VERSION,
	author="Dremio PS",
	author_email="dremisonar@dremio.com",
	packages=find_packages(),
	install_requires=['jaydebeapi','pandas','json','requests'],
	keywords=['Dremio','Sonar','Dremio Sonar'],
	classifiers=[
		"Development Status:: 1 - Planning",
		"Intended Audience:: Developers",
		"Programming Language:: Python :: 3",
		"Operating System:: Unix ",
		"Operating System:: MacOS :: MacOS X",
		"Operating System:: Microsoft :: Windows",
	]
)


