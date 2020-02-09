import sys, pickle

#open the file that is specified when calling on the commandline
f = open(sys.argv[1], "rb")
program = pickle.load(f)    # pickle just makes it really easy to get a datastructure into a file
f.close()

print(">>LRE<<\nWELCOME TO THE LMC RUNTIME ENV. (a.k.a LRE)")
print(">>LRE<< running", sys.argv[1])

# set up the memory environment
memory = ["000" for n in range(100)]
for line in range(len(program)):
    memory[line] = program[line]

def chars(i, count):
    if int(i) >= 0:
        while len(i) < count:
            i = "0"+i
        return i
    else:
        i = i[1:]
        while len(i) < count:
            i = "0"+i
        return "-"+i

PC = "000"
ACC = "000"
CIR = "000"
MBR = "000" # kind of redundant, but used for readability purposes

CLOCK = True  #true until HLT is called
while CLOCK:
    MBR = memory[int(PC)]
    CIR = MBR ; PC = chars(str(int(PC)+1),3) # increment PC by 1
    # print(CIR, ACC)
    if CIR[0] == "1": #ADD
        MBR = memory[int(CIR[1:3])]
        ACC = chars(str(int(ACC) + int(MBR)),3) # simulate ALU with this line
    elif CIR[0] == "2": #SUB
        MBR = memory[int(CIR[1:3])]
        ACC = chars(str(int(ACC) - int(MBR)),3) # simulate ALU with this line
    elif CIR[0] == "3": #STA
        memory[int(CIR[1:3])] = ACC
    elif CIR[0] == "5": #LDA
        ACC = memory[int(CIR[1:3])]
    elif CIR[0] == "6": #BRA
        PC = CIR[1:3]
    elif CIR[0] == "7": #BRZ
        if int(ACC) == 0:
            PC = CIR[1:3]
    elif CIR[0] == "8": #BRP
        if int(ACC) >= 0:
            PC = CIR[1:3]
    elif CIR == "901": #INP
        ACC = input("INPUT -> ")[:3]
    elif CIR == "902": #OUT
        print(ACC)
    elif CIR == "000": #HLT
        CLOCK = False





