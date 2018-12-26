class ExcelVariable:
	caseID = 0
	url = 2
	request_data = 3
	expect = 4
	result = 5

def getCaseID():
	return ExcelVariable.caseID

def getUrl():
	return ExcelVariable.url

def get_request_data():
	return ExcelVariable.request_data

def get_expect():
	return ExcelVariable.expect

def get_result():
	return ExcelVariable.result