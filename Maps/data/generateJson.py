import csv
import json
from json import *


def generateJSONfromCSV(sourcefile, outfile):
	with open(sourcefile, 'rb') as csvfile:
		# file_reader = csv.reader(csvfile, delimeter = ',')
		dialect = csv.Sniffer().sniff(csvfile.read(1024))
		csvfile.seek(1)					
		file_reader = csv.reader(csvfile, dialect)		
		firstline = True
		json_answer = {}
		for row in file_reader:
			if firstline:
				firstline = False
				continue
			summons = row[0]
			date =row[1]
			violation = row[2]
			time = row[3]
			address = row[4]+ " "+row[5]+ " " + row[6]
			json_answer[summons] = {'date':date, 'violation': violation, 'time': time, 'address': address }
	with open(outfile, 'w') as outfile:
		json.dump(json_answer, outfile)		

def generateLatLongfromCSV(sourcefile, outfile):
	with open(sourcefile, 'rb') as csvfile:
		# file_reader = csv.reader(csvfile, delimeter = ',')
		dialect = csv.Sniffer().sniff(csvfile.read(3024))
		csvfile.seek(1)					
		file_reader = csv.reader(csvfile, dialect)		
		firstline = True
		json_answer = {}
		for row in file_reader:
			if firstline:
				firstline = False
				continue
			summons = row[0]
			date =row[1]
			violation = row[2]
			time = row[5]
			lat = row[16]
			long = row[17]
			json_answer[summons] = {'date':date, 'violation': violation, 'time': time, 'lat':lat, 'long':long }
	with open(outfile, 'w') as outfile:
		json.dump(json_answer, outfile)		

def generateDayLatLongfromCSV(sourcefile, outfile):
	with open(sourcefile, 'rb') as csvfile:
		# file_reader = csv.reader(csvfile, delimeter = ',')
		dialect = csv.Sniffer().sniff(csvfile.read(3024))
		csvfile.seek(1)					
		file_reader = csv.reader(csvfile, dialect)		
		firstline = True
		json_answer = {}
		for row in file_reader:
			if firstline:
				firstline = False
				continue
			summons = row[0]
			date =row[1]
			violation = row[2]
			time = row[5]
			lat = row[16]
			long = row[17]
			day_entry = { 'violation': violation, 'time': time, 'lat':lat, 'long':long }
			if date in json_answer:
				json_answer[date][summons]=day_entry
			else:
				json_answer[date] = {}
				json_answer[date][summons] = day_entry
	with open(outfile, 'w') as outfile:
		json.dump(json_answer, outfile)		

		
if __name__ == '__main__':
	# generateJSONfromCSV('knn_geocodes.csv', 'json_geo.json')
	# generateLatLongfromCSV('knn_geocodes.csv', 'json_geo2.json')
	generateDayLatLongfromCSV('knn_geocodes.csv', 'json_geo2.json')