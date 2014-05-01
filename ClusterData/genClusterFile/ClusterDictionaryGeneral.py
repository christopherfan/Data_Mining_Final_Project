import csv
from datetime import datetime
import collections
import itertools

##Trigger Git Push

class ClusterDictionary:

	dict = {}
	features_headers = []
	features_param=[]
########## contains()
	def __init__(self, features_list):
		self.dict = {}
		self.features_param = features_list
		self.features_headers = ClusterDictionary.generateHeaders(features_list)
##########	
	def contains(self,issuer_id):
		return issuer_id in self.dict
				

########## addNewEntry(issuer_id)
	def addNewEntry(self, issuer_id):	
		default_entry = ClusterDictionary.createDefaultEntryToClusterDictAbstract(self.features_param)
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
		features = ClusterDictionary.generateHeaders(feature_array)
		
		for feature in features:
				entry_key = feature				
				entry[entry_key]= 0
		return entry
		
	@staticmethod
	def generateHeaders(feature_array):
		arguments_array = []
		for item in feature_array:
			arguments_array.append(item)
		# print arguments_array
		permutations = itertools.product(*arguments_array)
		string_headers=[]		
		for entry in permutations:
			string_entry = ""
			for index in entry:
				string_entry += str(index) +"_"
			string_headers.append(string_entry)
		return string_headers
			
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
			# for violation_category in xrange(1,7):
				# for time_category in xrange(1,13):
					# violation_time_entry = str(violation_category) +'_'+ str(time_category)
					# # print violation_time_entry
					# headers.append(violation_time_entry)
			headers+=(self.features_headers)
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
	def convertCSVRow(csv_input, numfeatures):
		print csv_input
		for counter in xrange(numfeatures+1):
			if csv_input[counter] == "":
				return False
				
		issuer_id = csv_input[0]		
		features_key = ""
		for count in xrange(1,numfeatures+1):
			features_key +=csv_input[count] +"_"
		key_name = features_key
		total = int(csv_input[numfeatures+1])
		converted_row = {'issuer_id':issuer_id, 'key':key_name, 'value': total} 						
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
				entry = ClusterDictionary.convertCSVRow(row, len(self.features_param))
				
				### Check for blanks
				if entry == False:
					continue		
				### Add to Dictionary
				if self.contains(entry['issuer_id']):					
					self.addToIssuerItem(entry['issuer_id'], entry['key'], entry['value'])
				else:
					# print "New Entry: " , entry['key'], entry['value']
					self.addNewEntry(entry['issuer_id'])
					self.addToIssuerItem(entry['issuer_id'], entry['key'], entry['value'])
		# self.addNewEntry('301011')
		# self.addToIssuerItem('301011', '3_10',11)
########## importCSV(self)

if __name__ == '__main__':
	# print ClusterDictionary.createDefaultEntryToClusterDict()
	dayperiod_violationcategory=[['AM','PM'], range(1,7)]
	dayperiod_violationcode=[['AM','PM'], range(1,100)]
	dayweek_violationcategory =[range(1,8), range(1,7)]
	dayweek_violationcode = [range(1,8), range(1,100)]
	typeday_violationcategory = [['Week','Weekend'], range(1,7)]
	typeday_violationcode = [['Week','Weekend'], range(1,100)]
	threefeaturesA = [range(1,80), ['AM','PM'], [14,38,69,21,37,20,31,16,46,40,47,19,42,71,17]]
	threefeaturesB = [['Week','Weekend'], ['AM','PM'], [14,38,69,21,37,20,31,16,46,40,47,19,42,71,17]]
	cluster_results = ClusterDictionary(threefeaturesB)
	cluster_results.importCSV('csv/3featuresB_forcluster_top_performers.csv')
	cluster_results.exportCSV('clusterfile/3featuresB_forcluster_top_performers_clusterfile.csv')
