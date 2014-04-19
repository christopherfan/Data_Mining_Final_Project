###
# Processes raw CSV rows into aggegated Tuples per Parking person
###

import csv
from datetime import datetime
######
# returns iterable object for CSV data 

######
def convertCSV():
	with open('violations.csv', 'rb') as csvfile:
		# file_reader = csv.reader(csvfile, delimeter = ',')
		dialect = csv.Sniffer().sniff(csvfile.read(1024))
		csvfile.seek(0)
		outfile  = open('ttest.csv', "wb")
		writer = csv.writer(outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
		file_reader = csv.reader(csvfile, dialect)		
		for row in file_reader:
			print ">>>>>>>", row
			convertRow = extractFields(row)
			# write.writerow(covertRow)

	outfile.close()
###

########## extractFields():
# extractFields(row) 
# Takes a row of csv data and returns specific fields
##########
def extractFields(row):
	# answer = {'954543_01022014':{'violation_category': 40, 'time': '1030A', 'address':'1777 PITKIN AVE'}}
	print "Input Row: ", row[0]
	issuerCode = row[16]
	date = row[4]	
	violation_category = row[5]
	time = row[19]
	address = row[23] + " " + row[24]
	# print issuerCode, date , time,  violation_category, address
	return_row = [issuerCode, date, time, violation_category, address]
	print "Convert Row: ", return_row
	return return_row



###############################
# Map a Violation Code to Pre-Set Violation Category
# (1) parking during street cleaning hours, the single most common violation
# (2) stopping, standing, or parking in illegal areas, or at certain hours; 
# (3) parking in illegal ways or blocking access or traffic (e.g., double parking, parking the wrong way or at an angle); 
# (4) parking beyond the time allowed by regulation or by the meter; and 
# (5) parking without proper registration, documentation, or with damaged license plates, etc.
# (6) Everything else
##############################
def assignCategory(violation_number):

	return 5
	
###
	# assignTime takes in a string representation of time and assigns to following categories
###

def assignTimeCategory(time_string):
	time_number= calculateTimeFromString(time_string)
	
	if(time_number < 900 and time_number >=600):
		return 1
	elif(time_number<1200 and time_number >=900):
		return 2
	elif(time_number <1500 and time_number >=1200):
		return 3
	elif(time_number <1800 and time_number >=1500):
		return 4	
	return 0

###	
# Generates Numerical representation of time 00:00 to 24:00
###
def calculateTimeFromString(time_string):
	ampm = time_string[4]
	time_num = int(time_string[0:4])	
	if (ampm =='A'):
		return time_num
	elif (ampm =='P'):
		if(time_num >=1200 and time_num <1260):
			return time_num
		else:
			return time_num + 1200

####
# transformDate(date)
####			
def transformDate(datestring):
	dt = datetime.strptime(datestring, '%Y-%m-%d %H:%M:%S')
	

if __name__ == '__main__':
	convertCSV()
	# print calculateTimeFromString('0200P')
	# row =	['1358044703', 'FPE1082', 'NY', '999', '01/02/2014', '40', 'SDN', 'ACURA', 'P', '70930', '89970', '82230', '20150612', '0073', '73', '165', '954543', '0165', '0000', '1030A', '', '', 'F', '1777', 'PITKIN AVE', '', '0', '408', 'E2', '', 'BBBBBBB', 'ALL', 'ALL', 'GOLD', '0', '2006', '-', '6', '', '', '', '', '']
	# extractFields(row)		