import logging
import json

import tornado
import tornado.gen

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

	def exit_with_success(self, status_code, success_message):
		self.set_status(status_code)
		self.write(success_message)
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

	def check_post_status_code(self, status_code, message, error_to_log):
		if status_code == 500 and error_to_log is not None:
			self.exit_with_error(status_code, message, error_to_log)
		elif status_code == 201 and error_to_log is None:
			self.exit_with_success(status_code, message)
		

class MainHandler(BaseRequestHandler):
	@tornado.web.asynchronous
	def get(self):
		self.set_status(200)
		self.write("hello, world")
		self.finish()

class GeneralStatementInfoHandler(WorkStatementRequestHandler):

	@tornado.web.asynchronous
	def post(self):
		general_statement_info_data = self.request_body
		field_keys = [
			'rate',
			'hours',
			'company_name'
		]

		field_keys = self._append_option_payment_date(field_keys, general_statement_info_data)

		(code, message) = self.check_field_keys(field_keys, general_statement_info_data)
		
		if code == 400:
			self.exit_with_error(code, message)
		else:
			(code, message, exception_message) = self._add_general_statement_info(general_statement_info_data)
			self.check_post_status_code(code, message, exception_message)
	
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

	def _general_statement_info_response_JSON(self, general_statement_info):
		response_body = {'data':[]}
		response_body['data'].append(general_statement_info.to_dict())
		return response_body

	def _append_option_payment_date(self, field_keys, general_statement_info_data):
		if 'payment_date' in general_statement_info_data:
			field_keys.append('payment_date')

		return field_keys