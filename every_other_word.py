import os, sys 

input_filepath = sys.argv[1]


# to do: teach this to respect lines 


with open(input_filepath, 'r') as input_file: 
	poem = input_file.read()

words = poem.split()

a_words = []
b_words = []

for i in range(len(words)): 
	if i % 2 == 0: 
		b_words.append(words[i])
	else: 
		a_words.append(words[i])

a_poem = " ".join(a_words)
b_words.reverse()
b_words = b_words
b_poem = " ".join(b_words)

print(a_poem)
print("\n\n")
print(b_poem)