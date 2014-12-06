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
	@tornado.web.asynchronous
	def get(self):
		self.set_status(200)
		self.write("hello, world")
		self.finish()

# class WebApplication(tornado.web.Application):
	
# 	def __init__(self, config, main_loop=None):

# 		# self.we_clients = WebSocketClients()
# 		# self.ws_listener = WebSocketListener(app=self, clients=self.ws_clients)

# 		# websocket_references = {}
# 		# websocket_references['clients'] = self.ws_clients
# 		# websocket_references['listener'] = self.ws_listener
# 		root = os.path.dirname(__file__)
# 		settings = {
# 			'template_path': root,
# 			'debug': True if config.getint('bankwebapp','debug') == 1 else False,
# 			'gzip': True if config.getint('bankwebapp','gzip') == 1 else False,
# 			# 'xsrf_cookies': True,
# 			'login_url': '/',
# 			'cookie_secret': 'Y2FmNTRiN2ItODM4NS00ODFiLWIzODAtNTNmMDViYWE3M2M3'
# 		}

# 		self.config = config

# 		handlers = []
# 		handlers.append((r'/', MainHandler))

# 		tornado.web.Application.__init__(self, handlers, **settings)


application = tornado.web.Application([
	(r'/?', MainHandler)
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

	logging.basicConfig(filename=config.get('bankwebapp', 'logpath'), level=logging.DEBUG)

	'''INIT SERVER'''
	main_loop = tornado.ioloop.IOLoop.instance()
	#application = WebApplication(config=config, main_loop=main_loop)
	application.listen(config.getint('bankwebapp','port'))
	logging.getLogger('webserver').info('<!> bank webapp initialized')
	main_loop.start()

if __name__ == "__main__":
	main()
