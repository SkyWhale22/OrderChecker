"""
	@Description
"""
from Scrappers.ScrapperBase import ScrapperBase

class ESMScrapper(ScrapperBase):
	####################################################################################
	#                                 Member Functions                                 #
	####################################################################################
	# ----- Private     -----
	# ----- Protected   -----
	# ----- Public      -----

	####################################################################################
	#                                 Member Functions                                 #
	####################################################################################

	# ----- Private     -----
	def __init(self):
		pass

	# ----- Protected   -----
	# ----- Public      -----

	def SignIn(self, account):
		super.SignIn(account)
		pass
	def SignOut(self):
		pass
	def Scrap(self):
		print("Scrapping data from ESM Plus")
	pass

class EleventhStScrapper(ScrapperBase):
	def __init(self):
		pass

	def SignIn(self, account):
		pass

	def SignOut(self):
		pass

	def Scrap(self):
		print("Scrapping data from 11st")

	pass

class SmartStoreScrapper(ScrapperBase):
	def __init(self):
		pass

	def SignIn(self, account):
		pass

	def SignOut(self):
		pass

	def Scrap(self):
		print("Scrapping data from Smart Store")
	pass
