''' FUNCTIONS FOR ENCODER '''

#function to make dict with key as alphabets and value zero.

def letter_dict_maker():

	ord_of_a = 97
	list_of_alpha = []

	for i in range(26):
		list_of_alpha.append(str(chr(ord_of_a)))
		ord_of_a +=1

	letter_dict = {}
	for letter in list_of_alpha:
		letter_dict[letter] = 0

	return letter_dict

# function that examine file and count the number of letter and store it in a dict.

def letter_index(file):

	with open(file) as file:
		var001 = file.readlines()

	for temp in range(len(var001)):
		var001[temp] = var001[temp].strip()

		temp0011 = list(str(var001[temp]))
		














def letter_index(file):
	with open(file) as file:
		var001 = file.read()

	for temp in var001:
		var001[temp] = var001[temp].strip()
