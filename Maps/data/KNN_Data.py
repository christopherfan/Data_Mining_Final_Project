import csv
import json
from json import *

def generateJSONfromCSV(sourcefile, outfile):
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
			print row[5]

def generateTimeNumber(timestring):
	hour = int(timestring[0:2])
	minute = int(timestring[3:5])
	return hour*60 + minute
if __name__ == '__main__':
	generateJSONfromCSV('knn_geocodes.csv', 'jsonAddress.json')