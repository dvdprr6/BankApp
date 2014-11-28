import logging
import datetime
import hashlib

from sqlalchemy import (create_engine, Table, Column, Integer, 
						BigInteger, String, DateTime, Text, Boolean, 
						Float, ForeignKey, desc)
from sqlalchemy.orm import relationship, column_property, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class GeneralStatementInfo(Base):

	__tablename__ = 'general_statement_information'

	id = Column(Integer, primary_key=True, nullable=False)
	rate = Column(Float, nullable=False)
	hours = Column(Float, nullable=False)
	company_name = Column(String(255))
	payment_date = Column(DateTime, default=datetime.datetime.utcnow)

	def to_dict(self):
		return{
			'id':self.id,
			'rate':self.rate,
			'hours':self.hours,
			'company_name':self.company_name,
			'payment_date':self.payment_date
		}