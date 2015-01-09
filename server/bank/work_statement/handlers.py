import logging
import json

import tornado
import tornado.gen

from collections import OrderedDict

from tornado.web import HTTPError
from sqlalchemy.exc import SQLAlchemyError

from ..db.models import GeneralStatementInfo
from ..handlers import BaseRequestHandler

log = logging.getLogger(__name__)

class WorkStatementRequestHandler(BaseRequestHandler):

	def exit_with_error(self, status_code, error_message, error_to_log=None):
		if error_to_log:
			log.error(error_to_log)
		self.set_status(status_code)
		self.write(
			{
				'error':{
					'message': error_message
				}
			}
		)
		self.finish()

	def prepare(self):
		if self.request.body:
			try:
				self.request_body = json.loads(self.request.body.decode('utf-8'))
			except ValueError as ex:
				self.exit_with_error(400, 'Bad Request: Invalid JSON', ex)

	def check_field_keys(self, field_keys, data):
		code = None
		error_message = None
		for key in field_keys:
			if not key in data:
				error_message = 'Bad Request: Missing attribute: {0}'.format(key)
				code = 400
		return code, error_message

	def check_exit_status(self, status_code, message, error_to_log):
		if status_code == 500 and error_to_log is not None:
			self.exit_with_error(status_code, message, error_to_log)
		elif status_code == 201 and error_to_log is None:
			self._exit_with_success(status_code, message)
		elif status_code == 200 and error_to_log is None:
			self._exit_with_success(status_code, message)
		
	def _exit_with_success(self, status_code, success_message):
		self.set_status(status_code)
		self.write(success_message)
		self.finish()

class MainHandler(WorkStatementRequestHandler):
	
	@tornado.web.asynchronous
	def get(self):
		(code, message, exception_message) = self._get_years_and_companies()
		self.check_exit_status(code, message, exception_message)

	def _get_years_and_companies(self):
		ex = None
		try:
			general_statement_info_data = self.db.query(GeneralStatementInfo).all()
			message = self._all_years_and_companies_response_JSON(general_statement_info_data)
			code = 200
		except SQLAlchemyError as ex:
			message = 'Interal Server Error: Unable to get dates'
			code = 500
			return code, message, ex

		return code, message, ex

	def _all_years_and_companies_response_JSON(self, general_statement_info_data):
		response_body = {
			'data':{
				'years': self._get_years(general_statement_info_data),
				'companies':self._get_companies(general_statement_info_data)
			}
		}

		return response_body

	def _get_years(self, general_statement_info_all_dates):
		years = []

		for year in general_statement_info_all_dates:
			years.append(year.to_dict_return_dates())

		return list(OrderedDict.fromkeys(years))

	def _get_companies(self, general_statement_info_all_companies):
		companies = []

		for company in general_statement_info_all_companies:
			companies.append(company.to_dict_return_companies())

		return list(OrderedDict.fromkeys(companies))

class GeneralStatementInfoHandler(WorkStatementRequestHandler):

	@tornado.web.asynchronous
	def post(self):
		general_statement_info_data = self.request_body
		field_keys = [
			'rate',
			'hours',
			'company_name',
			'payment_date'
		]

		(code, message) = self.check_field_keys(field_keys, general_statement_info_data)
		
		if code == 400:
			self.exit_with_error(code, message)
		else:
			(code, message, exception_message) = self._add_general_statement_info(general_statement_info_data)
			self.check_exit_status(code, message, exception_message)
	
	def _add_general_statement_info(self, general_statement_info_data):
		ex = None
		
		try:
			general_statement_info = GeneralStatementInfo(**general_statement_info_data)
			self.db.add(general_statement_info)
			self.db.commit()
			message = self._general_statement_info_response_JSON(general_statement_info)
			code = 201
		except SQLAlchemyError as ex:
			message = 'Internal Server Error: Unable to create general statement info'
			code = 500
			return code, message, ex
		
		return code, message, ex

	def _general_statement_info_response_JSON(self, general_statement_info):
		response_body = {
			'data':{
				'general_statement_info': general_statement_info.to_dict()
			}
		}
		return response_body