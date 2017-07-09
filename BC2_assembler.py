import sys
import BC2parser
import BC2instructions
import CustomError

#assembly_file, output_file = sys.argv[1], sys.arv[2]

input_file = []
instructions = []
pointers = {}
assembly_failed = 0
counter = 0

fi = open("input.txt", "r")
temp = fi.readlines()
for line in temp:
	input_file.append(line.split())

BC2parser.parseAssembly(input_file, instructions, pointers)
fi.close()

fo = open("Output.txt", "w")

for instruction in instructions:
	wasResolved = BC2instructions.resolveInstruction(instruction, pointers, fo, assembly_failed)
	if wasResolved == False:
		assembly_failed = True
	counter += 1
	if counter % 4 == 0:
		fo.write("\n")
	else:
		fo.write('\t')

if assembly_failed == 1:
	print(CustomError.ERR_assemblyFailed())
	fo.close()
	file_delete = open("Output.txt", "w")
	file_delete.write(CustomError.ERR_assemblyFailed())
	file_delete.close()

