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

def instr_Jmp(instruction, pointers, fo):
	top_byte = "0d"
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
		CustomError.ERR_invalidArgumentType(instruction[-1], '2', "reference")
		return 0
	temp = pointers.get(instruction[2], None)
	if temp == None:
		CustomError.ERR_labelMissing(instruction[-1])
		return 0
	low_bytes = int(temp)
	fo.write("{}{}{} {}".format(top_byte, '0', topmid_byte_bottom_nibble,"%.4x"%(low_bytes)))
	return 1

def instr_Inc(instruction, pointers, fo):
	top_byte = "17"
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
	
	
def instr_Dec(instruction, pointers, fo):
	top_byte = "18"
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
	topmid_byte_top_nibble = registers.get(instruction[2], None)
	if topmid_byte_top_nibble == None:
		CustomError.ERR_invalidValue(instruction[-1], '1')
		return 0
	botmid_byte_top_nibble = registers.get(instruction[3], None)
	if botmid_byte_top_nibble == None:
		CustomError.ERR_invalidValue(instruction[-1], '2')
		return 0
	fo.write("{}{}{} {}{}".format(top_byte, topmid_byte_top_nibble, '0', botmid_byte_top_nibble, "000"))
	return 1


def instr_Push(instruction, pointers, fo):
	print(instruction)
def instr_Pop(instruction, pointers, fo):
	print(instruction)
def instr_Call(instruction, pointers, fo):
	print(instruction)
def instr_Ret(instruction, pointers, fo):
	print(instruction)
def instr_Mov(instruction, pointers, fo):
	top_byte = "00"
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
		fo.write("{}{}{} {}".format(top_byte, topmid_byte_top_nibble, topmid_byte_bottom_nibble, "0000"))
		return 1
	elif instruction[2][0] == 'd':
		tempnum = int(instruction[3][1:])
		if -32768 < tempnum < 32767:
			CustomError.ERR_invalidValue(instruction[-1], '2')
			return 0
		else:
			fo.write("{}{}{} {}".format(top_byte, topmid_byte_top_nibble, '0', "%4.4x"%(int(instruction[3][1:]))))
			return 1
	elif instruction[2].length == 5 and instruction[2][0] == 'h':
		bottom_bytes = []
		for c in instruction[2][1:]:
			if c >= 0 and c <= 9 or c == 'a' or c == 'b' or c == 'c' or c == 'd' or c== 'e' or c == 'f':
				bottom_bytes.append(c)
			else:
				CustomError.ERR_invalidValue(instruction[-1], '2')
				return 0
		fo.write("{}{}{} {}{}{}{}".format(top_byte, topmid_byte_top_nibble, '0', instruction[2][1], instruction[2][2], instruction[2][3], instruction[2][4]))
		return 1
	else:
		CustomError.ERR_invalidArgumentType(instruction[-1], '2', "d (decimal), h (hexadecimal) or r (register reference)")
		return 0

def instr_Add(instruction, pointers, fo):
	print(instruction)
def instr_Addc(instruction, pointers, fo):
	print(instruction)
def instr_Sub(instruction, pointers, fo):
	print(instruction)
def instr_Subb(instruction, pointers, fo):
	print(instruction)
def instr_Xor(instruction, pointers, fo):
	print(instruction)
def instr_And(instruction, pointers, fo):
	print(instruction)
def instr_Or(instruction, pointers, fo):
	print(instruction)
def instr_Save(instruction, pointers, fo):
	print(instruction)
def instr_Load(instruction, pointers, fo):
	print(instruction)
def instr_Rsf(instruction, pointers, fo):
	print(instruction)
def instr_Lsf(instruction, pointers, fo):
	print(instruction)
def instr_Ars(instruction, pointers, fo):
	print(instruction)
def instr_Neg(instruction, pointers, fo):
	print(instruction)
def instr_Not(instruction, pointers, fo):
	print(instruction)
def instr_Pushf(instruction, pointers, fo):
	print(instruction)
def instr_Popf(instruction, pointers, fo):
	print(instruction)
def instr_Int(instruction, pointers, fo):
	print(instruction)
def instr_Tst(instruction, pointers, fo):
	print(instruction)
def instr_Nop(instruction, pointers, fo):
	fo.write("0000 0000")
	
instructions_repository = {
	"jmp": instr_Jmp,
	"inc": instr_Inc,
	"dec": instr_Dec,
	"push": instr_Push,
	"pop": instr_Pop,
	"call": instr_Call,
	"ret": instr_Ret,
	"mov": instr_Mov,
	"add": instr_Add,
	"addc": instr_Addc,
	"sub": instr_Sub,
	"subb": instr_Subb,
	"xor": instr_Xor,
	"and": instr_And,
	"or": instr_Or,
	"save": instr_Save,
	"load": instr_Load,
	"rsf": instr_Rsf,
	"lsf": instr_Lsf,
	"ars": instr_Ars,
	"neg": instr_Neg,
	"not": instr_Not,
	"pushf": instr_Pushf,
	"popf": instr_Popf,
	"int": instr_Int,
	"tst": instr_Tst,
	"nop": instr_Nop
}


def resolveInstruction(instruction, pointers, fo):
	return instructions_repository[instruction[0]](instruction, pointers, fo)
