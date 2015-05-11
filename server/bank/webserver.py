import sys
import os
import base64
import uuid
import json
import argparse
import configparser
import logging
import logging.config

from sqlalchemy import engine_from_config
from sqlalchemy.orm import scoped_session, sessionmaker

import tornado.ioloop
import tornado.web

from .handlers import work_statement_api as work_statement_handlers

def parse_config(config_file):
	config = configparser.RawConfigParser()
	config.read(config_file)
	return config


class WebApplication(tornado.web.Application):
	
	def __init__(self, config, main_loop=None):

		self.db = scoped_session(sessionmaker(bind=engine_from_config({
				'sqlalchemy.url': config.get('sqlalchemy', 'url'),
				'sqlalchemy.echo': config.getboolean('sqlalchemy', 'echo')
			})))
		
		root = os.path.dirname(__file__)
		
		settings = {
			'debug': True,
			'cookie_secret': str(base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes))
		}

		self.config = config

		handlers = []
		handlers += work_statement_handlers 

		tornado.web.Application.__init__(self, handlers, **settings)

def main():
	parser = argparse.ArgumentParser(description="Bank webapp init")
	parser.add_argument('--config', dest='config', required=True)
	args = parser.parse_args()
	if not args.config:
		parser.print_help()
		sys.exit(1)

	config = parse_config(args.config)
	if not config.has_option('bankwebapp', 'port'):
		print('port is required')
		sys.exit(1)

	#logging.basicConfig(filename=config.get('bankwebapp', 'logpath'), level=logging.DEBUG)
	logging.config.fileConfig(args.config, disable_existing_loggers=0)
	logging.getLogger('tornado').setLevel(config.getint('bankwebapp', 'logging'))
	logging.getLogger('webserver').info('<!> bank webapp being initialized...')
	'''INIT SERVER'''
	main_loop = tornado.ioloop.IOLoop.instance()
	application = WebApplication(config=config, main_loop=main_loop)
	application.listen(config.getint('bankwebapp','port'))
	logging.getLogger('webserver').info('<!> bank webapp initialized (version = %s)' % ('0.0.1'))
	logging.info("hello")
	main_loop.start()

if __name__ == "__main__":
	main()
