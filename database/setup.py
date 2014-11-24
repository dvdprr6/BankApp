from setuptools import setup, find_packages

version = '0.0.1'

install_requires = [
	'SQLAlchemy==0.9.4',
	'alembic',
	'pymysql'
]
	

setup(
	name='Database',
	version=version,
	description=('For managing the database models'),
	author='David Parr',
	author_email='dvdprr6@gmail.com',
	packages=find_packages(),
	install_requires=install_requires
)
