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
		self.write({'error':{'message':error_message}})
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
		return code, error_message

	def exit_with_success(self, status_code, message):
		self.set_status(status_code)
		if message != None:
			self.write(message)
		self.finish()

class MainHandler(WorkStatementRequestHandler):

	@tornado.web.asynchronous
	def get(self):
		try:
			general_statement_info = self.db.query(GeneralStatementInfo).all()

			response_body = self._get_years_and_companies(general_statement_info)
			code = 200
		except SQLAlchemyError as ex:
			response_body = 'Internal Server Error: Unable to get list of companies and years'
			code = 500

		if code == 200:
			self.exit_with_success(code, response_body)
		elif code == 500:
			self.exit_with_error(code, response_body, ex)


	def _get_years_and_companies(self, general_statement_info):
		years = []
		companies = []

		for year in general_statement_info:
			years.append(year.to_dict_return_dates())

		for company in general_statement_info:
			companies.append(company.to_dict_return_companies())

		response_body = {
			'data':{
				'years': list(OrderedDict.fromkeys(years)),
				'companies': list(OrderedDict.fromkeys(companies))
			}
		}

		return response_body

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

		(code, response_body) = self.check_field_keys(field_keys, general_statement_info_data)
		if code == 400:
			self.exit_with_error(code, response_body)
		else:
			self._add_general_statement_info(general_statement_info_data)

	def _add_general_statement_info(self, general_statement_info_data):
		try:
			general_statement_info = GeneralStatementInfo(**general_statement_info_data)
			self.db.add(general_statement_info)
			self.db.commit()
			code = 201
			request_body = {
				'data':{
					'general_statement_info':general_statement_info.to_dict()
				}
			}
		except SQLAlchemyError as ex:
			request_body = 'Internal Server Error: Unable to create general statement info'
			code = 500

		if code == 201:
			self.exit_with_success(201, request_body)
		elif code == 500:
			self.exit_with_error(code, response_body, ex)