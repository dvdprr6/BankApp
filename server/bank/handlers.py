import logging
import json

import tornado.web


logging = logging.getLogger(__name__)

class BaseRequestHandler(tornado.web.RequestHandler):

	@property
	def db(self):
		return self.application.db

	@property
	def request_body_json(self):
		return json.loads(self.request.body.decode('utf-8'))


'''
	Work Statement API
'''
from .work_statement.handlers import MainHandler

work_statement_api = [
	(r'/?', MainHandler)

]