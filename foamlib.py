class AuthenticationError(Exception):
	"""Raised when there is an exception that occurs in the process of authentication"""

class MissingDataError(Exception):
	"""Raised when an error occurs because of lack of data"""

class User():
	def __init__(self, user_id):
		self.user_id=user_id
		if user_id==None:
			self.username=None
		else:
			self.username="testuser"
	
	def profile_url(self):
		return "http://www.foamservice.com/users/"+self.username+"/profile"
		
	def friends_markup(self):
		"""Premade markup to display in a webview or such"""
		return ", ".join(self.friends())
	
	def friends(self):
		"""returns friend id list"""
		return ["44345ffdfg53434", "4345gfrdse434323" ]
	
	
	def login(self, password):
		return True#send server message about logging in.
	
	def logout(self):
		if self.user_id!=None:
			pass#Do something that tells server you logged out.
		else:
			raise MissingDataError
			
	
def user_id(username):
	return "test12345"#Send request for user id.
		
def authenticate(username, password):
	u=User(user_id(username))
	if u.login(password)==True:
		return u
	else:
		raise AuthenticationError("Failed to login, username or password is incorrect.")
	