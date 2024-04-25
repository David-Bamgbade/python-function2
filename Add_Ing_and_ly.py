def string_add(letter):

	if len(letter) < 3:
		return letter
	elif letter[-3:] == 'ing':
		return letter + 'ly'
	else:
		return string + ing