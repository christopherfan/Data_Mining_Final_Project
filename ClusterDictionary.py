import csv
from datetime import datetime
import collections
import itertools

class ClusterDictionary:

	dict = {}
########## contains()
	def __init__(self):
		self.dict = {}
##########	
	def contains(self,issuer_id):
		return issuer_id in self.dict
				

########## addNewEntry(issuer_id)
	def addNewEntry(self, issuer_id):
		default_entry = ClusterDictionary.createDefaultEntryToClusterDict()
		self.dict[issuer_id] =default_entry
########## addNewEntry(issuer_id)
	
########## createDefaultEntryClusterDict()
# Creates a ordered dictionary of 6 Violation Categories {0-5} by 12 time categories {0-11} with default value 0
# Returns the Ordered Dictionary
##########
	@staticmethod
	def createDefaultEntryToClusterDict():
		entry = collections.OrderedDict()
		for violation_category in xrange(1,7):
			for time_category in xrange(1,13):
				entry_key = str(violation_category) +'_'+ str(time_category)
				# print entry_key
				entry[entry_key]= 0
		return entry
########## createDefaultEntryClusterDict()

########## createDefaultEntryClusterDict()
# Creates a ordered dictionary of 6 Violation Categories {0-5} by 12 time categories {0-11} with default value 0
# Returns the Ordered Dictionary
##########
	@staticmethod
	def createDefaultEntryToClusterDictAbstract(feature_array):
		entry = collections.OrderedDict()
		feature_vector = ClusterDictionary.generateHeaders(feature_array)
		for feature in feature_vector:			
				entry_key = feature				
				entry[entry_key]= 0
		return entry
		
	@staticmethod
	def generateHeaders(feature_array):
		arguments_array = []
		for item in feature_array:
			arguments_array.append(range(1,item+1))
		print arguments_array
		return itertools.product(*arguments_array)
			
########## createDefaultEntryClusterDict()

########## getItems(Issuer_id)
	def getItems(self, issuer_id):
		if(self.contains(issuer_id)):
			return self.dict[issuer_id].items()
		else: 
			return False
########## getItems(Issuer_id)

########## getItems(Issuer_id)
	def getValues(self, issuer_id):
		if(self.contains(issuer_id)):
			return self.dict[issuer_id].values()
		else: 
			return False
########## getItems(Issuer_id)

########## getItems(Issuer_id)
	def getIssuerSpecificItem(self, issuer_id, item):
		if(self.contains(issuer_id)):
			return self.dict[issuer_id][item]
		else: 
			return False
########## getItems(Issuer_id)

########## incrementIssuerItem(self, issuer_id,item)
	def incrementIssuerItem(self, issuer_id, item):
		if self.contains(issuer_id):
			self.dict[issuer_id][item] +=1
		return False
########## incrementIssuerItem(self, issuer_id,item)

########## incrementIssuerItem(self, issuer_id,item)
	def addToIssuerItem(self, issuer_id, item, number):
		if self.contains(issuer_id):
			self.dict[issuer_id][item] +=number
		return False
########## incrementIssuerItem(self, issuer_id,item)

########## exportCSV(self)
	def exportCSV(self, file_name):
		with open(file_name, 'wb') as outfile:
			# file_reader = csv.reader(csvfile, delimeter = ',')						
			writer = csv.writer(outfile, delimiter=',')
			# Create Headers
			headers =['Issuer_id']
			for violation_category in xrange(1,7):
				for time_category in xrange(1,13):
					violation_time_entry = str(violation_category) +'_'+ str(time_category)
					# print violation_time_entry
					headers.append(violation_time_entry)
			# print headers
			writer.writerow(headers)
			for people in self.dict.keys():			
				entry = []
				entry.append(people)
				values = self.getValues(people)
				entry +=values
				writer.writerow(entry)					
		return True
########## exportCSV(self)

########## convertCSVRow(self, csv_input)
	@staticmethod
	def convertCSVRow(csv_input):
		issuer_id = csv_input[0]
		violation_category = csv_input[1]
		time_category = csv_input[2]
		violation_time = str(violation_category)+'_'+str(time_category)		
		total = int(csv_input[3])
		converted_row = {'issuer_id':issuer_id, 'violation_time':violation_time, 'total': total} 
		return converted_row

########## convertCSVRow(self, csv_input)

########## importCSV(self)
	def importCSV(self, filename):
		with open(filename, 'rb') as csvfile:
			# file_reader = csv.reader(csvfile, delimeter = ',')
			dialect = csv.Sniffer().sniff(csvfile.read(1024))
			csvfile.seek(1)					
			file_reader = csv.reader(csvfile, dialect)		
			firstline = True
			for row in file_reader:
				if firstline:
					firstline = False
					continue
				entry = ClusterDictionary.convertCSVRow(row)
				if(self.contains(entry['issuer_id'])):
					self.addToIssuerItem(entry['issuer_id'], entry['violation_time'], entry['total'])
				else:
					self.addNewEntry(entry['issuer_id'])
					self.addToIssuerItem(entry['issuer_id'], entry['violation_time'], entry['total'])
		# self.addNewEntry('301011')
		# self.addToIssuerItem('301011', '3_10',11)
########## importCSV(self)

if __name__ == '__main__':
	# print ClusterDictionary.createDefaultEntryToClusterDict()
	# cluster_results = ClusterDictionary()
	# cluster_results.importCSV('tim/violations_top_performers_grouped.csv')
	# cluster_results.exportCSV('ClusterData/cluster_data.csv')
	for stuff in ClusterDictionary.generateHeaders([2,3,2]):
		print stuff