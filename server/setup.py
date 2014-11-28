from setuptools import setup, find_packages

version = '0.0.1'

install_requires = [
	'SQLAlchemy==0.9.4',
	'alembic',
	'pymysql'
]

setup(name='Bank',
	version=version,
	description=('For managing banking needs'),
	author='David Parr',
	author_email='dvdprr6@gmail.com',
	packages=find_packages(),
	install_requires=install_requires,
	entry_points={
		'console_scripts':['bankwebapp = bank.webserver:main']
	}

)