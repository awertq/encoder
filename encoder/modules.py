''' FUNCTIONS FOR ENCODER '''

import numpy as np


#function to make dict with key as alphabets and value zero.

def letter_dict_maker():

	ord_of_a = 1
	list_of_alpha = []

	for i in range(1000):
		list_of_alpha.append(str(chr(ord_of_a)))
		ord_of_a +=1

	letter_dict = {}
	for letter in list_of_alpha:
		letter_dict[letter] = 0


	return letter_dict



'''------------------------------------------------------------------------------'''


'''converting letter_dict to array and using boolean array to fetch the true data
   then printing the dict of true value'''

def letter_dict_printer(letter_dict):
	arr_k = np.array([])   #key storing array
	arr_v = np.array([])   #value storing array

	#iterating through list and making two array.

	for k,v in letter_dict.items():
		arr_k = np.append(arr_k,k)
		arr_v = np.append(arr_v,[v])

	arr_v = np.array(arr_v,int)         # to convert float value to int

	#making arr_v a boolean array

	arr_v = arr_v > 0

	arr_k[arr_v]       #this will give all the key with value true

	for i in arr_k:
		for j in letter_dict:           #finetillnow
			print(i)
			if i == letter_dict[j]:
				print("  ",j,"\t",letter_dict[j])



















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
