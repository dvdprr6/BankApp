import logging
import datetime
import hashlib

from sqlalchemy import create_engine, Table, Column, Integer, BigInteger, String, DateTime, Text, Boolean, Float, ForeignKey, desc
from sqlalchemy.orm import relationship, column_property, backref
from sqlalchemy.ext.declarative import declarative_base

log = logging.getLogger(__name__)

Base = declarative_base()

class GeneralStatementInfo(Base):
	__tablename__ = 'general_statement_info'

	id = Column(Integer, primary_key=True)
	company_name_id = Column(Integer, ForeignKey('companies.id'))
	date_id = Column(Integer, ForeignKey('dates.id'))
	rate = Column(String(55))
	hours = Column(String(55))

	companyName = relationship("Company");
	date = relationship("Date")

	date = relationship("Date", backref=backref('general_statement_info', order_by=id))

class Company(Base):
	__tablename__ = 'companies'

	id = Column(Integer, primary_key=True)
	name = Column(String(255))

	general_statement_info = relationship("GeneralStatementInfo", cascade="save-update, merge, delete, delete-orphan")

class Date(Base):
	__tablename__ = 'dates'

	id = Column(Integer, primary_key=True)
	# TODO: set the date_value to proper date format
	#date_value = Column(String(255))
	date_value = Column(DateTime, default=datetime.datetime.utcnow)

	generalStatementInfo = relationship("GeneralStatementInfo", cascade="save-update, merge, delete, delete-orphan")
