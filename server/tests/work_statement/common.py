import json

from tornado.web import BaseAppTestCase

from bank.db.models import GeneralStatementInfo

DEFAULT_GENERAL_STATEMENT_INFO = {
	'rate':23.00,
	'hours':80.00,
	'company_name':'Nuance',
	'payment_date':'2014-05-20'
}

class BankStatementAPITestCase(BaseAppTestCase):

	def setUp(self):
		super().setUp()

	def tearDown(self):
		super().tearDown()

	@property
	def db(self):
		return self.get_app().db