"""
	@Description

"""


class OrderData(object):
	def __init__(self, buyerName, shippingAddress, contact, item, amount, paid):
		self.m_buyerName = buyerName
		self.m_shippingAddress = shippingAddress
		self.m_contactNumber = contact
		self.m_orderedItem = item
		self.m_orderedAmount = amount
		self.m_totalPaid = paid

class SignInData(object):
	def __init(self, id, pw):
		self.m_id = id
		self.m_pw = pw

