atline = "Error at line: "

def ERR_labelDefined(line):
	print(atline, line, "; Label already defined.")

def ERR_missingArgument(line, position):
	print(atline, line, "; Missing argument at argument position: ", position)

def ERR_invalidArgument(line, position):
	print(atline, line, "; Invalid argument at argument position: ", position)

def ERR_invalidArgumentType(line, position, requirement):
	print(atline, line, "; Invalid argument type at argument position: ", position, ", a ", requirement, " is required instead.")

def ERR_labelMissing(line):
	print(atline, line, "; Reference to label can not be resolved, label is missing from source.")

def ERR_invalidValue(line, position):
	print(atline, line, "; Invalid argument value at argument position: ", position)

def ERR_outOfBounds(line):
	print(atline, line, "; Label reference results in an address outside of the allowed 64K range.")

def ERR_assemblyFailed():
	return "\nAssembly of the source file failed, please resolve all errors."
