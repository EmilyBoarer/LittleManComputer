import sys, pickle

def chars(i, count):
    while len(i)  < count:
        i = "0"+i
    return i

print(">>ASSEMBLER<<: Assembling " + sys.argv[1] + " into " + sys.argv[2] + " ...")

f = open(sys.argv[1])
assembly = f.read().upper()
f.close()

opcodetranslate = {
    "ADD": "1",
    "SUB": "2",
    "STA": "3",
    "LDA": "5",
    "BRA": "6",
    "BRZ": "7",
    "BRP": "8"
    }

opcodes = ["ADD","SUB","STA","LDA","BRA","BRZ","BRP","INP","OUT","HLT","DAT"]

labels = {} #time to collect the labels' addresses
lineno = 0
for line in assembly.split("\n"):       # run a pass to extract label line numbers to substitute
    parts = line.split(" ")
    
    # get rid of whitespace
    while "" in parts:
        parts.remove("")

    # use actual information
    opcoded = False
    for part in parts:
        if not part in opcodes and not opcoded:
            labels[part] = str(lineno) # add to parsing table
        if part in opcodes and not opcoded:
            opcoded = True
    lineno += 1

program = [] # can properly compile and sub in labels now that the assembler knows what address they are tied to
lineno = 0
for line in assembly.split("\n"):           #run the final pass where labels can now be subbed for memory locations / line numbers
    parts = line.split(" ")
    
    # get rid of whitespace
    while "" in parts:
        parts.remove("")

    # use actual information
    label = ""
    operand = ""
    opcode = ""

    opcoded = False
    for part in parts:
        if not part in opcodes and not opcoded:
            label = part
        if part in opcodes and not opcoded:
            opcode = part
            opcoded = True
        if opcoded:
            operand = part
    # debug only print("L:" + label + " OPCODE:" + opcode + " OPERAND:" + operand)
    if opcode == "INP":
        inst = "901"
    elif opcode == "OUT":
        inst = "902"
    elif opcode == "HLT":
        inst = "000"
    elif opcode == "DAT":
        if operand == "": operand = "0" # initilised to 0
        inst = chars(operand,3) # set to vaue assigned
    else: # other "normal" insructions
        inst = opcodetranslate[opcode] + chars(labels[operand], 2)
    program.append(inst)
    lineno += 1

# save output to external file using pickle makes it easy to then import them again when being read, would be fairly easy to just use a txt file though i imagine
f=open(sys.argv[2], "wb")
pickle.dump(program, f)
f.close()

print(">>ASSEMBLER<<: Finished Assembling Successfully")