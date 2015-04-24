import json
import datetime

TEST_GENERAL_STATEMENT_INFO_DATA = {
	'rate':23.00,
	'hours':80.00,
	'company_name':'Nuance',
	'payment_date':datetime.date(2014, 5, 20)
}

TEST_INVALID_GENERAL_STATEMENT_INFO_DATA = {
	'fate':23.00,
	'nours':80.00,
	'date':datetime.date(2014, 4, 20)
}

DEFAULT_TEST_GENERAL_STATEMENT_INFO_DATA = [
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2011, 1, 15)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2011, 1, 30)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2011, 2, 15)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2011, 2, 28)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2011, 3, 15)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2011, 3, 30)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2011, 4, 15)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2011, 4, 30)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2011, 5, 15)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2011, 5, 30)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2011, 6, 15)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2011, 6, 30)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2011, 7, 15)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2011, 7, 30)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2011, 8, 15)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2011, 8, 30)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2011, 9, 15)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2011, 9, 30)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2011, 10, 15)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2011, 10, 30)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2011, 11, 15)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2011, 11, 30)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2011, 12, 15)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2011, 12, 30)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2012, 1, 15)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2012, 1, 30)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2012, 2, 15)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2012, 2, 28)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2012, 3, 15)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2012, 3, 30)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2012, 4, 15)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2012, 4, 30)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2012, 5, 15)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2012, 5, 30)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2012, 6, 15)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2012, 6, 30)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2012, 7, 15)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2012, 7, 30)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2012, 8, 15)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2012, 8, 30)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2012, 9, 15)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2012, 9, 30)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2012, 10, 15)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2012, 10, 30)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2012, 11, 15)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2012, 11, 30)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2012, 12, 15)
	},
	{
		'rate':15.00,
		'hours':80.00,
		'company_name':'Longbow Advantage',
		'payment_date':datetime.date(2012, 12, 30)
	},
	{
		'rate':23.00,
		'hours':72.00,
		'company_name':'Nuance Communications Inc.',
		'payment_date':datetime.date(2014, 6, 13)
	},
	{
		'rate':23.00,
		'hours':80.00,
		'company_name':'Nuance Communications Inc.',
		'payment_date':datetime.date(2014, 6, 30)
	},
	{
		'rate':23.00,
		'hours':120.00,
		'company_name':'Nuance Communications Inc.',
		'payment_date':datetime.date(2014, 7, 15)
	},
	{
		'rate':23.00,
		'hours':80.00,
		'company_name':'Nuance Communications Inc.',
		'payment_date':datetime.date(2014, 7, 31)
	},
	{
		'rate':23.00,
		'hours':80.00,
		'company_name':'Nuance Communications Inc.',
		'payment_date':datetime.date(2014, 8, 15)
	},
	{
		'rate':23.00,
		'hours':80.00,
		'company_name':'Nuance Communications Inc.',
		'payment_date':datetime.date(2014, 8, 29)
	},
	{
		'rate':23.00,
		'hours':80.00,
		'company_name':'Nuance Communications Inc.',
		'payment_date':datetime.date(2014, 9, 15)
	},
	{
		'rate':23.00,
		'hours':120.00,
		'company_name':'Nuance Communications Inc.',
		'payment_date':datetime.date(2014, 9, 30)
	},
	{
		'rate':23.00,
		'hours':80.00,
		'company_name':'Nuance Communications Inc.',
		'payment_date':datetime.date(2014, 10, 15)
	},
	{
		'rate':23.00,
		'hours':80.00,
		'company_name':'Nuance Communications Inc.',
		'payment_date':datetime.date(2014, 10, 31)
	},
	{
		'rate':23.00,
		'hours':80.00,
		'company_name':'Nuance Communications Inc.',
		'payment_date':datetime.date(2014, 11, 14)
	},
	{
		'rate':23.00,
		'hours':80.00,
		'company_name':'Nuance Communications Inc.',
		'payment_date':datetime.date(2014, 11, 28)
	},
	{
		'rate':23.00,
		'hours':80.00,
		'company_name':'Nuance Communications Inc.',
		'payment_date':datetime.date(2014, 12, 15)
	},
	{
		'rate':23.00,
		'hours':80.00,
		'company_name':'Nuance Communications Inc.',
		'payment_date':datetime.date(2014, 12, 14)
	}

]

DEFAULT_TEST_WORK_STATEMENT_HOME_RETURN_ATTRIBUTES = {
	'companies':['Longbow Advantage', 'Nuance Communications Inc.'],
	'years':['2011','2012', '2014']
}

GENERAL_STATEMENT_INFO_RETURN_ATTRIBUTES = [
	'rate',
	'hours',
	'company_name',
	'payment_date'
]

ENDPOINTS = {
	'home':'/work_statement/',
	'general_statement_info':'/work_statement/general_statement_info/'
}