import modules as m


''' __ENCODER__ '''


file_path = input("File Name : ")

''' making each line as an element in list '''

with open(file_path,"r") as file:                   #opening the text file store in the same folder where programme stored.
	content = file.readlines()		    #making list of each line as element and storing it in "content" variable.

for l in range(len(content)):
	content[l] = content[l].strip()             #striping all the spaces from each element(line).


letter_dict = m.letter_dict_maker()                 #making dictionary alphabet as key and values=0


'''file11 = open(file_path)
file__ = file11.read()
file11.close()

for i in file__:

	for j in i:
		for k,v in letter_dict.items():
			if j == k:
				v += 1
'''


for i in range(len(content)):
	content[i] = content[i].split()		    	#making a nested list in which we split each word as element

for x in range(len(content)):			   	 #looping through content list
	for y in content[x]:			   	 #looping through nested list(words) in content list
		for z in y:			   	 #loopint through each letter in the nested list(words)
			for k,v in letter_dict.items():		# k is for keys and v for value in 'letter_dict' dictionary
				if k == z:			# if key is equal to z(letter)
					v +=1			# add one to value of that key


print(letter_dict)
