import logging
import datetime
import hashlib

from sqlalchemy import (create_engine, Table, Column, Integer, BigInteger,
						String, DateTime, Text, Boolean, Float,
						ForeignKey, desc)
from sqlalchemy.orm import relationship, column_property, backref
from sqlalchemy.ext.declarative import declarative_base

log = logging.getLogger(__name__)

Base = declarative_base()

class GeneralStatementInfo(Base):

	__tablename__ = 'general_statement_info'

	id = Column(Integer, primary_key=True)
	rate = Column(String(55))
	hours = Column(String(55))
	company_name = Column(String(255))
	payment_date = Column(DateTime, default=datetime.datetime.utcnow)

	# earnings_deductions_association = relationship("EarningsDeductionAssociation",
	# 												cascade="save-update, merge, delete, delete-orphan")

	def to_dict(self):
		return{
			'id':self.id,
			'rate':self.rate,
			'hours':self.hours,
			'company_name':self.company_name,
			'payment_date':seld.payment_date
		}
