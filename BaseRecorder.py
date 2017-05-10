
import platform

class BaseRecorder(object):

	def __init__(self):
		self.platform = platform.system()
