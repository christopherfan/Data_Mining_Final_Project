import unittest 

from  ClusterDictionary import *


class ClusterDictionaryTest(unittest.TestCase):
	# Failing Unit Test
	def setUp(self):
		self.dict = ClusterDictionary()
		self.default_entry= [('1_1', 0), ('1_2', 0), ('1_3', 0), ('1_4', 0), ('1_5', 0), ('1_6', 0), ('1_7', 0), ('1_8', 0), ('1_9', 0), ('1_10', 0), ('1_11', 0), ('1_12', 0), ('2_1', 0), ('2_2', 0), ('2_3', 0), ('2_4', 0), ('2_5', 0), ('2_6', 0), ('2_7', 0), ('2_8', 0), ('2_9', 0), ('2_10', 0), ('2_11', 0), ('2_12', 0), ('3_1', 0), ('3_2', 0), ('3_3', 0), ('3_4', 0), ('3_5', 0), ('3_6', 0), ('3_7', 0), ('3_8', 0), ('3_9', 0), ('3_10', 0), ('3_11', 0), ('3_12', 0), ('4_1', 0), ('4_2', 0), ('4_3', 0), ('4_4', 0), ('4_5', 0), ('4_6', 0), ('4_7', 0), ('4_8', 0), ('4_9', 0), ('4_10', 0), ('4_11', 0), ('4_12', 0), ('5_1', 0), ('5_2', 0), ('5_3', 0), ('5_4', 0), ('5_5', 0), ('5_6', 0), ('5_7', 0), ('5_8', 0), ('5_9', 0), ('5_10', 0), ('5_11', 0), ('5_12', 0), ('6_1', 0), ('6_2', 0), ('6_3', 0), ('6_4', 0), ('6_5', 0), ('6_6', 0), ('6_7', 0), ('6_8', 0), ('6_9', 0), ('6_10', 0), ('6_11', 0), ('6_12', 0)]
	def test_RunDummy(self):
		self.assertEqual(0, 0)

########## Unit Test createDefaultEntryToClusterDict
	def test_createDefaultEntryToClusterDict_ShouldBe(self):
		
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
	def test_getIssuerSpecificItem_ShouldBe0_withIssuerID1234AndItem1_1(self):
		self.dict.addNewEntry('1234')
		self.assertEqual(0,self.dict.getIssuerSpecificItem('1234','1_1'))		
########## Unit  Test getIssuerSpecificItem(issuer_id, item)		

########## Unit  Test incrementIssuerItem(issuer_id, item)		
	def test_incrementIssuerItem_ShouldBe1_with_IssuerID1234andItem1_1(self):
		self.dict.addNewEntry('1234')
		self.assertEqual(0,self.dict.getIssuerSpecificItem('1234','1_1'))				
		self.dict.incrementIssuerItem('1234','1_1')
		self.assertEqual(1,self.dict.getIssuerSpecificItem('1234','1_1'))		

	def test_incrementIssuerItem_ShouldBe5_with_IssuerID1111andItem1_1(self):
		self.dict.addNewEntry('1111')
		self.assertEqual(0,self.dict.getIssuerSpecificItem('1111','1_1'))				
		for counter in xrange(5):
			self.dict.incrementIssuerItem('1111','1_1')
		self.assertEqual(5,self.dict.getIssuerSpecificItem('1111','1_1'))				
########## Unit  Test incrementIssuerItem(issuer_id, item)		

########## Unit  Test addToIssuerItem(issuer_id, item)		
	def test_addToIssuerItem_ShouldBe1_with_IssuerID1234andItem1_1(self):
		self.dict.addNewEntry('1234')
		self.assertEqual(0,self.dict.getIssuerSpecificItem('1234','1_1'))				
		self.dict.addToIssuerItem('1234','1_1',1)
		self.assertEqual(1,self.dict.getIssuerSpecificItem('1234','1_1'))		

	def test_addToIssuerItem_ShouldBe5_with_IssuerID1111andItem1_1(self):
		self.dict.addNewEntry('1111')
		self.assertEqual(0,self.dict.getIssuerSpecificItem('1111','1_1'))					
		self.dict.addToIssuerItem('1111','1_1', 5)
		self.dict.addToIssuerItem('1111','1_1', 5)
		self.assertEqual(10,self.dict.getIssuerSpecificItem('1111','1_1'))				
########## Unit  Test addToIssuerItem(issuer_id, item)		

########## Unit  Test exportCSV()		
	def test_exportCSV(self):
		newdict = ClusterDictionary()
		newdict.addNewEntry('1111')
		newdict.addToIssuerItem('1111','1_1', 8)		
		newdict.addToIssuerItem('1111','1_1', 8)				
		newdict.addNewEntry('2111')
		newdict.addToIssuerItem('2111','1_2', 18)				
		newdict.addNewEntry('3111')
		newdict.addToIssuerItem('3111','2_5', 28)						
		newdict.addNewEntry('4111')
		newdict.addToIssuerItem('4111','4_5', 118)								
		newdict.addNewEntry('5111')
		newdict.addToIssuerItem('5111','5_11', 218)													
		# self.assertTrue(newdict.csvExport())		
########## Unit  Test exportCSV()	

########## Unit  Test converCSVRow()		
	def test_convertCSVRowTest1(self):
		row_input = ['1234', '0', '4', '1234']
		answer = ClusterDictionary.convertCSVRow(row_input)
		expected_answer = {'issuer_id':'1234', 'violation_time':'0_4', 'total': 1234} 
		self.assertEqual(expected_answer, answer)
	def test_convertCSVRowTest2(self):
		row_input = ['33333', '5', '1', '8888']
		answer = ClusterDictionary.convertCSVRow(row_input)
		expected_answer = {'issuer_id':'33333', 'violation_time':'5_1', 'total': 8888} 
		self.assertEqual(expected_answer, answer)		
########## Unit  Test converCSVRow()		

########## UnitTest importCSV()		
	def test_importCSV(self):
		self.dict.importCSV('test_input.csv')
		verify_item = self.dict.getIssuerSpecificItem('301011','3_10')
		self.assertEqual(11, verify_item)
		verify_item = self.dict.getIssuerSpecificItem('101122','1_11')
		self.assertEqual(22, verify_item)		
		verify_item = self.dict.getIssuerSpecificItem('200222','2_2')
		self.assertEqual(44, verify_item)				
########## UnitTest importCSV()		

########## UnitTest genereateClusterFile()		
	
########## UnitTest genereateClusterFile()		
		
if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(ClusterDictionaryTest)
	unittest.TextTestRunner(verbosity=2).run(suite)
