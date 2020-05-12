class University:
	
	def __init__(self, name, code):
		self.name = name
		self.code = code
		
def a_level(points):
	global a_levels
	if "48" in points:
		a_levels = "EEE"
	elif "56" in points:
		a_levels = "DEE"
	elif "64" in points:
		a_levels = "DDE"
	elif "72" in points:
		a_levels = "DDD"
	elif "80" in points:
		a_levels = "CDD"
	elif "88" in points:
		a_levels = "CCD"
	elif "96" in points:
		a_levels = "CCC"
	elif "104" in points:
		a_levels = "BCC"
	elif "112" in points:
		a_levels = "BBC"
	elif "120" in points:
		a_levels = "BBB"
	elif "128" in points:
		a_levels = "ABB"
	elif "136" in points:
		a_levels = "AAB"
	elif "144" in points:
		a_levels = "AAA"
	elif "152" in points:
		a_levels = "A*AA"
	elif "160" in points:
		a_levels = "A*A*A"
	elif "168" in points:
		a_levels = "A*A*A*"
	return a_levels
		
