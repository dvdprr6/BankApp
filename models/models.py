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

	id = Column(Integer, primary_key=True, nullable=False)
	rate = Column(Float, nullable=False)
	hours = Column(Float, nullable=False)
	company_name = Column(Float, nullable=False)
	payment_date = Column(DateTime, default=datetime.datetime.utcnow)

	earnings_deductions_association = relationship("EarningsDeductionAssociation", cascade="save-update, merge, delete, delete-orphan")

	def to_dict(self):
		return{
			'id':self.id,
			'rate':self.rate,
			'hours':self.hours,
			'company_name':self.company_name,
			'payment_date':seld.payment_date
		}

class EarningsAssociation(Base):

	__tablename__ = 'earnings_association'

	id = Column(Integer, primary_key=True, nullable=False)
	earnings_ytd_id = Column(Integer, ForeignKey('ytd_earnings.id', ondelete="CASCADE"),
							 primary_key=True, nullable=False)
	earnings_id = Column(Integer, ForeignKey('earnings.id', ondelete="CASCADE"),
						 primary_key=True, nullable=False)

	ytd_earnings = relationship('YTDEarnings')
	earnings = relationship('Earnings')

	def to_dict(self):
		return{
			'id':self.id,
			'earnings_ytd_id':self.earnings_ytd_id,
			'earnings_id':self.earnings_id
		}


class YTDEarnings(Base):

	__tablename__ = 'ytd_earnings'

	id = Column(Integer, primary_key=True, nullable=False)
	ytd_hours = Column(Float, nullable=False)
	ytd_amount = Column(Float, nullable=False)

	earnings_association = relationship("EarningsAssociation", cascade="save-update, merge, delete, delete-orphan")

	def to_dict(self):
		return{
			'id': self.id,
			'ytd_hours': self.ytd_hours,
			'ytd_amount':self.ydt_amount
		}

class Earnings(Base):

	__tablename__ = 'earnings'

	id = Column(Integer, primary_key=True, nullable=False)
	amount = Column(Float, nullable=False)
	less_taxable_benefits = Column(Float, default=0.00, nullable=False)
	total_gross = Column(Float, nullable=False)

	earnings_association = relationship("EarningsAssociation", cascade="save-update, merge, delete, delete-orphan")

	def to_dict(self):
		return{
			'id':self.id,
			'amount':self.amount,
			'less_taxable_benefits':self.less_taxable_benefits,
			'total_gross':self.total_gross
		}

class EarningsDeductionsAssociation(Base):

	__tablename__ = 'earnings_deductions_association'

	# id = Column(Integer, primary_key=True, nullable=False)
	earnings_association_id = Column(Integer, ForeignKey('earnings_association.id', ondelete="CASCADE"),
									 primary_key=True, nullable=False)
	deductions_association_id = Column(Integer, ForeignKey('deductions_association.id', ondelete="CASCADE"), 
										primary_key=True, nullable=False)
	general_statement_info_id = Column(Integer, ForeignKey('general_statement_info.id', ondelete="CASCADE"), 
										primary_key=True, nullable=False)

	earnings_association = relationship('EarningsAssociation')
	deductions_association = relationship('DeductionsAssociation')
	general_statement_info = relationship('GeneralStatementInfo')


class DeductionsAssociation(Base):

	__tablename__ = 'deductions_association'

	id = Column(Integer, primary_key=True, nullable=False)
	deductions_ytd_id = Column(Integer, ForeignKey('ytd_deductions.id', ondelete="CASCADE"),
								primary_key=True, nullable=False)
	deductions_id = Column(Integer, ForeignKey('deductions.id', ondelete="CASCADE"),
							primary_key=True, nullable=False)

	ytd_deductions = relationship('YTDDeductions')
	deductions = relationship('Deductions')

class YTDDeductions(Base):

	__tablename__ = 'ytd_deductions'

	id = Column(Integer, primary_key=True, nullable=False)
	government_pension = Column(Float, nullable=False)
	federal_tax = Column(Float, nullable=False)
	qpip = Column(Float, nullable=False)
	employment_insurance_contriution = Column(Float, nullable=False)
	provencial_tax = Column(Float, nullable=False)

	deductions_association = relationship("DeductionsAssociation", cascade="save-update, merge, delete, delete-orphan")

	def to_dict(self):
		return{
			'id':self.id,
			'government_pension':self.government_pension,
			'federal_tax':self.federal_tax,
			'qpip':self.qpip,
			'employment_insurance_contriution':self.employment_insurance_contriution,
			'provencial_tax':self.provencial_tax
		}

class Deductions(Base):

	__tablename__ = 'deductions'

	id = Column(Integer, primary_key=True, nullable=False)
	government_pension = Column(Float, nullable=False)
	federal_tax = Column(Float, nullable=False)
	qpip = Column(Float, nullable=False)
	employment_insurance_contriution = Column(Float, nullable=False)
	provencial_tax = Column(Float, nullable=False)

	deductions_association = relationship("DeductionsAssociation", cascade="save-update, merge, delete, delete-orphan")

	def to_dict(self):
		return{
			'id':self.id,
			'government_pension':self.government_pension,
			'federal_tax':self.federal_tax,
			'qpip':self.qpip,
			'employment_insurance_contriution':self.employment_insurance_contriution,
			'provencial_tax':self.provencial_tax
		}


