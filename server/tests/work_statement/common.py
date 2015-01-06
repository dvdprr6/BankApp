import json
import datetime

from tornado.web import create_signed_value

from tests.core import BaseAppTestCase
from bank.db.models import GeneralStatementInfo

TEST_GENERAL_STATEMENT_INFO_DATA = {
	'rate':23.00,
	'hours':80.00,
	'company_name':'Nuance',
	'payment_date':datetime.date(2014, 5, 20)
}

GENERAL_STATEMENT_INFO_RETURN_ATTRIBUTES = [
	'rate',
	'hours',
	'company_name',
	'payment_date'
]

ENDPOINTS = {
	'home':'/work_statement/',
	'general_statement_info':'/work_statement/general_statement_info/'
}

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

	def retrieve_dictionary_keys(self, key_list):
		key_values = []
		for key in key_list:
			key_values.append(key)
		return key_values

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

