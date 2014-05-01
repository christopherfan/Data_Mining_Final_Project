# -*- coding: utf-8 -*-
"""
Created on Thu Apr 24 14:46:41 2014

@author: chrisfan
"""

import unittest 

from  KNN_Data import *

class KNN_Data_Test(unittest.TestCase):

	def test_DefaultRunner(self):
		self.assertEqual(0, 0)
	
	def test_GenerateTimeNumber(self):
		self.assertEqual(0, generateTimeNumber('00:00'))
		self.assertEqual(360, generateTimeNumber('06:00'))
		self.assertEqual(400, generateTimeNumber('06:40'))
	
if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(KNN_Data_Test)
	unittest.TextTestRunner(verbosity=2).run(suite)