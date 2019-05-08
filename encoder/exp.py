import numpy as np


dict = {
	"a" : 1,
	"b" : 3,
	"z" : 4
		}


#iterating through list and making two array.

arr_k = np.array([])
arr_v = np.array([])

for k,v in dict.items():
	arr_k = np.append(arr_k,k)
	arr_v = np.append(arr_v,[v])

arr_v = np.array(arr_v,int)         # to convert float value to int


print(arr_k,"\t",arr_v)
