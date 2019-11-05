def greet(name):
	print('hello, ' + name + '!')
	greet2(name)
	print('geeting ready to say bye...')
	bye()

def greet2(name):
	print('how are you, ' + name + '?')

def bye():
	print('ok bye!')

greet('mark')