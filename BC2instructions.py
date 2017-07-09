import CustomError

jump_flags = {
	"always"	: "0",	"a"		: "0",
	"overflow"	: "1",	"of"	: "1",
	"underflow"	: "2",	"uf"	: "2",
	"sign"		: "3",	"s"		: "3",
	"zero"		: "4",	"z"		: "4",
	"A>B"		: "5",	"gt"	: "5",
	"A=B"		: "6",	"eq"	: "6",
	"A<B"		: "7",	"lt"	: "7",
	"!overflow"	: "8",	"nof"	: "8",
	"!underflow": "9",	"nuf"	: "9",
	"!sign"		: "a",	"ns"	: "a",
	"!zero"		: "b",	"nz"	: "b",
	"!A=B"		: "c",	"ne"	: "c",
	"A>=B"		: "d",	"gtoe"	: "d",
	"A<=B"		: "e",	"ltoe"	: "e"
}

registers = {
	"rz":	'0',
	"r1":	'1',
	"r2":	'2',
	"r3":	'3',
	"r4":	'4',
	"r5":	'5',
	"r6":	'6',
	"r7":	'7',
	"r8":	'8',
	"r9":	'9',
	"r10":	'a',
	"r11":	'b',
	"r12":	'c',
	"rdp":	'd',
	"rpb":	'e',
	"rsp":	'f'
}

def threeRegFieldInstruction(instruction, pointers, fo, opcode):
	top_byte = opcode
	instruction_length = len(instruction)
	if instruction_length < 5:
		if instruction_length < 4:
			if instruction_lenth < 3:
				CustomError.ERR_missingArgument(instruction[-1], '1')
				return 0
			CustomError.ERR_missingArgument(instruction[-1], '2')
			return 0
		CustomError.ERR_missingArgument(instruction[-1], '3')
		return 0
	if instruction[1][0] != 'r':
		CustomError.ERR_invalidArgumentType(instruction[-1], '1', "register reference")
		return 0
	elif instruction[2][0] != 'r':
		CustomError.ERR_invalidArgumentType(instruction[-1], '2', "register reference")
		return 0
	elif instruction[3][0] != 'r':
		CustomError.ERR_invalidArgumentType(instruction[-1], '3', "register reference")
		return 0
	topmid_byte_top_nibble = registers.get(instruction[1], None)
	if topmid_byte_top_nibble == None:
		CustomError.ERR_invalidValue(instruction[-1], '1')
		return 0
	topmid_byte_bottom_nibble = registers.get(instruction[2], None)
	if topmid_byte_bottom_nibble == None:
		CustomError.ERR_invalidValue(instruction[-1], '2')
		return 0
	botmid_byte_top_nibble = registers.get(instruction[3], None)
	if botmid_byte_top_nibble == None:
		CustomError.ERR_invalidValue(instruction[-1], '3')
		return 0
	fo.write("{}{}{} {}{}".format(top_byte, topmid_byte_top_nibble, topmid_byte_bottom_nibble, botmid_byte_top_nibble, "000"))
	return 1

def writeAndRead1Instruction(instruction, pointers, fo, opcode):
	top_byte = opcode
	if len(instruction) < 4:
		if len(instruction) < 3:
			CustomError.ERR_missingArgument(instruction[-1], '1')
			return 0
		CustomError.ERR_missingArgument(instruction[-1], '2')
		return 0
	if instruction[1][0] != 'r':
		CustomError.ERR_invalidArgumentType(instruction[-1], '1', "register reference")
		return 0
	elif instruction[2][0] != 'r':
		CustomError.ERR_invalidArgumentType(instruction[-1], '2', "register reference")
		return 0
	topmid_byte_top_nibble = registers.get(instruction[1], None)
	if topmid_byte_top_nibble == None:
		CustomError.ERR_invalidValue(instruction[-1], '1')
		return 0
	botmid_byte_top_nibble = registers.get(instruction[2], None)
	if botmid_byte_top_nibble == None:
		CustomError.ERR_invalidValue(instruction[-1], '2')
		return 0
	fo.write("{}{}{} {}{}".format(top_byte, topmid_byte_top_nibble, '0', botmid_byte_top_nibble, "000"))
	return 1

def writeAndRead2Instruction(instruction, pointers, fo, opcode):
	top_byte = opcode
	if len(instruction) < 4:
		if len(instruction) < 3:
			CustomError.ERR_missingArgument(instruction[-1], '1')
			return 0
		CustomError.ERR_missingArgument(instruction[-1], '2')
		return 0
	if instruction[1][0] != 'r':
		CustomError.ERR_invalidArgumentType(instruction[-1], '1', "register reference")
		return 0
	elif instruction[2][0] != 'r':
		CustomError.ERR_invalidArgumentType(instruction[-1], '2', "register reference")
		return 0
	topmid_byte_top_nibble = registers.get(instruction[1], None)
	if topmid_byte_top_nibble == None:
		CustomError.ERR_invalidValue(instruction[-1], '1')
		return 0
	topmid_byte_bottom_nibble = registers.get(instruction[2], None)
	if topmid_byte_bottom_nibble == None:
		CustomError.ERR_invalidValue(instruction[-1], '2')
		return 0
	fo.write("{}{}{} {}".format(top_byte, topmid_byte_top_nibble, topmid_byte_bottom_nibble, "0000"))
	return 1

def writeFieldWithStackInstruction(instruction, pointers, fo, opcode):
	if len(instruction) < 3:
		CustomError.ERR_missingArgument(instruction[-1], '1')
		return 0
	if instruction[1][0] != 'r':
		CustomError.ERR_invalidArgumentType(instruction[-1], '1', "register reference")
		return 0
	topmid_byte_top_nibble = registers.get(instruction[1], None)
	if topmid_byte_top_nibble == None:
		CustomError.ERR_invalidValue(instruction[-1], '1')
		return 0
	fo.write("{}{}{}".format(opcode, topmid_byte_top_nibble, "e f000"))
	return 1

def instr_Jmp(instruction, pointers, fo):
	if len(instruction) < 4:
		if len(instruction) < 3:
			CustomError.ERR_missingArgument(instruction[-1], '1')
			return 1
		CustomError.ERR_missingArgument(instruction[-1], '2')
		return 0
	topmid_byte_bottom_nibble = jump_flags.get(instruction[1], None)
	if topmid_byte_bottom_nibble == None:
		CustomError.ERR_invalidArgument(instruction[-1], '1')
		return 0
	if instruction[2][0] != '&':
		CustomError.ERR_invalidArgumentType(instruction[-1], '2', "label reference")
		return 0
	temp = pointers.get(instruction[2], None)
	if temp == None:
		CustomError.ERR_labelMissing(instruction[-1])
		return 0
	low_bytes = int(temp) * 2
	if low_bytes > 65535:
		CustomError.ERR_outOfBounds(instruction[-1])
		return 0
	fo.write("{}{} {}".format("0d0", topmid_byte_bottom_nibble,"%.4x"%(low_bytes)))
	return 1

def instr_Inc(instruction, pointers, fo):
	return writeAndRead1Instruction(instruction, pointers, fo, "17")
	
def instr_Dec(instruction, pointers, fo):
	return writeAndRead1Instruction(instruction, pointers, fo, "18")

def instr_Push(instruction, pointers, fo):
	return writeFieldWithStackInstruction(instruction, pointers, fo, "10")

def instr_Pop(instruction, pointers, fo):
	return writeFieldWithStackInstruction(instruction, pointers, fo, "11")

def instr_Call(instruction, pointers, fo):
	if len(instruction) < 3:
		CustomError.ERR_missingArgument(instruction[-1], '1')
		return 0
	if instruction[1][0] != '&':
		CustomError.ERR_invalidArgumentType(instruction[-1], '1', "label reference")
		return 0
	temp = pointers.get(instruction[1], None)
	if temp == None:
		CustomError.ERR_labelMissing(instruction[-1])
		return 0
	low_bytes = int(temp) * 2
	if low_bytes > 65535:
		CustomError.ERR_outOfBounds(instruction[-1])
		return 0
	fo.write("{} {}".format("0efe", "%.4x"%(low_bytes)))
	return 1

def instr_Ret(instruction, pointers, fo):
	fo.write("0f0e f000")
	return 1

def instr_Mov(instruction, pointers, fo):
	if len(instruction) < 4:
		if len(instruction) < 3:
			CustomError.ERR_missingArgument(instruction[-1], '1')
			return 0
		CustomError.ERR_missingArgument(instruction[-1], '2')
		return 0
	if instruction[1][0] != 'r':
		CustomError.ERR_invalidArgumentType(instruction[-1], '1', "register reference")
		return 0
	topmid_byte_top_nibble = registers.get(instruction[1], None)
	if topmid_byte_top_nibble == None:
		CustomError.ERR_invalidValue(instruction[-1], '1')
		return 0
	if instruction[2][0] == 'r':
		topmid_bottom_nibble = registers.get(instruction[2], None)
		if topmid_bottom_nibble == None:
			CustomError.ERR_invalidArgumentType(instruction[-1], '1', "register reference")
			return 0
		fo.write("{}{}{} {}".format("00", topmid_byte_top_nibble, topmid_byte_bottom_nibble, "0000"))
		return 1
	elif instruction[2][0] == 'd':
		if -32768 > int(instruction[2][1:]) > 32767:
			CustomError.ERR_invalidValue(instruction[-1], '2')
			return 0
		else:
			fo.write("{}{}{} {}".format("00", topmid_byte_top_nibble, '0', "%4.4x"%(int(instruction[2][1:]))))
			return 1
	elif len(instruction[2]) == 5 and instruction[2][0] == 'h':
		bottom_bytes = []
		for c in instruction[2][1:]:
			if '0' <= c <= '9' or 'a' <= c <= 'f':
				bottom_bytes.append(c)
			else:
				CustomError.ERR_invalidValue(instruction[-1], '2')
				return 0
		fo.write("{}{}{} {}".format("00", topmid_byte_top_nibble, '0', instruction[2][1:]))
		return 1
	else:
		CustomError.ERR_invalidArgumentType(instruction[-1], '2', "d (decimal), h (hexadecimal) or r (register reference)")
		return 0

def instr_Add(instruction, pointers, fo):
	return threeRegFieldInstruction(instruction,pointers, fo, "01")

def instr_Addc(instruction, pointers, fo):
	return threeRegFieldInstruction(instruction,pointers, fo, "02")

def instr_Sub(instruction, pointers, fo):
	return threeRegFieldInstruction(instruction,pointers, fo, "03")

def instr_Subb(instruction, pointers, fo):
	return threeRegFieldInstruction(instruction,pointers, fo, "04")

def instr_Xor(instruction, pointers, fo):
	return threeRegFieldInstruction(instruction,pointers, fo, "05")

def instr_And(instruction, pointers, fo):
	return threeRegFieldInstruction(instruction,pointers, fo, "06")

def instr_Or(instruction, pointers, fo):
	return threeRegFieldInstruction(instruction,pointers, fo, "07")

def instr_Save(instruction, pointers, fo):
	return writeFieldWithStackInstruction(instruction, pointers, fo, "15")

def instr_Load(instruction, pointers, fo):
	return writeFieldWithStackInstruction(instruction, pointers, fo, "16")

def instr_Rsf(instruction, pointers, fo):
	return writeAndRead1Instruction(instruction, pointers, fo, "09")

def instr_Lsf(instruction, pointers, fo):
	return writeAndRead1Instruction(instruction, pointers, fo, "0a")

def instr_Ars(instruction, pointers, fo):
	return writeAndRead1Instruction(instruction, pointers, fo, "0b")

def instr_Neg(instruction, pointers, fo):
	return writeAndRead2Instruction(instruction, pointers, fo, "0c")

def instr_Not(instruction, pointers, fo):
	return writeAndRead2Instruction(instruction, pointers, fo, "08")

def instr_Pushf(instruction, pointers, fo):
	fo.write("120e f000")
	return 1

def instr_Popf(instruction, pointers, fo):
	fo.write("130e f000")
	return 1

def instr_Int(instruction, pointers, fo):
	if len(instruction) < 3:
		CustomError.ERR_missingArgument(instruction[-1], '1')
		return 0
	if instruction[1][0] == 'd':
		temp = int(instruction[1][1:])
		if 0 > temp > 255:
			CustomError.ERR_invalidValue(instruction[-1], '1')
			return 0
		else:
			fo.write("{}{}{}".format("14", "0e f0", "%2.2x"%temp))
			return 1
	elif len(instruction[1]) == 3 and instruction[1][0] == 'h':
		bottom_byte = []
		for c in instruction[1][1:]:
			if '0' <= c <= '9' or 'a' <= c <= 'f':
				bottom_byte.append(c)
			else:
				CustomError.ERR_invalidValue(instruction[-1], '1')
				return 0
		fo.write("{}{}{}".format("14", "0e f0", instruction[1][1:]))
		return 1
	else:
		CustomError.ERR_invalidArgumentType(instruction[-1], '2', "d (decimal), h (hexadecimal)")
		return 0

def instr_Tst(instruction, pointers, fo):
	if len(instruction) < 4:
		if len(instruction) < 3:
			CustomError.ERR_missingArgument(instruction[-1], '1')
			return 0
		CustomError.ERR_missingArgument(instruction[-1], '2')
		return 0
	if instruction[1][0] != 'r':
		CustomError.ERR_invalidArgumentType(instruction[-1], '1', "register reference")
		return 0
	elif instruction[2][0] != 'r':
		CustomError.ERR_invalidArgumentType(instruction[-1], '2', "register reference")
		return 0
	topmid_byte_bottom_nibble = registers.get(instruction[1], None)
	if topmid_byte_bottom_nibble == None:
		CustomError.ERR_invalidValue(instruction[-1], '1')
		return 0
	botmid_byte_top_nibble = registers.get(instruction[2], None)
	if botmid_byte_top_nibble == None:
		CustomError.ERR_invalidValue(instruction[-1], '2')
		return 0
	fo.write("{}{} {}{}".format("190", topmid_byte_bottom_nibble, botmid_byte_top_nibble, "000"))
	return 1

def instr_Nop(instruction, pointers, fo):
	fo.write("0000 0000")
	return 1

instructions_repository = {
	"jmp":	instr_Jmp,
	"inc":	instr_Inc,
	"dec":	instr_Dec,
	"push":	instr_Push,
	"pop":	instr_Pop,
	"call":	instr_Call,
	"ret":	instr_Ret,
	"mov":	instr_Mov,
	"add":	instr_Add,
	"addc":	instr_Addc,
	"sub":	instr_Sub,
	"subb":	instr_Subb,
	"xor":	instr_Xor,
	"and":	instr_And,
	"or":	instr_Or,
	"save":	instr_Save,
	"load":	instr_Load,
	"rsf":	instr_Rsf,
	"lsf":	instr_Lsf,
	"ars":	instr_Ars,
	"neg":	instr_Neg,
	"not":	instr_Not,
	"pushf":instr_Pushf,
	"popf":	instr_Popf,
	"int":	instr_Int,
	"tst":	instr_Tst,
	"nop":	instr_Nop
}

def resolveInstruction(instruction, pointers, fo):
	return instructions_repository[instruction[0]](instruction, pointers, fo)
