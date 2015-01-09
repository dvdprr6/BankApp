import json
import datetime

from bank.db.models import GeneralStatementInfo
from .common import (
	WorkStatementAPITestCase, 
	InitializeGeneralStatementTestCase
)
from .test_data import (
	ENDPOINTS, 
	TEST_GENERAL_STATEMENT_INFO_DATA, 
	GENERAL_STATEMENT_INFO_RETURN_ATTRIBUTES,
	DEFAULT_TEST_WORK_STATEMENT_HOME_RETURN_ATTRIBUTES
)

# solves the issue of the date can't be json serialized
def serialize_date(obj):
	if isinstance(obj, datetime.datetime):
		serial = obj.isoformat()
		return serial

class TestWorkStatementHome(InitializeGeneralStatementTestCase):
	'''Standard cases on /work_statement/'''

	def test_work_statement_home(self):
		request_url = ENDPOINTS['home']
		expected_response_list_years = DEFAULT_TEST_WORK_STATEMENT_HOME_RETURN_ATTRIBUTES['years']
		expected_response_list_companies = DEFAULT_TEST_WORK_STATEMENT_HOME_RETURN_ATTRIBUTES['companies']
		response = self.fetch(request_url, method='GET')
		self.assertEqual(response.code, 200)
		returned_response_list_years = self.convert_byte_string_to_JSON(response)['data']['years']
		returned_response_list_companies = self.convert_byte_string_to_JSON(response)['data']['companies']
		self.assertEqual(
			sorted(returned_response_list_years),
			sorted(expected_response_list_years)
		)
		self.assertEqual(
			sorted(returned_response_list_companies),
			sorted(expected_response_list_companies)
		)

class TestGeneralStatementInfo(WorkStatementAPITestCase):
	'''Standard cases on /work_statement/general_statement_info/'''

	def test_post_general_statement_info(self):
		request_url = ENDPOINTS['general_statement_info']
		general_statement_info_data = TEST_GENERAL_STATEMENT_INFO_DATA
		keys = GENERAL_STATEMENT_INFO_RETURN_ATTRIBUTES
		response = self.fetch_request(
			request_url, 
			method='POST', 
			body=json.dumps(general_statement_info_data, default=serialize_date)
		)
		self.assertEqual(response.code, 201)
		g_query = self.db.query(GeneralStatementInfo).filter_by(
			company_name=general_statement_info_data['company_name']
		)
		response_expected = list(g_query.first().to_dict().keys())
		self.db.delete(g_query.first())
		self.db.commit()
		response_list = self.convert_byte_string_to_JSON(response)['data']['general_statement_info']
		response_returned = list(response_list.keys())
		self.assertEqual(
			sorted(response_returned),
			sorted(response_expected)
		)
