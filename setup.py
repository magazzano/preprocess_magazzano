import setuptools

with open('README.md', 'r') as file:
	long_description = file.read()


setuptools.setup(
	name = 'preprocess_magazzano',
	version = '0.0.2',
	author = 'Marcelo Gazzano',
	author_email = 'magazzano@gmail.com',
	description = 'This is preprocessing package',
	long_description = long_description,
	long_description_content_type = 'text/markdown',
	packages = setuptools.find_packages(),
	classifiers = [
	'Programing.Language :: Python :: 3',
	'License :: OSI Approved :: MIT License',
	'Operating System ::OS Indepedent'],
	python_requires = '>=3.5'
	)