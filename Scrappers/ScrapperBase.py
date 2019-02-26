"""
	@Description

"""

from Interfaces.GlobalInterface import OrderData, SignInData

class ScrapperBase:
	####################################################################################
	#                                 Member Variables                                 #
	####################################################################################

	# ----- Private     -----
	# ----- Protected   -----
	# ----- Public      -----

	####################################################################################
	#                                 Member Functions                                 #
	####################################################################################

	# ----- Private     -----
	def __init__(self):
		self._m_orderList = []

	# ----- Protected   -----
	# ----- Public      -----
	def SignIn(self, account):
		assert account == None

	def SignOut(self):
		pass

	def Scrap(self):

		return False

	def GetOrderList(self):
		assert len(self._m_orderList) != 0
		return self._m_orderList

if __name__ == "__main__":
	test = ScrapperBase()
	test.GetOrderList()