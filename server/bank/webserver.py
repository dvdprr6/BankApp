import sys
import os
import json
import argparse
import configparser
import logging
import logging.config

import tornado.ioloop
import tornado.web

def parse_config(config_file):
	config = configparser.RawConfigParser()
	config.read(config_file)
	return config

class MainHandler(tornado.web.RequestHandler):
	def get(self):
		self.write("hello, world")

application = tornado.web.Application([
	(r'/', MainHandler)
])

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

	'''INIT SERVER'''
	application.listen(config.getint('bankwebapp','port'))
	tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
	main()
