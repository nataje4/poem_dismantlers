import os, sys 


words_per_line = sys.argv[1]
input_filepath = sys.argv[2]


try: 
	per_line = int(words_per_line)
except: 
	print("that is not a valid number")


with open(input_filepath, 'r') as input_file: 
	poem = input_file.read()


lines = poem.splitlines()
lines = [ l.strip() for l in lines]
poem_prime = " ".join(lines)
words = poem_prime.split()

new = []


for i in range(len(words)): 
	# d = (len(words)-i)
# 	print(d)
# 	if d % per_line == 0: 
# 		words.insert(d, "\n")
	if i % per_line == 0:
		new.append("\n")
	new.append(words[i])


#print(c)
	
print(" ".join(new))
