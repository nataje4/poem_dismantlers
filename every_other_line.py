import os, sys 

input_filepath = sys.argv[1]


# to do: teach this to respect lines 


with open(input_filepath, 'r') as input_file: 
	poem = input_file.read()

lines = poem.splitlines()

a_lines = []
b_lines = []

for i in range(len(lines)): 
	if i % 2 == 0: 
		b_lines.append(lines[i] + "\n") 
	else: 
		a_lines.append(lines[i] + "\n")

a_poem = " ".join(a_lines)
# b_lines.reverse()
b_lines = b_lines
b_poem = " ".join(b_lines)

print(a_poem)
print("\n\n")
print(b_poem)