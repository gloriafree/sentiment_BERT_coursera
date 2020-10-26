# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 16:53:28 2020

@author: bblje
"""
import numpy as np

#--------------------- argmax -------------------#
A = np.matrix([[1,2,44,3], [4,5,6,1], [9,10,55,3]])
A.shape
# multi-dim array, shape (3,4) = (row, col)

## no index parameter
np.argmax(A)
# argmax returns the first(if more than one max value) index of max value
B = [1,1,1]
np.argmax(B)

# if no axis parameter specified in the function, numpy automatically flattens the multiple dimentional array and returns the index of max

## specify index paramter
np.argmax(A, axis = 0)
# 0 -> row of matrix
np.argmax(A, axis = 1)
# 1 -> col of matrix




#----------------create dictionary from key value -----------------------#

celebr = ['Tony','Harry','Katty','Sam']
perc = [69,31,0,0]



d_org = dict(zip(celebr, perc))
d_org


d_new = {v:k  for k, v in d_org.items() }
d_new




# tqdm

from tqdm import tqdm

for i in tqdm(range(int(9e6))):
    pass

