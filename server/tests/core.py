import unittest
import configparser

from tornado.testing import AsyncHTTPTestCase, LogTrapTestCase
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import engine_from_config

from bank.webserver import WebApplication

config = configparser.RawConfigParser()
config.read('conf/test/bank.conf')

app = WebApplication(config=config)

def get_db():
	database = scoped_session(sessionmaker(
		bind=engine_from_config({
			'sqlalchemy.url':config.get('sqlalchemy','url'),
			'sqlalchemy.echo':config.getboolean('sqlalchemy','echo')
		})
	))

	return database

class BaseTestCase(LogTrapTestCase):

	def setUp(self):
		self.db = get_db()
		self.config = config
		self.start()

	def tearDown(self):
		self.end():
		self.db.remove()

	def start(self):
		pass

	def end(self):
		pass

	def get_app(self):
		return app

class BaseAppTestCase(AsyncHTTPTestCase, LogTrapTestCase):

	def setUp(self):
		super().setUp()
		self._start()

	def tearDown(self):
		self._end()
		super().tearDown()

	def _start(self):
		pass

	def _end(self):
		pass

	def get_app(self):
		return app