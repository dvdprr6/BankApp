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

	earnings_deductions_association = relationship("EarningsDeductionsAssociation",
										  cascade="save-update, merge, delete, delete-orphan")


	def to_dict(self):
		return{
			'id':self.id,
			'rate':self.rate,
			'hours':self.hours,
			'company_name':self.company_name,
			'payment_date':self.payment_date
		}

class EarningsDeductionsAssociation(Base):

	__tablename__ = 'earnings_deductions_associations'

	earnings_association_id = Column(Integer, ForeignKey('earnings_associations.id'), primary_key=True, nullable=False)
	deductions_association_id = Column(Integer, ForeignKey('deductions_associations.id'), primary_key=True, nullable=False)
	general_statement_info_id = Column(Integer, ForeignKey('general_statement_information.id'), primary_key=True, nullable=False)

	general_statement_information = relationship("GeneralStatementInfo")
	deductions_association = relationship("DeductionsAssociation")
	earnings_association = relationship("EarningsAssociation")

	def to_dict(self):
		return{
			'earnings_association_id':self.earnings_association_id,
			'deductions_association_id':self.deductions_association_id,
			'general_statement_info_id':self.general_statement_info_id
		}


class DeductionsAssociation(Base):

	__tablename__ = 'deductions_associations'

	id = Column(Integer, primary_key=True, nullable=False)
	deductions_ytd_id = Column(Integer, ForeignKey('ytd_deductions.id'), primary_key=True, nullable=False)
	deductions_id = Column(Integer, ForeignKey('deductions.id'), primary_key=True, nullable=False)

	earnings_deductions_association = relationship("EarningsDeductionsAssociation",
										  cascade="save-update, merge, delete, delete-orphan")

	ytd_deductions = relationship("YTDDeductions")
	deductions = relationship("Deductions")

	def to_dict(self):
		return{
			'id':self.id,
			'deductions_ytd_id':self.deductions_ytd_id,
			'deductions_id':self.deductions_id
		}


class YTDDeductions(Base):

	__tablename__ = 'ytd_deductions'

	id = Column(Integer, primary_key=True, nullable=False)
	government_pension = Column(Float, nullable=False)
	federal_tax = Column(Float, nullable=False)
	qpip = Column(Float, nullable=False)
	ei_contribution = Column(Float, nullable=False)
	provencial_tax = Column(Float, nullable=False)

	deductions_association = relationship("DeductionsAssociation",
										  cascade="save-update, merge, delete, delete-orphan")

	def to_dict(self):
		return{
			'id':self.id,
			'government_pension':self.government_pension,
			'federal_tax':self.federal_tax,
			'qpip':self.qpip,
			'ei_contribution':self.ei_contribution,
			'provencial_tax':self.provencial_tax
		}

class Deductions(Base):

	__tablename__ = 'deductions'

	id = Column(Integer, primary_key=True, nullable=False)
	government_pension = Column(Float, nullable=False)
	federal_tax = Column(Float, nullable=False)
	qpip = Column(Float, nullable=False)
	ei_contribution = Column(Float, nullable=False)
	provencial_tax = Column(Float, nullable=False)

	deductions_association = relationship("DeductionsAssociation",
										  cascade="save-update, merge, delete, delete-orphan")

	def to_dict(self):
		return{
			'id':self.id,
			'government_pension':self.government_pension,
			'federal_tax':self.federal_tax,
			'qpip':self.qpip,
			'ei_contribution':self.ei_contribution,
			'provencial_tax':self.provencial_tax
		}

class EarningsAssociation(Base):

	__tablename__ = 'earnings_associations'

	id = Column(Integer, primary_key=True, nullable=False)
	earnings_ytd_id = Column(Integer, ForeignKey('ytd_earnings.id'), primary_key=True, nullable=False)
	earnings_id = Column(Integer, ForeignKey('earnings.id'), primary_key=True, nullable=False)

	earnings_deductions_association = relationship("EarningsDeductionsAssociation",
										  cascade="save-update, merge, delete, delete-orphan")


	ytd_earnings = relationship("YTDEarnings")
	earnings = relationship("Earnings")

	def to_dict(self):
		return{
			'id':self.id,
			'earnings_ytd_id':self.earnings_ytd_id,
			'earnings_id':self.earnings_id
		}

class YTDEarnings(Base):

	__tablename__ = 'ytd_earnings'

	id = Column(Integer, primary_key=True, nullable=False)
	hours = Column(Float, nullable=False)
	amount = Column(Float, nullable=False)

	earnings_association = relationship("EarningsAssociation",
										cascade="save-update, merge, delete, delete-orphan")

	def to_dict(self):
		return{
			'id':self.id,
			'hours':self.hours,
			'amount':self.amount
		}

class Earnings(Base):

	__tablename__ = 'earnings'

	id = Column(Integer, primary_key=True, nullable=False)
	amount = Column(Float, nullable=False)
	less_taxable_benefits = Column(Float, nullable=False)
	total_gross = Column(Float, nullable=False)

	earnings_association = relationship("EarningsAssociation",
										cascade="save-update, merge, delete, delete-orphan")

	def to_dict(self):
		return{
			'id':self.id,
			'amount':self.amount,
			'less_taxable_benefits':self.less_taxable_benefits,
			'total_gross':self.total_gross
		}