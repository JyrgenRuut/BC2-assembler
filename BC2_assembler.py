import sys
import BC2parser
import BC2instructions
import CustomError

#sys.argv[1], sys.argv[2]

input_file = []
instructions = []
pointers = {}
assembly_failed = 0
counter = 0

#run through the source file and split it up to lines of code with each word being a "statement". said words are also used as tokens for later logic
fi = open("input.txt", "r")
temp = fi.readlines()
for line in temp:
	input_file.append(line.split())
BC2parser.parseAssembly(input_file, instructions, pointers)
fi.close()

fo = open("Output.txt", "w")

#loop that tries to assemble the source file into "machine code" (though it is in text form, reason being, that's what "Logisim" accepts as input)
#the assembly process will run through the whole file to catch all errors but will only write to an output until no errors have been found
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

