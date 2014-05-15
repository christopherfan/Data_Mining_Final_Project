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
			address = row[6]+ " "+row[7]+ " " + row[8]
			json_answer[summons] = {'date':date, 'violation': violation, 'time': time, 'address': address }
	with open(outfile, 'w') as outfile:
		json.dump(json_answer, outfile)		
				
if __name__ == '__main__':
	generateJSONfromCSV('Addresses.csv', 'jsonAddres.txt')