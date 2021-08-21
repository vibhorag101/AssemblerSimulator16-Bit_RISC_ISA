from sys import stdin
from typing import Type
registers = {
    "000":"00000000",
    "001":"00000000",
    "010":"00000000",
    "011":"00000000",
    "100":"00000000",
    "101":"00000000",
    "110":"00000000",
    #Flags Register last 4 bits 0- Overflow
    "111": ["0","0","0","0"]}

mainList =[]
memoryList =[]
pc = "00000000"
halted = False
varList= {}


def add(reg1,reg2,reg3):
    overFlowFlag=False
    re1 = int(reg1,2)
    re2 = int(reg2,2)
    re3 = int(reg3,2)

    re1 = re2 + re3
    if(re1<0):
        re1=0;
        registers["111"][0]="1"
    elif(re1>65535):
        registers["111"][0]="1"
        overFlowFlag=True

    binR1= bin(re1)[2:]
    
    if(overFlowFlag):
        takeOverFlow = len(binR1)-16
        binR1=binR1[takeOverFlow:]

    registers[reg1]= binR1.zfill(16)


def sub(reg1,reg2,reg3):
    overFlowFlag=False
    re1 = int(reg1,2)
    re2 = int(reg2,2)
    re3 = int(reg3,2)

    re1 = re2 - re3
    if(re1<0):
        re1=0;
        registers["111"][0]="1"
    elif(re1>65535):
        registers["111"][0]="1"
        overFlowFlag=True

    binR1= bin(re1)[2:]
    
    if(overFlowFlag):
        takeOverFlow = len(binR1)-16
        binR1=binR1[takeOverFlow:]

    registers[reg1]= binR1.zfill(16)

def mul(reg1,reg2,reg3):
    overFlowFlag=False
    re1 = int(reg1,2)
    re2 = int(reg2,2)
    re3 = int(reg3,2)

    re1 = re2 * re3
    if(re1<0):
        re1=0;
        registers["111"][0]="1"
    elif(re1>65535):
        registers["111"][0]="1"
        overFlowFlag=True

    binR1= bin(re1)[2:]
    
    if(overFlowFlag):
        takeOverFlow = len(binR1)-16
        binR1=binR1[takeOverFlow:]

    registers[reg1]= binR1.zfill(16)

def div(reg3,reg4):
    re3 = int(reg3,2)
    re4 = int(reg4,2)
    re0= re3//re4
    re1 = re3 % re4
    binR0= bin(re0)[2:]
    binR1= bin(re1)[2:]

    registers["000"]= binR0.zfill(16)
    registers["001"]= binR1.zfill(16)


def movimm(reg1,imm):
    reg1 = imm

def movreg(reg1,reg2):
    reg1 = reg2

def ld(reg1,memory):
    reg1= varList[memory]

def st(reg1,memory):
    varList[memory]= reg1






def rtsf(reg1,imm):
    n = int(imm,2)
    re1 = int(reg1,2)
    re1= re1>>n
    binR1= bin(re1)[2:]
    registers[reg1]= binR1.zfill(16)

def ltsf(reg1,imm):
    n = int(imm,2)
    re1 = int(reg1,2)
    re1= re1<<n
    binR1= bin(re1)[2:]
    registers[reg1]= binR1.zfill(16)


def xor(reg1,reg2,reg3):
    re1 = int(reg1,2)
    re2 = int(reg2,2)
    re3 = int(reg3,2)

    re1 = re2 ^ re3

    binR1= bin(re1)[2:]
    registers[reg1]= binR1.zfill(16)

def oor(reg1,reg2,reg3):
    re1 = int(reg1,2)
    re2 = int(reg2,2)
    re3 = int(reg3,2)

    re1 = re2 | re3

    binR1= bin(re1)[2:]
    registers[reg1]= binR1.zfill(16)

def aand(reg1,reg2,reg3):
    re1 = int(reg1,2)
    re2 = int(reg2,2)
    re3 = int(reg3,2)

    re1 = re2 & re3

    binR1= bin(re1)[2:]
    registers[reg1]= binR1.zfill(16)

#here we do the true bitwise operation
#we dont use ~ operator and rather invert each bit manually
def invert(reg1,reg2):
    temp = ""
    for i in reg2:
        if(i=="0"):
            temp=temp+"1"
        else:
            temp=temp+ "0"
    registers[reg1]= temp.zfill(16)

def compare(reg1,reg2):
    if reg1 < reg2:
        registers["111"][1]="1"
    elif reg1 > reg2:
        registers["111"][2]="1"
    elif reg1 == reg2:
        registers["111"][3]="1"


def uncjmp(memoryAdress):
    instLine = int(memoryAdress,2)
    instruction= mainList[instLine]
    # now just need to execute the instruction as done in normal case, just replicate from the for loop


def jlt():
    pass

def jgt():
    pass

def je():
    pass

def hlt():
    halted = True


for commandInput in stdin:
    if(commandInput != ""):
        commandInput = commandInput.strip()
        if(commandInput == ""):
            continue
        mainList.append(commandInput)
    else:
        break

lineCounter =0
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
        reg1 = registers[code[5:8]]
        memoryVar = registers[code[8:]]
        ld(reg1,memoryVar)

    elif opc == "00101":
        reg1 = registers[code[5:8]]
        memoryVar = registers[code[8:]]
        st(reg1,memoryVar)
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

    pc = bin(lineCounter)[2:].zfill(8)
    lineCounter = lineCounter + 1

    # printing part
    flagPrint = "".join(registers["111"]).zfill(16)
    reqString = pc+" "+ registers["000"]+ " " + registers["001"]+ " " + registers["010"]+ " " + registers["011"]+ " " + registers["100"]+ " " + registers["101"]+ " " + registers["110"]+ " " + flagPrint

    memoryList.append(reqString)

#memoryDump
for i in mainList:
    memoryList.append(i)

dictItems = varList.items()
varList= sorted(dictItems)
for i in varList:
    memoryList.append(varList[i][1])

extraLines = 256 - len(memoryList)
for i in range(extraLines):
    memoryList.append("0000000000000000")

for i in memoryList:
    print(i)
    

    


