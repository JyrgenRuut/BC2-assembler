	
def parseAssembly(fi, instructions, pointers):
	counter = 0
	true_counter = 0;
	
	for instruction in fi:
		if instruction[0][0] == '*':
			reference = '&' + instruction[0][1:]
			if reference in pointers:
				print("Error at line: ", true_counter + 1, "; Label already defined.")
			else:
				pointers.update({reference:counter})
				counter -= 1
		else:
			instructions.append(instruction)
		true_counter += 1
		counter += 1
	
