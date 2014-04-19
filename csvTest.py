###
# Unit Tests for Converting Raw Parking Violation Data into Clusterable Tuples	
###

import unittest 

from  csv_process import *

class csvUnitTests(unittest.TestCase):

	# Failing Unit Test
	def test_RunDummy(self):
		self.assertEqual(0, 0)
	def test_AssignCategory_ShouldBe5_withViolationCode56(self):
		
		self.assertEqual(5, assignCategory(56))

###### Unit Test for extractFields()
	def test_extractFieldsShouldAnswerfromInput(self):		
		row =	['1358044703', 'FPE1082', 'NY', '999', '01/02/2014', '40', 'SDN', 'ACURA', 'P', '70930', '89970', '82230', '20150612', '0073', '73', '165', '954543', '0165', '0000', '1030A', '', '', 'F', '1777', 'PITKIN AVE', '', '0', '408', 'E2', '', 'BBBBBBB', 'ALL', 'ALL', 'GOLD', '0', '2006', '-', '6', '', '', '', '', '']
		answer = ['954543', '01/02/2014','1030A','40',  '1777 PITKIN AVE']		
		fields = extractFields(row)
		self.assertEquals(answer, fields)

	def test_extractFieldsShouldAnswer2fromInput2(self):		
		row =	['1358044703', 'FPE1082', 'NY', '999', '12/22/2014', '45', 'SDN', 'ACURA', 'P', '70930', '89970', '82230', '20150612', '0073', '73', '165', '951234', '0165', '0000', '1230P', '', '', 'F', '1234', 'COLUMBUS AVE', '', '0', '408', 'E2', '', 'BBBBBBB', 'ALL', 'ALL', 'GOLD', '0', '2006', '-', '6', '', '', '', '', '']
		answer = ['951234', '12/22/2014','1230P','45',  '1234 COLUMBUS AVE']		
		fields = extractFields(row)
		self.assertEquals(answer, fields)		
###### Unit Test for extractFields()
###### Unit Test calculateTimeFromString()	
	def test_CalculateTimefromString_ShouldBe0100from0100A(self):	
		self.assertEqual(100, calculateTimeFromString('0100A'))
	def test_CalculateTimefromString_ShouldBe1500from0300P(self):	
		self.assertEqual(1500, calculateTimeFromString('0300P'))
	def test_CalculateTimefromString_ShouldBe1259from1259P(self):	
		self.assertEqual(1259, calculateTimeFromString('1259P'))
	def test_CalculateTimefromString_ShouldBe1259from0059P(self):	
		self.assertEqual(1259, calculateTimeFromString('0059P'))		
###### Unit Test calculateTimeFromString()	
########### Unit Test assignTimeCategory
	def test_AssignTimeCategory_ShouldBe1with1000A(self):		
		self.assertEqual(2, assignTimeCategory('1000A'))

	def test_AssignTimeCategory_ShouldBe0with0830A(self):		
		self.assertEqual(1, assignTimeCategory('0830A'))		
		
	def test_AssignTimeCategory_ShouldBe2with1230P(self):		
		self.assertEqual(3, assignTimeCategory('1230P'))				
	def test_AssignTimeCategory_ShouldBe3with0430P(self):		
		self.assertEqual(4, assignTimeCategory('0430P'))				
	def test_AssignTimeCategory_ShouldBe0with0930P(self):		
		self.assertEqual(0, assignTimeCategory('0930P'))								
########### Unit Test assignTimeCategory
	# def test_ParseRow_ShouldReturn_ExtractedFiels(self):
		# test_row = ['1358044703,FPE1082,NY,999,01', '02', '2014,40,SDN,ACURA,P,70930,89970,82230,20150612,0073,73,165,954543,0165,0000,1030A,,,F,1777,PITKIN AVE,,0,408,E2,,BBBBBBB,ALL,ALL,GOLD,0,2006,-,6,,,,,']
		
if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(csvUnitTests)
	unittest.TextTestRunner(verbosity=2).run(suite)