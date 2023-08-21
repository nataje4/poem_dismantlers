import os, sys 


number_of_subpoems = sys.argv[1]
input_filepath = sys.argv[2]


# to do: teach this to respect lines 

try: 
	num_poems = int(number_of_subpoems)
except: 
	print("that is not a valid number")

with open(input_filepath, 'r') as input_file: 
	poem = input_file.read()


lines = poem.splitlines()
lines = [ l.strip() + "**\n" for l in lines]
poem_prime = " ".join(lines)
words = poem_prime.split()


for i in range(num_poems): 
	dummy_poem_array = []
	for j in range(len(words)): 
		if j % num_poems == i: 
			dummy_poem_array.append(words[j])
	print(" ".join(dummy_poem_array))
	print("\n")
  