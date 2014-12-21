import json

from bank.db.models import GeneralStatementInfo
from .common import WorkStatementAPITestCase
from .common import (
	ENDPOINTS, 
	TEST_GENERAL_STATEMENT_INFO_DATA, 
	GENERAL_STATEMENT_INFO_RETURN_ATTRIBUTES
)

class TestWorkStatementHome(WorkStatementAPITestCase):
	'''Standard cases on /work_statement/'''

	def test_work_statement_home(self):
		request_url = ENDPOINTS['home']
		response = self.fetch(request_url, method='GET')
		self.assertEqual(response.code, 200)

class TestGeneralStatementInfo(WorkStatementAPITestCase):
	'''Standard cases on /work_statement/general_statement_info/'''

	def test_post_general_statement_info(self):
		request_url = ENDPOINTS['general_statement_info']
		general_statement_info_data = TEST_GENERAL_STATEMENT_INFO_DATA
		keys = GENERAL_STATEMENT_INFO_RETURN_ATTRIBUTES
		response = self.fetch_request(request_url, method='POST', body=json.dumps(general_statement_info_data))
		g_query = self.db.query(GeneralStatementInfo).filter_by(company_name=general_statement_info_data['company_name'])
		response_list = self.convert_byte_string_to_JSON(response)['data']
		response_returned = self.retrieve_dictionary_keys(response_list[0].keys())
		response_expected = self.retrieve_dictionary_keys(g_query.first().to_dict().keys())
		self.assertEqual(response.code, 201)
		self.assertEqual(
			sorted(response_returned),
			sorted(response_expected)
		)
		self.db.delete(g_query.first())
		self.db.commit()


