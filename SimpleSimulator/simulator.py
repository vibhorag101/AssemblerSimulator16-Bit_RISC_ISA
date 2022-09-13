from sys import stdin
from typing import Type
registers = {
    "000": "0000000000000000",
    "001": "0000000000000000",
    "010": "0000000000000000",
    "011": "0000000000000000",
    "100": "0000000000000000",
    "101": "0000000000000000",
    "110": "0000000000000000",
    # Flags Register last 4 bits 0- Overflow
    "111": ["0", "0", "0", "0"]}

mainList = []
memoryList = []
halted = False
varList = {}
haltFlag = False


def add(r1, r2, r3):
    reg1 = registers[r1]
    reg2 = registers[r2]
    reg3 = registers[r3]
    overFlowFlag = False
    re1 = int(reg1, 2)
    re2 = int(reg2, 2)
    re3 = int(reg3, 2)

    re1 = re2 + re3
    if(re1 < 0):
        re1 = 0
        registers["111"][0] = "1"
    elif(re1 > 65535):
        registers["111"][0] = "1"
        overFlowFlag = True

    binR1 = bin(re1)[2:]

    if(overFlowFlag):
        takeOverFlow = len(binR1)-16
        binR1 = binR1[takeOverFlow:]
    else:
        registers["111"]= ["0", "0", "0", "0"]
    registers[r1] = binR1.zfill(16)


def sub(r1, r2, r3):
    reg1 = registers[r1]
    reg2 = registers[r2]
    reg3 = registers[r3]
    overFlowFlag = False
    re1 = int(reg1, 2)
    re2 = int(reg2, 2)
    re3 = int(reg3, 2)

    re1 = re2 - re3
    if(re1 < 0):
        re1 = 0
        registers["111"][0] = "1"
        overFlowFlag = True
    elif(re1 >= 65535):
        registers["111"][0] = "1"
        overFlowFlag = True

    binR1 = bin(re1)[2:]

    if(overFlowFlag):
        takeOverFlow = len(binR1)-16
        binR1 = binR1[takeOverFlow:]
    else:
        registers["111"]= ["0", "0", "0", "0"]

    registers[r1] = binR1.zfill(16)


def mul(r1, r2, r3):
    reg1 = registers[r1]
    reg2 = registers[r2]
    reg3 = registers[r3]
    overFlowFlag = False
    re1 = int(reg1, 2)
    re2 = int(reg2, 2)
    re3 = int(reg3, 2)

    re1 = re2 * re3
    if(re1 < 0):
        re1 = 0
        registers["111"][0] = "1"
    elif(re1 > 65535):
        registers["111"][0] = "1"
        overFlowFlag = True

    binR1 = bin(re1)[2:]

    if(overFlowFlag):
        takeOverFlow = len(binR1)-16
        binR1 = binR1[takeOverFlow:]
        registers["111"]= ["1", "0", "0", "0"]
    else:
        registers["111"]= ["0", "0", "0", "0"]

    registers[r1] = binR1.zfill(16)


def div(r3, r4):

    reg3 = registers[r3]
    reg4 = registers[r4]
    re3 = int(reg3, 2)
    re4 = int(reg4, 2)
    re0 = re3//re4
    re1 = re3 % re4
    binR0 = bin(re0)[2:]
    binR1 = bin(re1)[2:]

    registers["000"] = binR0.zfill(16)
    registers["001"] = binR1.zfill(16)
    registers["111"]= ["0", "0", "0", "0"]


def movimm(reg1, imm):
    r1 = imm
    registers[reg1] = r1.zfill(16)
    registers["111"]= ["0", "0", "0", "0"]


def movreg(reg1, reg2):
    if(reg2 == "111"):
        flagReg = "".join(registers["111"]).zfill(16)
        registers[reg1] = flagReg
    else:
        r1= registers[reg2]
        registers[reg1] = r1
    registers["111"]= ["0", "0", "0", "0"]


def ld(reg1, memory):
    try:
        r1 = varList[memory]
    except:
        r1="0000000000000000"
    registers[reg1] = r1
    registers["111"]= ["0", "0", "0", "0"]


def st(reg1, memory):
    varList[memory] = registers[reg1]
    registers["111"]= ["0", "0", "0", "0"]


def rtsf(reg1, imm):
    n = int(imm, 2)
    re1 = int(registers[reg1], 2)
    re1 = re1 >> n
    binR1 = bin(re1)[2:]
    registers[reg1] = binR1.zfill(16)
    registers["111"]= ["0", "0", "0", "0"]


def ltsf(reg1, imm):
    n = int(imm, 2)
    re1 = int(registers[reg1], 2)
    re1 = re1 << n
    binR1 = bin(re1)[2:]
    registers[reg1] = binR1.zfill(16)
    registers["111"]= ["0", "0", "0", "0"]


def xor(reg1, reg2, reg3):
    re1 = int(registers[reg1], 2)
    re2 = int(registers[reg2], 2)
    re3 = int(registers[reg3], 2)

    re1 = re2 ^ re3

    binR1 = bin(re1)[2:]
    registers[reg1] = binR1.zfill(16)
    registers["111"]= ["0", "0", "0", "0"]


def oor(reg1, reg2, reg3):
    re1 = int(registers[reg1], 2)
    re2 = int(registers[reg2], 2)
    re3 = int(registers[reg3], 2)

    re1 = re2 | re3

    binR1 = bin(re1)[2:]
    registers[reg1] = binR1.zfill(16)
    registers["111"]= ["0", "0", "0", "0"]


def aand(reg1, reg2, reg3):
    re1 = int(registers[reg1], 2)
    re2 = int(registers[reg2], 2)
    re3 = int(registers[reg3], 2)

    re1 = re2 & re3

    binR1 = bin(re1)[2:]
    registers[reg1] = binR1.zfill(16)
    registers["111"]= ["0", "0", "0", "0"]

# here we do the true bitwise operation
# we dont use ~ operator and rather invert each bit manually


def invert(reg1, reg2):
    temp = ""
    for i in registers[reg2]:
        if(i == "0"):
            temp = temp+"1"
        else:
            temp = temp + "0"
    registers[reg1] = temp.zfill(16)
    registers["111"]= ["0", "0", "0", "0"]


def compare(r1, r2):
    reg1= registers[r1]
    reg2 = registers[r2]
    re1 = int(reg1, 2)
    re2 = int(reg2, 2)
    if(re1 == re2):
        registers["111"][3] = "1"
    elif(re1>re2):
        registers["111"][2] = "1"
    elif(re1<re2):
        registers["111"][1] = "1"


def uncjmp():
    memAdr = code[8:16]
    registers["111"]= ["0", "0", "0", "0"]
    return int(memAdr, 2)


def jlt():
    memAdr = code[8:16]
    registers["111"]= ["0", "0", "0", "0"]
    return int(memAdr, 2)


def jgt():
    memAdr = code[8:16]
    registers["111"]= ["0", "0", "0", "0"]
    return int(memAdr, 2)


def je():
    memAdr = code[8:16]
    registers["111"]= ["0", "0", "0", "0"]
    return int(memAdr, 2)


def hlt():
    registers["111"]= ["0", "0", "0", "0"]
    halted = True


for commandInput in stdin:
    if(commandInput != ""):
        commandInput = commandInput.strip()
        if(commandInput == ""):
            continue
        mainList.append(commandInput)
    else:
        break


i = 0
while i <= (len(mainList)-1):
    pc = bin(i)[2:].zfill(8)
    code = mainList[i]

    opc = code[0:5]

    if opc == "00000":
        reg1 = code[7:10]
        reg2 = code[10:13]
        reg3 = code[13:]

        add(reg1, reg2, reg3)
        i = i+1

    elif opc == "00001":
        reg1 = code[7:10]
        reg2 = code[10:13]
        reg3 = code[13:]

        sub(reg1, reg2, reg3)
        i = i+1

    elif opc == "00010":
        reg1 = code[5:8]
        imm = "00000000" + code[8:]
        movimm(reg1, imm)
        i = i+1

    elif opc == "00011":
        reg1 = code[10:13]
        reg2 = code[13:]

        movreg(reg1, reg2)
        i = i+1

    elif opc == "00100":
        reg1 = code[5:8]
        memoryVar = code[8:]
        ld(reg1, memoryVar)
        i = i+1

    elif opc == "00101":
        reg1 = code[5:8]
        memoryVar = code[8:]
        st(reg1, memoryVar)
        i = i+1

    elif opc == "00110":
        reg1 = code[7:10]
        reg2 = code[10:13]
        reg3 = code[13:]

        mul(reg1, reg2, reg3)

        i = i+1

    elif opc == "00111":
        reg1 = code[10:13]
        reg2 = code[13:16]

        div(reg1, reg2)

        i = i+1

    elif opc == "01000":
        reg1 = code[5:8]
        imm = "00000000" + code[8:]

        rtsf(reg1, imm)
        i = i+1

    elif opc == "01001":
        reg1 = code[5:8]
        imm = "00000000" + code[8:]

        ltsf(reg1, imm)
        i = i+1

    elif opc == "01010":
        reg1 = code[7:10]
        reg2 = code[10:13]
        reg3 = code[13:]

        xor(reg1, reg2, reg3)
        i = i+1

    elif opc == "01011":
        reg1 = code[7:10]
        reg2 = code[10:13]
        reg3 = code[13:]

        oor(reg1, reg2, reg3)
        i = i+1

    elif opc == "01100":
        reg1 = code[7:10]
        reg2 = code[10:13]
        reg3 = code[13:]

        aand(reg1, reg2, reg3)
        i = i+1

    elif opc == "01101":
        reg1 = code[10:13]
        reg2 = code[13:]

        invert(reg1, reg2)
        i = i+1

    elif opc == "01110":
        reg1 = code[10:13]
        reg2 = code[13:]

        compare(reg1, reg2)
        i = i+1

    elif opc == "01111":
        i = uncjmp()

    elif opc == "10000":

        if registers["111"][1] == "1":
            i = jlt()
        else:
            registers["111"]= ["0", "0", "0", "0"]
            i = i+1

    elif opc == "10001":
        if registers["111"][2] == "1":
            i = jgt()

        else:
            registers["111"]= ["0", "0", "0", "0"]
            i = i+1

    elif opc == "10010":
        if registers["111"][3] == "1":
            i = je()

        else:
            registers["111"]= ["0", "0", "0", "0"]
            i = i+1

    elif opc == "10011":
        registers["111"]= ["0", "0", "0", "0"]
        haltFlag = True
        i = i+1


    # printing part
    flagPrint = "".join(registers["111"]).zfill(16)
    reqString = pc+" " + registers["000"] + " " + registers["001"] + " " + registers["010"] + " " + \
        registers["011"] + " " + registers["100"] + " " + \
        registers["101"] + " " + registers["110"] + " " + flagPrint

    memoryList.append(reqString)
    if(haltFlag):
        break

# memoryDump
dumpCounter = 0
for i in mainList:
    memoryList.append(i)
    dumpCounter = dumpCounter + 1
dictItems = varList.items()
varList = sorted(dictItems)
if(len(varList) > 0):
    for i in varList:
        memoryList.append(i[1])
        dumpCounter = dumpCounter + 1

extraLines = 256 - dumpCounter
for i in range(extraLines):
    memoryList.append("0000000000000000")

for i in memoryList:
    print(i)
