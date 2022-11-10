# problem reverse an array|list

from os import *
from sys import *
from collections import *
from math import *

def reverseArray(arr, m):
    
	s = m
	e = len(arr) - 1

	while s<=e:
		arr[s],arr[e] = arr[e],arr[s]
		s+=1
		e-=1

	return arr



# m = int(input())
# a = list(map(int, input().split()))
# print(reverseArray(a,m))



