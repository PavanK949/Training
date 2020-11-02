#Program to do CRUD operations for any domain

menuFileName = "Menu.cfg"
fieldFileName = "Fields.cfg"
dataFileName = "Data.dat"
updatableFieldsFileName = "updatableFields.cfg"
fileNotFoundMessage = "File Not Found or error in opening the file"

try:
	with open(menuFileName) as fMenuObj:
		menu = fMenuObj.read()
	fMenuObj.close()
except FileNotFoundError:
	print(fileNotFoundMessage)

try:
	with open(fieldFileName) as fFieldObj:
		fieldNames = fFieldObj.readlines()
	fFieldObj.close()
except FileNotFoundError:
	print(fileNotFoundMessage)

try:
	with open(dataFileName, 'r') as fDataObj:
		listOfRecords = fDataObj.readlines();
	fDataObj.close()
except:
	print(fileNotFoundMessage)

for listOfRecord in listOfRecords:
	records = eval(listOfRecord)

def createRecord():
	fieldValues = []
	recordStatus = 'a'
	fieldValues.append(recordStatus)
	for fieldName in fieldNames:
		print(fieldName.rstrip() + ": ", end = "")
		fieldValue = input()
		fieldValues.append(fieldValue)
	records.append(fieldValues)
	writeRecord()
	print("--------------")
	print("The details you entered are saved successfully.")

def readRecords():
	countOfRecords = 0
	for fieldValuesOfRecord in records:
		if fieldValuesOfRecord[0] == 'a':
			index = 1
			for fieldName in fieldNames:
				print(fieldName.rstrip() + ": ", end = "")
				print(fieldValuesOfRecord[index])
				index += 1
			print("--------------")
			countOfRecords += 1
	print("Number Of record(s): " + str(countOfRecords))

def updateRecord():
	printPromptToEnterRecordId()
	idToUpdateRecord = input()
	with open(updatableFieldsFileName, 'r') as fUpdatableFieldsObj:
		listOfUpdatableFields = fUpdatableFieldsObj.readlines()
	fUpdatableFieldsObj.close()
	updateRecordStatus = 0
	for fieldValuesOfRecord in records:
		if fieldValuesOfRecord[0] == 'a' and fieldValuesOfRecord[1] == str(idToUpdateRecord):
			updateRecordStatus = 1
			counter = 1
			for updatableField in listOfUpdatableFields:
				print(str(counter) + "." + " Update " + fieldNames[eval(updatableField) - 1].rstrip())
				counter += 1
			try:
				updateChoice = input("Enter your update choice: ")
				updateChoice = int(updateChoice)
			except Exception:
				print("Invalid Update choice")
			print("Enter new " + fieldNames[eval(listOfUpdatableFields[updateChoice - 1]) - 1].rstrip() + ": ", end = "")
			fieldValuesOfRecord[eval(listOfUpdatableFields[updateChoice - 1])] = input()
			print(fieldNames[eval(listOfUpdatableFields[updateChoice - 1]) - 1].rstrip() + " updated successfully.")
			break
	if updateRecordStatus == 0:
		printRecordNotFound()
	else:
		writeRecord()

def deleteRecord():
	printPromptToEnterRecordId()
	idToDeleteRecord = input()
	deleteRecordStatus = 0
	for fieldValuesOfRecord in records:
		if fieldValuesOfRecord[0] == 'a' and fieldValuesOfRecord[1] == str(idToDeleteRecord):
			deleteRecordStatus = 1
			fieldValuesOfRecord[0] = 'd'
			break
	if deleteRecordStatus == 0:
		printRecordNotFound()
	else:
		writeRecord()
		print("Deleted successfully")

def searchRecord():
	printPromptToEnterRecordId()
	idToSearchRecord = input()
	searchRecordStatus = 0
	for fieldValuesOfRecord in records:
		if fieldValuesOfRecord[0] == 'a' and fieldValuesOfRecord[1] == str(idToSearchRecord):
			searchRecordStatus = 1
			index = 1
			for fieldName in fieldNames:
				print(fieldName.rstrip() + ": ", end = "")
				print(fieldValuesOfRecord[index])
				index += 1
			break
	if searchRecordStatus == 0:
		printRecordNotFound()

def printPromptToEnterRecordId():
	print("Enter " + fieldNames[0].rstrip() + ":", end = "")
def writeRecord():
	try:
		with open(dataFileName, 'w') as fDataObj:
			fDataObj.write(str(records))
		fDataObj.close()
	except:
		print(fileNotFoundMessage)

def printRecordNotFound():
	print(fieldNames[0].rstrip() + " Not found.")

functionsList = [createRecord, readRecords, searchRecord, updateRecord, deleteRecord, exit]

while True:
	print(menu)
	try:
		userChoice = input("Enter you choice: ")
		userChoice = int(userChoice)
		if userChoice == 6:
			print("Entered exit as choice")
		functionsList[userChoice - 1]()
	except Exception:
		print("Invalid Choice")
	print("--------------")