import logging
import json

import tornado
import tornado.gen

from tornado.web import HTTPError

from ..handlers import BaseRequestHandler

logger = logging.getLogger(__name__)

class MainHandler(BaseRequestHandler):
	@tornado.web.asynchronous
	def get(self):
		self.set_status(200)
		self.write("hello, world")
		self.finish()