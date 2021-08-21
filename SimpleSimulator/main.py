from sys import stdin
registers = {
    "000":"r1",
    "001":"r2",
    "010":"r3",
    "011":"r4",
    "100":"r5",
    "101":"r6"}

mainList =[]


r1 = 00000000
r2 = 00000000
r3 = 00000000
r4 = 00000000
r5 = 00000000
r6 = 00000000

flags = [0,0,0,0] 
pc = 00000000
halted = False


def add(reg1,reg2,reg3):
    re1 = int(reg1,2)
    re2 = int(reg2,2)
    re3 = int(reg3,2)

    re1 = re2 + re3

    re1 = int(re1,2)
    re1 = str(re1)
    reg1 = int(str(re1).zfill(16))


def sub(reg1,reg2,reg3):
    re1 = int(reg1,2)
    re2 = int(reg2,2)
    re3 = int(reg3,2)

    re1 = re2 - re3

    re1 = int(re1,2)
    re1 = str(re1)
    reg1 = int(str(re1).zfill(16))

def movimm(reg1,imm):
    reg1 = imm

def movreg(reg1,reg2):
    reg1 = reg2

def ld():

def st():

def mul(reg1,reg2,reg3):
    re1 = int(reg1,2)
    re2 = int(reg2,2)
    re3 = int(reg3,2)

    re1 = re2*re3
    re1 = int(re1,2)
    re1 = str(re1)
    reg1 = int(str(re1).zfill(16))


def div(reg1,reg2,reg3):
    re1 = int(reg1,2)
    re2 = int(reg2,2)
    re3 = int(reg3,2)
    

    re1 = re2/re3
    re1 = int(re1,2)
    re1 = str(re1)
    reg1 = int(str(re1).zfill(16))

def rtsf(reg1,imm):
    n = int(imm,2)
    for x in range(n):
        reg1>>

def ltsf(reg1,imm):
    n = int(imm,2)
    for x in range(n):
        reg1<<

def xor(reg1,reg2,reg3):
    reg1 = reg2^reg3

def oor(reg1,reg2,reg3):
    reg1 = reg2|reg3

def aand(reg1,reg2,reg3):
    reg1 = reg2&reg3

def invert(reg1,reg2):
    reg1 = ~reg2

def compare(reg1,reg2):
    if reg1 < reg2:
        flags[1] = 1
    elif reg1 > reg2:
        flags[2] = 1
    elif reg1 == reg2:
        flags[3] = 1


def uncjmp(memoryAdress):
    instLine = int(memoryAdress,2)
    instruction= mainList[instLine]
    # now just need to execute the instruction as done in normal case, just replicate from the for loop


def jlt():

def jgt():

def je():

def hlt():
    halted = True


for commandInput in stdin:
    if(commandInput != ""):
        commandInput = commandInput.strip()
        if(commandInput == ""):
            continue
        command = commandInput.split()
        mainList.append(command)
    else:
        break

for code in mainList:
    opc = code[0:5]

    if opc == "00000" :
        reg1 = registers[code[7:10]]
        reg2 = registers[code[10:13]]
        reg3 = registers[code[13:]]

        add(reg1,reg2,reg3)

    elif opc == "00001":
        reg1 = registers[code[7:10]]
        reg2 = registers[code[10:13]]
        reg3 = registers[code[13:]]

        sub(reg1,reg2,reg3)

    elif opc == "00010":
        reg1 = registers[code[5:8]]
        imm = "00000000" + code[8:]
        imm = int(imm)
        movimm(reg1,imm)

    elif opc == "00011":
        reg1 = registers[code[10:13]]
        reg2 = registers[code[13:]]

        movreg(reg1,reg2)

    elif opc == "00100":
        ld()
    elif opc == "00101":
        st()
    elif opc == "00110":
        reg1 = registers[code[7:10]]
        reg2 = registers[code[10:13]]
        reg3 = registers[code[13:]]

        mul(reg1,reg2,reg3)

    elif opc == "00111":
        reg1 = registers[code[7:10]]
        reg2 = registers[code[10:13]]
        

        div(reg1,reg2,reg3)

    elif opc == "01000":
        reg1 = registers[code[5:8]]
        imm = "00000000" + code[8:]
        imm = int(imm)

        rtsf(reg1,imm)

    elif opc == "01001":
        reg1 = registers[code[5:8]]
        imm = "00000000" + code[8:]
        imm = int(imm)

        ltsf(reg1,imm)

    elif opc == "01010":
        reg1 = registers[code[7:10]]
        reg2 = registers[code[10:13]]
        reg3 = registers[code[13:]]

        xor(reg1,reg2,reg3)

    elif opc == "01011":
        reg1 = registers[code[7:10]]
        reg2 = registers[code[10:13]]
        reg3 = registers[code[13:]]

        oor(reg1,reg2,reg3)

    elif opc == "01100":
        reg1 = registers[code[7:10]]
        reg2 = registers[code[10:13]]
        reg3 = registers[code[13:]]

        aand(reg1,reg2,reg3)

    elif opc == "01101":
        reg1 = registers[code[10:13]]
        reg2 = registers[code[13:]]

        invert(reg1,reg2)

    elif opc == "01110":
        reg1 = registers[code[10:13]]
        reg2 = registers[code[13:]]

        compare(reg1,reg2)
    elif opc == "01111":
        memAdr = code[8:15]
        uncjmp(memAdr)
    elif opc == "10000":
        jlt()
    elif opc == "10001":
        jgt()
    elif opc == "10010":
        je()
    elif opc == "10011":
        hlt()


