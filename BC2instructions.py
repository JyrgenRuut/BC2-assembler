
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
			return
		CustomError.ERR_missingArgument(instruction[-1], '2')
		return
	topmid_byte = jump_flags.get(instruction[1], None)
	if topmid_byte == None:
		CustomError.ERR_invalidArgument(instruction[-1], '1')
		return
	if instruction[2][0] != '&':
		CustomError.ERR_invalidArgumentType(instruction[-1], '2', "reference")
		return
	temp = pointers.get(instruction[2], None)
	if temp == None:
		CustomError.ERR_labelMissing(instruction[-1])
		return
	low_bytes = int(temp)
	fo.write(top_byte, topmid_byte, ".4x"%(low_bytes))

def instr_Inc(instruction, pointers, fo):
	top_byte = "17"
	if len(instruction) < 4:
		if len(instruction) < 3:
			CustomError.ERR_missingArgument(instruction[-1], '1')
			return
		CustomError.ERR_missingArgument(instruction[-1], '2')
		return
	if instruction[2][0] != 'r':
		CustomError.ERR_invalidArgumentType(instruction[-1], '1', "register reference")
		return
	elif instruction[3][0] != 'r':
		CustomError.ERR_invalidArgumentType(instruction[-1], '2', "register reference")
		return
	topmid_byte_top_nibble = registers.get([instruction[2], None)
	if topmid_byte == None:
		CustomError.ERR_invalidValue(instruction[-1], '1')
		return
	botmid_byte_top_nibble = registers.get(instruction[3], None)
	if botmid_byte == None:
		CustomError.ERR_invalidValue(instruction[-1], '2')
		return
	fo.write(top_byte, topmid_byte_top_nibble, '0' botmid_byte_top_nibble, "000")
	
	
def instr_Dec(instruction, pointers, fo):
	top_byte = "17"
	if len(instruction) < 4:
		if len(instruction) < 3:
			CustomError.ERR_missingArgument(instruction[-1], '1')
			return
		CustomError.ERR_missingArgument(instruction[-1], '2')
		return
	if instruction[2][0] != 'r':
		CustomError.ERR_invalidArgumentType(instruction[-1], '1', "register reference")
		return
	elif instruction[3][0] != 'r':
		CustomError.ERR_invalidArgumentType(instruction[-1], '2', "register reference")
		return
	if int(instruction[2][1:]) >= 16 or int(instruction[2][1:]) < 0:
		CustomError.ERR_invalidValue(instruction[-1], '1')
		return
	elif int(instruction[3][1:]) >= 16 or int(instruction[3][1:]) < 0:
		CustomError.ERR_invalidValue(instruction[-1], '2')
		return
	topmid_byte = ".1x"%(int(instruction[2][1:])) + '0'
	botmid_byte = ".1x"%(int(instruction[2][1:])) + '0'
	fo.write(top_byte, topmid_byte, botmid_byte, "00")


def instr_Push(instruction, pointers, fo):
	print(instruction)
def instr_Pop(instruction, pointers, fo):
	print(instruction)
def instr_Call(instruction, pointers, fo):
	print(instruction)
def instr_Ret(instruction, pointers, fo):
	print(instruction)
def instr_Mov(instruction, pointers, fo):
	if instruction[2][0] == 'h':
		
	elif instruction[2][0] == 'd':
		int(
		 
	print("%5.4x"% (47))

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
	"tst": instr_Tst
}


def resolveInstruction(instruction, pointers, fo):
	instructions_repository[instruction[0]](instruction, pointers, fo)
