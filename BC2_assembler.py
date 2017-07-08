import sys
import BC2parser

#assembly_file, output_file = sys.argv[1], sys.arv[2]

fi = []
instructions = []
pointers = {}

inputFile = open("input.txt", "r")
temp = inputFile.readlines()
for line in temp:
	fi.append(line.split())

BC2parser.parseAssembly(fi, instructions, pointers)

print(instructions)
print(pointers)


