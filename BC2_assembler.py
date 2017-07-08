import sys
import BC2parser
import BC2instructions
import CustomError

#assembly_file, output_file = sys.argv[1], sys.arv[2]

input_file = []
instructions = []
pointers = {}

fi = open("input.txt", "r")
temp = fi.readlines()
for line in temp:
	input_file.append(line.split())

BC2parser.parseAssembly(input_file, instructions, pointers)
fi.close()

fo = open("Output.txt", "w")

for instruction in instructions:
	BC2instructions.resolveInstruction(instruction, pointers, fo)

