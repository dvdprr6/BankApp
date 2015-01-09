import json
import datetime

from tornado.web import create_signed_value

from tests.core import BaseAppTestCase
from bank.db.models import GeneralStatementInfo
from .test_data import (
	TEST_GENERAL_STATEMENT_INFO_DATA,
	DEFAULT_TEST_GENERAL_STATEMENT_INFO_DATA,
	GENERAL_STATEMENT_INFO_RETURN_ATTRIBUTES,
	ENDPOINTS
)

class WorkStatementAPITestCase(BaseAppTestCase):

	def setUp(self):
		super().setUp()

	def tearDown(self):
		super().tearDown()

	@property
	def db(self):
		return self.get_app().db

	def convert_byte_string_to_JSON(self, response):
		return json.loads(response.body.decode('utf-8'))

	def fetch_request(self, *args, **kwargs):
		headers = self._authenticate_request()
		headers['Content-Type'] = 'application/json'
		kwargs['headers'] = headers
		return self.fetch(*args, **kwargs)

	def _authenticate_request(self):
		app = self.get_app()
		secure_cookie = create_signed_value(app.settings['cookie_secret'], 'test', 'user').decode('utf-8')
		headers = {
			'Cookie':'='.join(secure_cookie)
		}
		return headers

class InitializeGeneralStatementTestCase(WorkStatementAPITestCase):

	def setUp(self):
		super().setUp()
		self._init_general_statement()

	def tearDown(self):
		self._remove_general_statement()
		super().tearDown()

	def _init_general_statement(self):
		for general_statement_data in DEFAULT_TEST_GENERAL_STATEMENT_INFO_DATA:
			general_statement = GeneralStatementInfo(**general_statement_data)
			self.db.add(general_statement)
		self.db.commit()
		self.general_statement_info = self.db.query(GeneralStatementInfo).all()

	def _remove_general_statement(self):
		for general_statement_data in self.general_statement_info:
			self.db.delete(general_statement_data)
		self.db.commit()
		self.general_statement_info = []

