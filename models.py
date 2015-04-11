from google.appengine.ext import ndb

class Task (ndb.Model):
	"""Models a task"""
	title = ndb.StringProperty()
	groupId = ndb.IntegerProperty(repeated=True)
	
class TaskGroup (ndb.Model):
	"""Models a collection of tasks (like a tag)"""
	title = ndb.StringProperty()
	
