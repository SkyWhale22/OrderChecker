from Scrappers.ScrapperBase import ScrapperBase
from Interfaces.GlobalInterface import SignInData
from Scrappers.ChildScrappers import ESMScrapper, EleventhStScrapper, SmartStoreScrapper
from enum import Enum

"""
	@Description
"""
class Type(Enum):
	kESM    = 0
	k11st   = 1
	kSmart  = 2

# Factory class
class ScrapperFactory:
	@staticmethod
	def Create(number):
		if(number == Type.kESM):
			return ESMScrapper()
		elif(number == Type.k11st):
			return EleventhStScrapper()
		elif(number == Type.kSmart):
			return SmartStoreScrapper()

testList = []

while(True):
	print("{0} = ESM, {1} = 11st, {2} = Smart Store, {3} = Stop")
	answer = int(input())

	if(answer == '3'):
		break

	testList.append(ScrapperFactory.Create(answer))

for unit in testList:
	unit.Scrap()



