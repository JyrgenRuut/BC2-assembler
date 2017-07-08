import CustomError

def parseAssembly(fi, instructions, pointers):
	counter = 0
	true_counter = 0;
	
	for instruction in fi:
		if instruction[0][0] == '*':
			reference = '&' + instruction[0][1:]
			if reference in pointers:
				CustomError.ERR_labelDefined(true_counter + 1)
			else:
				pointers.update({reference:counter})
				counter -= 1
		elif instruction[0][0] != '/':
			instruction.append(true_counter + 1)
			instructions.append(instruction)
		true_counter += 1
		counter += 1
	
