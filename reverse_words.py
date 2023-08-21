import os, sys 

input_filepath = sys.argv[1]


# to do: teach this to respect lines 


with open(input_filepath, 'r') as input_file: 
	poem = input_file.read()

words = poem.split()
words.reverse()

print(" ".join(words))