mode = "CLI"

def get_input(string):
	if mode is "CLI":
		return input(string)
	else:
		return console.get(string)

def _print(string, ending=None, at=None):
	if mode is "CLI":
		print(string, end=ending)
	else:
		console.log(string, end=ending)
	return