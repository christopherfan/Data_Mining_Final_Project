import unittest 

from  ClusterDictionaryGeneral import *


class ClusterDictionaryTest(unittest.TestCase):
	# Failing Unit Test
	def setUp(self):
		self.dict = ClusterDictionary([range(1,3),range(1,4),range(1,3)])
		self.default_entry= [('1_1', 0), ('1_2', 0), ('1_3', 0), ('1_4', 0), ('1_5', 0), ('1_6', 0), ('1_7', 0), ('1_8', 0), ('1_9', 0), ('1_10', 0), ('1_11', 0), ('1_12', 0), ('2_1', 0), ('2_2', 0), ('2_3', 0), ('2_4', 0), ('2_5', 0), ('2_6', 0), ('2_7', 0), ('2_8', 0), ('2_9', 0), ('2_10', 0), ('2_11', 0), ('2_12', 0), ('3_1', 0), ('3_2', 0), ('3_3', 0), ('3_4', 0), ('3_5', 0), ('3_6', 0), ('3_7', 0), ('3_8', 0), ('3_9', 0), ('3_10', 0), ('3_11', 0), ('3_12', 0), ('4_1', 0), ('4_2', 0), ('4_3', 0), ('4_4', 0), ('4_5', 0), ('4_6', 0), ('4_7', 0), ('4_8', 0), ('4_9', 0), ('4_10', 0), ('4_11', 0), ('4_12', 0), ('5_1', 0), ('5_2', 0), ('5_3', 0), ('5_4', 0), ('5_5', 0), ('5_6', 0), ('5_7', 0), ('5_8', 0), ('5_9', 0), ('5_10', 0), ('5_11', 0), ('5_12', 0), ('6_1', 0), ('6_2', 0), ('6_3', 0), ('6_4', 0), ('6_5', 0), ('6_6', 0), ('6_7', 0), ('6_8', 0), ('6_9', 0), ('6_10', 0), ('6_11', 0), ('6_12', 0)]
	def test_RunDummy(self):
		self.assertEqual(0, 0)

########## Unit Test createDefaultEntryToClusterDict
	def tes_createDefaultEntryToClusterDict_ShouldBe(self):		
		value = ClusterDictionary.createDefaultEntryToClusterDict().items()		
		self.assertEqual(self.default_entry, value)
########## Unit Test addDefaultEntryToClusterDict


########## Unit  addNewEntry(issuer_id)
	def test_addNewEntry(self):
		self.dict.addNewEntry('1234')
		self.assertTrue(self.dict.contains('1234'))
		self.assertTrue(self.default_entry, self.dict.getItems('1234'))

########## Unit  addNewEntry(issuer_id)

########## Unit Test contains(issuer_id)
	def test_Contains_ShouldBeTrue_with_IssuerID12345(self):
		# dict = ClusterDictionary()
		self.dict.addNewEntry('22222')
		self.assertTrue(self.dict.contains('22222'))
########## Unit Test contains(issuer_id)

########## Unit  Test getIssuerSpecificItem(issuer_id, item)
	def tes_getIssuerSpecificItem_ShouldBe0_withIssuerID1234AndItem1_1(self):
		self.dict.addNewEntry('1234')
		self.assertEqual(0,self.dict.getIssuerSpecificItem('1234','1_1'))		
########## Unit  Test getIssuerSpecificItem(issuer_id, item)		

########## Unit  Test incrementIssuerItem(issuer_id, item)		
	def test_incrementIssuerItem_ShouldBe1_with_IssuerID1234andItem1_1(self):
		self.dict.addNewEntry('1234')
		self.assertEqual(0,self.dict.getIssuerSpecificItem('1234','1_1_1_'))				
		self.dict.incrementIssuerItem('1234','1_1_1_')
		self.assertEqual(1,self.dict.getIssuerSpecificItem('1234','1_1_1_'))		

	def test_incrementIssuerItem_ShouldBe5_with_IssuerID1111andItem1_1(self):
		self.dict.addNewEntry('1111')
		self.assertEqual(0,self.dict.getIssuerSpecificItem('1111','1_1_1_'))				
		for counter in xrange(5):
			self.dict.incrementIssuerItem('1111','1_1_1_')
		self.assertEqual(5,self.dict.getIssuerSpecificItem('1111','1_1_1_'))				
########## Unit  Test incrementIssuerItem(issuer_id, item)		

########## Unit  Test addToIssuerItem(issuer_id, item)		
	def test_addToIssuerItem_ShouldBe1_with_IssuerID1234andItem1_1(self):
		self.dict.addNewEntry('1234')
		self.assertEqual(0,self.dict.getIssuerSpecificItem('1234','1_1_1_'))				
		self.dict.addToIssuerItem('1234','1_1_1_',1)
		self.assertEqual(1,self.dict.getIssuerSpecificItem('1234','1_1_1_'))		

	def test_addToIssuerItem_ShouldBe5_with_IssuerID1111andItem1_1(self):
		self.dict.addNewEntry('1111')
		self.assertEqual(0,self.dict.getIssuerSpecificItem('1111','1_1_1_'))					
		self.dict.addToIssuerItem('1111','1_1_1_', 5)
		self.dict.addToIssuerItem('1111','1_1_1_', 5)
		self.assertEqual(10,self.dict.getIssuerSpecificItem('1111','1_1_1_'))				
########## Unit  Test addToIssuerItem(issuer_id, item)		

########## Unit  Test exportCSV()		
	def test_exportCSV(self):
		newdict = ClusterDictionary([range(1,3),['mon','tues','wed'],range(1,3)])
		newdict.addNewEntry('1111')
		newdict.addToIssuerItem('1111','1_mon_1_', 8)		
		newdict.addToIssuerItem('1111','1_mon_1_', 8)				
		newdict.addNewEntry('2111')
		newdict.addToIssuerItem('2111','1_mon_2_', 18)				
		newdict.addNewEntry('3111')
		newdict.addToIssuerItem('3111','1_wed_2_', 28)						
		newdict.addNewEntry('4111')
		newdict.addToIssuerItem('4111','2_tues_2_', 118)								
		newdict.addNewEntry('5111')
		newdict.addToIssuerItem('5111','2_tues_1_', 218)													
		# self.assertTrue(newdict.exportCSV('test_file.csv'))
########## Unit  Test exportCSV()	

########## Unit  Test converCSVRow()		
	def test_convertCSVRowTest1(self):
		row_input = ['1234', '0', '4','3' ,'1234']
		answer = ClusterDictionary.convertCSVRow(row_input,3)
		expected_answer = {'issuer_id':'1234', 'key':"0_4_3_", 'value': 1234} 
		self.assertEqual(expected_answer, answer)
	def test_convertCSVRowTest2(self):
		row_input = ['1234', '0', '4','3','10','2','5432']
		answer = ClusterDictionary.convertCSVRow(row_input,5)
		expected_answer = {'issuer_id':'1234', 'key':"0_4_3_10_2_", 'value': 5432} 
		self.assertEqual(expected_answer, answer)
########## Unit  Test converCSVRow()		

########## UnitTest importCSV()		
	def test_importCSV(self):
		# newdict = ClusterDictionary([range(1,3),range(1,4),range(1,3)])
		self.dict.importCSV('test_input.csv')
		verify_item = self.dict.getIssuerSpecificItem('301011','1_2_1_')
		self.assertEqual(11, verify_item)
		verify_item = self.dict.getIssuerSpecificItem('101122','1_1_1_')
		self.assertEqual(22, verify_item)		
		verify_item = self.dict.getIssuerSpecificItem('200222','2_2_2_')
		self.assertEqual(44, verify_item)				
########## UnitTest importCSV()		

########## UnitTest genereateClusterFile()		
	
########## UnitTest genereateClusterFile()		
		
if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(ClusterDictionaryTest)
	unittest.TextTestRunner(verbosity=2).run(suite)
