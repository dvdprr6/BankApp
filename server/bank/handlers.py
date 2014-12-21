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
from .work_statement.handlers import GeneralStatementInfoHandler

work_statement_api = [
	(r'/work_statement/?', MainHandler),
	(r'/work_statement/general_statement_info/?', GeneralStatementInfoHandler)

]