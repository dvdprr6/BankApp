import os
import sys
sys.path.append('/home/david/projects/BankApp/db/')
import logging
import argparse
import configparser

from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import create_engine
from bank.db.models import Base, Company, Date

def parse_config(config_file):
	config = configparser.RawConfigParser()
	config.read(config_file)
	return config

def createDatabase(config):
	db_url = config.get('sqlalchemy', 'url')
	db_echo = config.getboolean('sqlalchemy', 'echo')
	logging.info('creating %s' % db_url)
	DBEngine = create_engine(db_url, echo=db_echo)

	Base.metadata.create_all(DBEngine)

	initializeDatabase(DBEngine)

def initializeDatabase(engine):
	db = scoped_session(sessionmaker(bind=engine))

	company = Company(
		name='Nuance'
		)

	date = Date()

	db.add(company)
	db.add(date)
	db.commit()


"""
To init the database:
python initdb.py --config=../conf/python/dev/bank.conf
"""

def main(argv=sys.argv):
	parser = argparse.ArgumentParser(description="NDEV+ DB Init")
	parser.add_argument('--config', dest='config', required=True)
	args = parser.parse_args()
	if not args.config:
		parser.print_help()
		sys.exit(1)
	config = parse_config(args.config)

	createDatabase(config)



if __name__ == '__main__':
	main()