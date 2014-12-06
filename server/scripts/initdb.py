import os
import sys
import logging
import argparse
import configparser
from sqlalchemy import create_engine
from bank.db.models import Base

'''
To get the .db for sqlite
python scripts/initdb.py --config=conf/test/bank.conf
'''

def parse_config(config_file):
	config = configparser.RawConfigParser()
	config.read(config_file)
	return config

def createDatabase(config):
	db_url = config.get('sqlalchemy','url')
	db_echo = config.getboolean('sqlalchemy', 'echo')
	DbEngine = create_engine(db_url, echo=db_echo)
	Base.metadata.create_all(DbEngine)

def main(argv=sys.argv):
	parser = argparse.ArgumentParser(description="Bank DB Init")
	parser.add_argument('--config', dest='config', required=True)
	args = parser.parse_args()
	if not args.config:
		parser.print_help()
		sys.exit(1)
	config = parse_config(args.config)
	createDatabase(config)

if __name__ == '__main__':
	main()
